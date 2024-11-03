use yasminamahdy_digimed;

DROP TABLE IF EXISTS `treatedby`;

CREATE TABLE `treatedby` (
  `PatientNatID` char(14) NOT NULL,
  `DoctorNatID` char(14) NOT NULL,
  `startDate` date DEFAULT NULL,
  PRIMARY KEY (`PatientNatID`,`DoctorNatID`),
  KEY `DoctorNatID` (`DoctorNatID`),
  CONSTRAINT `treatedby_ibfk_1` FOREIGN KEY (`PatientNatID`) REFERENCES `patient` (`NatID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `treatedby_ibfk_2` FOREIGN KEY (`DoctorNatID`) REFERENCES `doctor` (`NatID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

