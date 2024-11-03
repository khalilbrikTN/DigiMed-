use yasminamahdy_digimed;

DROP TABLE IF EXISTS `referring`;

CREATE TABLE `referring` (
  `ReferringNatID` char(14) NOT NULL,
  `ReferredNatID` char(14) NOT NULL,
  `PatientNatID` char(14) NOT NULL,
  PRIMARY KEY (`ReferringNatID`,`ReferredNatID`,`PatientNatID`),
  KEY `ReferredNatID` (`ReferredNatID`),
  KEY `PatientNatID` (`PatientNatID`),
  CONSTRAINT `referring_ibfk_1` FOREIGN KEY (`ReferringNatID`) REFERENCES `doctor` (`NatID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `referring_ibfk_2` FOREIGN KEY (`ReferredNatID`) REFERENCES `doctor` (`NatID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `referring_ibfk_3` FOREIGN KEY (`PatientNatID`) REFERENCES `patient` (`NatID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

