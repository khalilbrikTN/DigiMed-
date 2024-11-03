use yasminamahdy_digimed;

DROP TABLE IF EXISTS `presriptions`;

CREATE TABLE `presriptions` (
  `PatientNatID` char(14) NOT NULL,
  `PrescriptionID` int NOT NULL,
  `DocNatID` char(14) DEFAULT NULL,
  `DateOfPrescription` date DEFAULT NULL,
  PRIMARY KEY (`PatientNatID`,`PrescriptionID`),
  KEY `DocNatID` (`DocNatID`),
  CONSTRAINT `presriptions_ibfk_1` FOREIGN KEY (`PatientNatID`) REFERENCES `patient` (`NatID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `presriptions_ibfk_2` FOREIGN KEY (`DocNatID`) REFERENCES `doctor` (`NatID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

