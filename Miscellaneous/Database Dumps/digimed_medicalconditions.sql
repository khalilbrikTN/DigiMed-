use yasminamahdy_digimed;

DROP TABLE IF EXISTS `medicalconditions`;

CREATE TABLE `medicalconditions` (
  `PatientNatID` char(14) NOT NULL,
  `MedCondition` char(14) NOT NULL,
  `Notes` varchar(500) NOT NULL,
  PRIMARY KEY (`PatientNatID`,`MedCondition`),
  CONSTRAINT `medicalconditions_ibfk_1` FOREIGN KEY (`PatientNatID`) REFERENCES `patient` (`NatID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
