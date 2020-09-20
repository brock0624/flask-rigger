/*
Navicat MySQL Data Transfer

Source Server         : zero.brock.fun
Source Server Version : 80019
Source Host           : zero.brock.fun:3306
Source Database       : scott

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-09-20 16:24:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('6b80088a05b1');

-- ----------------------------
-- Table structure for s_role
-- ----------------------------
DROP TABLE IF EXISTS `s_role`;
CREATE TABLE `s_role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of s_role
-- ----------------------------
INSERT INTO `s_role` VALUES ('1', 'user', null);
INSERT INTO `s_role` VALUES ('2', 'superuser', null);

-- ----------------------------
-- Table structure for s_roles_users
-- ----------------------------
DROP TABLE IF EXISTS `s_roles_users`;
CREATE TABLE `s_roles_users` (
  `user_id` int DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  KEY `role_id` (`role_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `s_roles_users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `s_role` (`id`),
  CONSTRAINT `s_roles_users_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `s_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of s_roles_users
-- ----------------------------
INSERT INTO `s_roles_users` VALUES ('1', '1');
INSERT INTO `s_roles_users` VALUES ('1', '2');

-- ----------------------------
-- Table structure for s_user
-- ----------------------------
DROP TABLE IF EXISTS `s_user`;
CREATE TABLE `s_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `username` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `last_login_at` datetime DEFAULT NULL,
  `current_login_at` datetime DEFAULT NULL,
  `last_login_ip` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `current_login_ip` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `login_count` int DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `confirmed_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `s_user_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of s_user
-- ----------------------------
INSERT INTO `s_user` VALUES ('1', 'admin', 'admin', '$pbkdf2-sha512$25000$bA3hfO8dY8x5L.VcixEiRA$P3Fz13PsFTL0pw0TFYRLFfsB1u8CFPtsFharEUJQlhnEosJuG9cVJN7/QXZXV/jypxRzcilzD3kfwU6.ReoDPQ', '2020-09-19 13:53:01', '2020-09-20 08:23:14', '127.0.0.1', '127.0.0.1', '2', '1', null);

-- ----------------------------
-- Table structure for t_codes
-- ----------------------------
DROP TABLE IF EXISTS `t_codes`;
CREATE TABLE `t_codes` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `code` varchar(64) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '代码',
  `code_value` varchar(660) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '代码值',
  `type` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '代码类型',
  `revision` int DEFAULT NULL COMMENT '乐观锁',
  `active` tinyint(1) DEFAULT NULL COMMENT '状态',
  `created_by` varchar(20) COLLATE utf8mb4_general_ci DEFAULT 'sys' COMMENT '创建人',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  `updated_by` varchar(20) COLLATE utf8mb4_general_ci DEFAULT 'sys' COMMENT '更新人',
  `updated_time` datetime DEFAULT NULL COMMENT '更新时间',
  `memo` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`),
  UNIQUE KEY `code_code_type` (`code`,`type`),
  CONSTRAINT `t_codes_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of t_codes
-- ----------------------------
INSERT INTO `t_codes` VALUES ('1', 'code1', 'test123', 'test', '0', '0', 'sys', '2020-09-19 22:07:58', 'sys', '2020-09-19 22:08:44', null);
