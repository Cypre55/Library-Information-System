/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ lis /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE lis;

DROP TABLE IF EXISTS BOOKS;
CREATE TABLE `BOOKS` (
  `UniqueID` int NOT NULL AUTO_INCREMENT,
  `ISBN` varchar(255) DEFAULT NULL,
  `BookName` varchar(255) DEFAULT NULL,
  `RackNumber` int DEFAULT NULL,
  `LastIssued` date DEFAULT NULL,
  `IsDisposed` int DEFAULT NULL,
  PRIMARY KEY (`UniqueID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS MEMBERS;
CREATE TABLE `MEMBERS` (
  `MemberID` varchar(255) NOT NULL,
  `MemberName` varchar(255) DEFAULT NULL,
  `MemberType` varchar(255) DEFAULT NULL,
  `ListOfBooksIssued` varchar(1000) DEFAULT NULL,
  `ReservedBook` varchar(255) DEFAULT NULL,
  `GotReminder` int DEFAULT NULL,
  `PassWd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MemberID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS RESERVATIONS;
CREATE TABLE `RESERVATIONS` (
  `ISBN` varchar(255) NOT NULL,
  `AvailableUIDs` varchar(1000) DEFAULT NULL,
  `TakenUIDs` varchar(1000) DEFAULT NULL,
  `PendingReservations` varchar(1000) DEFAULT NULL,
  `ActiveReservations` varchar(1000) DEFAULT NULL,
  `ActiveReservedUIDs` varchar(1000) DEFAULT NULL,
  `NumberOfCopiesAvailable` int DEFAULT NULL,
  PRIMARY KEY (`ISBN`),
  UNIQUE KEY `ISBN` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `EMPLOYEES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMPLOYEES` (
  `EmployeeID` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `EmployeeName` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `PassWd` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;










/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;