/*
 Navicat Premium Data Transfer

 Source Server         : work_connection
 Source Server Type    : MySQL
 Source Server Version : 90001 (9.0.1)
 Source Host           : localhost:3306
 Source Schema         : inventorydb

 Target Server Type    : MySQL
 Target Server Version : 90001 (9.0.1)
 File Encoding         : 65001

 Date: 11/08/2024 20:36:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for inventories
-- ----------------------------
DROP TABLE IF EXISTS `inventories`;
CREATE TABLE `inventories`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NULL DEFAULT NULL,
  `location_id` int NULL DEFAULT NULL,
  `quantity` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 56 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of inventories
-- ----------------------------
INSERT INTO `inventories` VALUES (49, 55, 19, 5);
INSERT INTO `inventories` VALUES (50, 55, 20, 1);
INSERT INTO `inventories` VALUES (51, 56, 22, 15);
INSERT INTO `inventories` VALUES (52, 56, 20, 1);
INSERT INTO `inventories` VALUES (53, 57, 21, 1);
INSERT INTO `inventories` VALUES (54, 59, 23, 29);
INSERT INTO `inventories` VALUES (55, 60, 24, 1337);

-- ----------------------------
-- Table structure for locations
-- ----------------------------
DROP TABLE IF EXISTS `locations`;
CREATE TABLE `locations`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of locations
-- ----------------------------
INSERT INTO `locations` VALUES (19, 'Москва');
INSERT INTO `locations` VALUES (20, 'Ижевск');
INSERT INTO `locations` VALUES (21, 'Верхне-Позимь');
INSERT INTO `locations` VALUES (22, 'Глазов');
INSERT INTO `locations` VALUES (23, 'Яр');
INSERT INTO `locations` VALUES (24, 'Детский Мир');

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `price` float NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of products
-- ----------------------------
INSERT INTO `products` VALUES (55, 'Монитор', 'Gigabyte', 45000);
INSERT INTO `products` VALUES (56, 'Процессор', 'AMD Ryzen 5', 24500);
INSERT INTO `products` VALUES (57, 'Мышь', 'HyperX', 3000);
INSERT INTO `products` VALUES (58, 'Носки чёрные', 'хлопковые', 150);
INSERT INTO `products` VALUES (59, 'Молоко', 'сгущенное', 140);
INSERT INTO `products` VALUES (60, 'Пистолет', 'игрушечный', 10000);

SET FOREIGN_KEY_CHECKS = 1;
