use yasminamahdy_digimed;

DROP TABLE IF EXISTS `appointments`;

CREATE TABLE `appointments` (
  `DocNatID` char(14) NOT NULL,
  `AppID` int NOT NULL,
  `OrgNum` int DEFAULT NULL,
  `AppDateTime` datetime DEFAULT NULL,
  `PatientNatID` char(14) DEFAULT NULL,
  PRIMARY KEY (`DocNatID`,`AppID`),
  KEY `OrgNum` (`OrgNum`),
  KEY `PatientNatID` (`PatientNatID`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`DocNatID`) REFERENCES `doctor` (`NatID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`OrgNum`) REFERENCES `org` (`OrgNo`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `appointments_ibfk_3` FOREIGN KEY (`PatientNatID`) REFERENCES `patient` (`NatID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

