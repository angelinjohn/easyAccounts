-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_user`
--

DROP TABLE IF EXISTS `tbl_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_user` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_email` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `state` bigint(20) DEFAULT NULL,
  `City` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `SSN` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user`
--

LOCK TABLES `tbl_user` WRITE;
/*!40000 ALTER TABLE `tbl_user` DISABLE KEYS */;
INSERT INTO `tbl_user` VALUES (1,'Angelin','angelin@gmail.com','pbkdf2:sha256:50000$fNeyUrtU$63039bf68d26d8bbc0382e958c0b1aa11f9c63dd7cfcc5509ed27a74a48e74be',NULL,NULL,NULL),(2,'kevin demo','demo1@easyacc.com','pbkdf2:sha256:50000$RtAfMGmN$cb4ea689e037880e7e78e7861131a9cc963450b173c57d2609c6ab1611f86cda',NULL,NULL,NULL),(3,'angelin john','angelinjohn1234@1234.com','pbkdf2:sha256:50000$E0FK2xVH$24bef490d68b4cb6138359b1ca63e27034ab56e8a7e777b1080e6244aefe7a08',NULL,NULL,NULL),(4,'angelin john','angelinjohn1234@1234.com','pbkdf2:sha256:50000$Dc0hlkxK$6235d5ffc9b649f9274e197f556ac5a0fdf964cf1ae81e9937d5025848d6e471',NULL,NULL,NULL),(5,'varsha vijayan','varsha@gmail.com','pbkdf2:sha256:50000$5lyPFkEp$9d4f30401dda1601a94ddff22840f712aae0e68624c7d20ed40b8ae365d47936',1,'Phoenix',453267897),(6,'varsha','varshaheiudoi@gmail.com','pbkdf2:sha256:50000$j7TZPg8U$e742d4c5fdda7c29053842d1fe3ffe2d85d08a9e43bfc7c55a871d77c6e5a55b',NULL,NULL,NULL),(7,'v a','v','pbkdf2:sha256:50000$5NbcFxRU$c518d74b09888c743b90ad6c3ed57b4f3cdfd8ea6ab8483c30864a4d583539a9',NULL,NULL,NULL),(8,'ange','ange','pbkdf2:sha256:150000$grApglfe$c7dc766b0041003c241c38fe1ff5f6dd12b140353a39c5ebbaadfda9b1fde476',1,'Phoenix',343565221),(9,'jane doe','jdoe@test.com','pbkdf2:sha256:150000$Ac96Sa4m$f385ceb1d9e69aba6ac635e8db828f7aace67bfeef161183f54ac36bece42993',NULL,NULL,NULL),(10,'test user','t123@123.com','pbkdf2:sha256:150000$FhohLxRX$638a35288147fa7567c311fa3f2c514ddf1295302ec03230970495a7e4a10d29',NULL,NULL,NULL),(11,'test user','t123@123.com','pbkdf2:sha256:150000$fX5isOzr$b3f78b53b954d8971fbe72ce35ddb54dc3a0034714620db74e11916bbf7461f2',NULL,NULL,NULL),(12,'te tes','tes@123.com','pbkdf2:sha256:150000$uQnVr4B8$5d7f69f9b3bae496df5096ba455b08e5977cc0cd93e7a2698044333c516aa26d',NULL,NULL,NULL),(13,'test uii','iuio','pbkdf2:sha256:150000$0VYRfsVB$8f2d9690b466e66579f2740f3bdd44c5021ee4bd0d310a80480563cf4aa3a7b2',NULL,NULL,NULL),(14,'test uii','iuio','pbkdf2:sha256:150000$DhEIxR0O$43396e7a15ceac14f34e4f3f81e9c28f874d4cbf5aeb078681cc98c3acab865c',NULL,NULL,NULL),(15,'shds kjkj','kjjk','pbkdf2:sha256:150000$V6qmiac0$006bb4cccb5c4b99fb8f4ac72293d846aea492442a3c849cdaa8ed7d512f2b44',NULL,NULL,NULL),(16,'shds kjkj','jdhkjsjk','pbkdf2:sha256:150000$WVudc41l$cdd9f3587c06559f0280495b8b0969be7dac6b33b7f562fb2e54ee0e112e561c',NULL,NULL,NULL),(17,'shds kjkj','jdhkjsjk','pbkdf2:sha256:150000$xgWJsQhu$935bab8fd3eeff2f0bc6fe4e7376133d58474207da24726276a606e43297a30b',NULL,NULL,NULL),(18,'fskjh jhkj','kjhkjh','pbkdf2:sha256:150000$IAusMWEJ$c4422b1905124d41aa79d2e62f50e5e1b41b5f640eff9d4d2f3c75e2a66cd521',NULL,NULL,NULL),(19,'test gyd','yuiu','pbkdf2:sha256:150000$EsfJ385P$c0cf1508ece16c94a3854ed76fb69a9fca8768dc32b9fa8679afd75b99d2df24',NULL,NULL,NULL),(20,'test gyd','yuiu','pbkdf2:sha256:150000$lD0GfSjZ$d7e74f85040d6cc0eabc857b26453fa51d782672c34b4409fe47ff630469b87f',NULL,NULL,NULL),(21,'dgqyh hiuh','hhui','pbkdf2:sha256:150000$gDYtO4uM$3b9fa5e2b524545afe51bd9ce7cb4a83c5d2225640041b495b0c695664f8234a',NULL,NULL,NULL),(22,'dgqyh hiuh','hhui','pbkdf2:sha256:150000$0ojujHFi$0427fa1c20faddfb561c2de19c450d2b919b364d1cf0b474faad4df22eaa8c01',NULL,NULL,NULL),(23,'dgqyh hiuh','hhui','pbkdf2:sha256:150000$ciecLdNP$12fcf346669c3703daae237fb84595f7ca01b7af422433ae0d545d01d621416a',NULL,NULL,NULL),(24,'dgqyh hiuh','hhui','pbkdf2:sha256:150000$RBVJT9XI$07423ccbc534f756252183333bdc8813aa19a78350d3705259565a1a5d1c274e',NULL,NULL,NULL),(25,'hdwhswu` hjh','hjhjkh','pbkdf2:sha256:150000$dkLzn9Qe$272375666a8531ad3ba3b6b87325d32e3c0146e63eef85ec2f8337c3a56cc0e8',NULL,NULL,NULL),(26,'hdwhswu` hjh','hjhjkh','pbkdf2:sha256:150000$HutAdXxv$6d7b7efd27db3e64e236ca8ee383932a88e7cb12cf8c2f69b58de26505d30cee',NULL,NULL,NULL),(27,'hey hery','hty','pbkdf2:sha256:150000$RtfVB04B$17cd5843404ce0140b41b08d10e845a276ef66e2dea3ef26ced8edc617521000',NULL,NULL,NULL),(28,'sdf sdf','def','pbkdf2:sha256:150000$ACFl8oLS$e780c1206181abae55e234a9a25fbd457f8a31f64f5b10bdc9927edff2dd9e8c',NULL,NULL,NULL),(29,'y u','uyiu','pbkdf2:sha256:150000$EzhO9fO4$5a8783aaa8000d5208aac865e2ed4f7d57236c64c784dc8bbb4bd71bae07e6b9',NULL,NULL,NULL);
/*!40000 ALTER TABLE `tbl_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-28 23:21:17
