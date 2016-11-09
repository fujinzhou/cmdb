-- MySQL dump 10.13  Distrib 5.6.31, for Linux (x86_64)
--
-- Host: localhost    Database: reboot10
-- ------------------------------------------------------
-- Server version	5.6.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cabinet`
--

DROP TABLE IF EXISTS `cabinet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cabinet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL COMMENT '机柜名称',
  `idc_id` int(11) DEFAULT NULL COMMENT '所在机房ID',
  `u_num` varchar(10) DEFAULT NULL COMMENT 'U位',
  `power` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='机柜表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (1,'cabinet02',2,'12','12'),(2,'cabinet03',4,'1','12');
/*!40000 ALTER TABLE `cabinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idclist`
--

DROP TABLE IF EXISTS `idclist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idclist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT '机房名',
  `cabinets` varchar(50) NOT NULL COMMENT '机柜数量',
  `hosts` varchar(50) NOT NULL COMMENT '主机数量',
  `contacts` varchar(50) DEFAULT NULL COMMENT '联系人',
  `telephone` varchar(11) NOT NULL COMMENT '电话',
  `remarks` varchar(10) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='idc列表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idclist`
--

LOCK TABLES `idclist` WRITE;
/*!40000 ALTER TABLE `idclist` DISABLE KEYS */;
INSERT INTO `idclist` VALUES (2,'南汇机房','3','3','张三','123456','上海');
/*!40000 ALTER TABLE `idclist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(24) NOT NULL COMMENT '主机名',
  `lan_ip` varchar(24) DEFAULT NULL COMMENT '内网IP',
  `wan_ip` varchar(24) DEFAULT NULL COMMENT '外网IP',
  `cabinet_id` int(11) DEFAULT NULL COMMENT '机柜ID',
  `op` varchar(24) DEFAULT NULL COMMENT '运维负责人',
  `phone` varchar(11) DEFAULT NULL COMMENT '联系电话',
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='服务器表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT '用户名',
  `name_cn` varchar(50) NOT NULL COMMENT '中文名',
  `password` varchar(50) NOT NULL COMMENT '用户密码',
  `email` varchar(50) DEFAULT NULL COMMENT '电子邮件',
  `mobile` varchar(11) NOT NULL COMMENT '手机号码',
  `role` varchar(10) NOT NULL COMMENT '1:sa;2:php;3:ios;4:test',
  `status` tinyint(4) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `last_time` datetime DEFAULT NULL COMMENT '最后登录时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8 COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (16,'admin','admin','94b5d4cd072ec6ab3ed1da66aa3bca70','123456','1234455667','admin',0,NULL,'2016-08-18 18:00:53'),(58,'55','55','www.123','55','5566','admin',0,NULL,NULL),(59,'ouyang','欧阳','www.123','1445675350@qq.com','11111111111','user',0,NULL,NULL),(60,'66','66','666','66677','66677','admin',0,NULL,NULL),(61,'fujinzhou','fujinzhou','111','111','111','admin',0,NULL,NULL),(64,'fujinzhou1','周福金','www.123','1445675350@qq.com','13651602471','admin',0,NULL,NULL),(66,'fujinzhou22','周福金','www.123','1445675350@qq.com','13651602471','admin',0,NULL,NULL),(68,'fujinzhou2222','周福金','www.123','1445675350@qq.com','13651602471','admin',0,NULL,NULL),(70,'panda','刘子平','1234','1445675350@qq.com','13651602471','user',0,NULL,NULL),(71,'yangke','杨科1','97e359a9c42a24fbb408cfadea15568c','1445675350@qq.com','13651602471','user',0,NULL,NULL),(72,'2222','二二二','97e359a9c42a24fbb408cfadea15568c','1445675350@qq.com','13651602471','user',0,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-08 15:48:03
