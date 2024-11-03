use yasminamahdy_digimed;

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `PatientNatID` char(14) NOT NULL,
  `PrescriptionID` int NOT NULL,
  `MedicineName` varchar(35) NOT NULL,
  `subscriptionHeading` char(2) DEFAULT NULL,
  `FormOfIntake` varchar(25) DEFAULT NULL,
  `DurationOfIntake` int DEFAULT NULL,
  `FrequencyOfIntake` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`PatientNatID`,`PrescriptionID`,`MedicineName`),
  CONSTRAINT `medicine_ibfk_1` FOREIGN KEY (`PatientNatID`, `PrescriptionID`) REFERENCES `presriptions` (`PatientNatID`, `PrescriptionID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
