from flask import render_template, url_for, jsonify, request
from inventory_control import app, db, csrf
from inventory_control.models import Inventory, Product, Location
from inventory_control.forms import ProductForm, LocationForm, AddInventoryForm, RemoveInventoryForm
from flask_wtf.csrf import generate_csrf

@app.route("/")
def main():
    products = Product.query.all()
    locations = Location.query.all()
    form = ProductForm()
    location_form = LocationForm()
    add_inventory_form = AddInventoryForm()
    remove_inventory_form = RemoveInventoryForm()
    csrf_token = generate_csrf()
    return render_template('main.html', products=products, locations=locations, form=form, location_form=location_form, add_inventory_form=add_inventory_form, remove_inventory_form=remove_inventory_form, csrf_token=csrf_token)

@app.route("/new_product", methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            product = Product(name=form.name.data, description=form.description.data, price=form.price.data)
            db.session.add(product)
            db.session.commit()
            return jsonify({'success': True, 'product': {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price}})
        else:
            return jsonify({'success': False, 'message': 'Form validation failed', 'errors': form.errors})
    return render_template('new_product.html', form=form)

@app.route("/new_location", methods=['GET', 'POST'])
def new_location():
    form = LocationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            location = Location(name=form.name.data)
            db.session.add(location)
            db.session.commit()
            return jsonify({'success': True, 'location': {'id': location.id, 'name': location.name}})
        else:
            return jsonify({'success': False, 'message': 'Form validation failed', 'errors': form.errors})
    return render_template('new_location.html', form=form)

@app.route("/add_inventory", methods=['POST'])
def add_inventory():
    form = AddInventoryForm()
    if form.validate_on_submit():
        product_id = form.product_id.data
        location_id = form.location_id.data
        quantity = form.quantity.data

        inventory = Inventory.query.filter_by(product_id=product_id, location_id=location_id).first()
        if inventory:
            inventory.quantity += quantity
        else:
            inventory = Inventory(product_id=product_id, location_id=location_id, quantity=quantity)
            db.session.add(inventory)
        db.session.commit()
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Form validation failed', 'errors': form.errors})

@app.route("/remove_inventory", methods=['POST'])
def remove_inventory():
    form = RemoveInventoryForm()
    if form.validate_on_submit():
        product_id = form.product_id.data
        location_id = form.location_id.data

        inventory = Inventory.query.filter_by(product_id=product_id, location_id=location_id).first()
        if inventory:
            db.session.delete(inventory)
            db.session.commit()
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Form validation failed', 'errors': form.errors})

@app.route("/search", methods=['GET'])
def search():
    term = request.args.get('term', '')
    location_id = request.args.get('location_id', None)
    sort_field = request.args.get('sort_field', None)
    sort_order = request.args.get('sort_order', None)

    query = Product.query.filter(Product.name.ilike(f'%{term}%'))

    if location_id:
        query = query.join(Product.inventories).filter(Inventory.location_id == location_id)

    if sort_field == 'price':
        query = query.order_by(Product.price.asc() if sort_order == 'asc' else Product.price.desc())
    elif sort_field == 'quantity':
        query = query.outerjoin(Product.inventories).group_by(Product.id).order_by(db.func.coalesce(db.func.sum(Inventory.quantity), 0).asc() if sort_order == 'asc' else db.func.coalesce(db.func.sum(Inventory.quantity), 0).desc())

    products = query.all()

    return jsonify({'products': [{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'inventories': [{
            'location': {'name': inventory.location.name},
            'quantity': inventory.quantity
        } for inventory in product.inventories]
    } for product in products]})

@app.route("/locations_with_quantity", methods=['GET'])
def locations_with_quantity():
    product_id = request.args.get('product_id', None)
    if product_id:
        locations = db.session.query(Location.id, Location.name, Inventory.quantity).join(Inventory, Inventory.location_id == Location.id, isouter=True).filter(Inventory.product_id == product_id).all()
        return jsonify({'locations': [{'id': location.id, 'name': location.name, 'quantity': location.quantity} for location in locations]})
    return jsonify({'locations': []})