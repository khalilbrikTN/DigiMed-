use yasminamahdy_digimed;

DROP TABLE IF EXISTS `worksin`;

CREATE TABLE `worksin` (
  `DocNatID` char(14) NOT NULL,
  `OrgNum` int NOT NULL,
  `ScheduleWorkingDays` varchar(15) DEFAULT NULL,
  `ScheduleWorkingHours` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`DocNatID`,`OrgNum`),
  KEY `OrgNum` (`OrgNum`),
  CONSTRAINT `worksin_ibfk_1` FOREIGN KEY (`DocNatID`) REFERENCES `doctor` (`NatID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `worksin_ibfk_2` FOREIGN KEY (`OrgNum`) REFERENCES `org` (`OrgNo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

