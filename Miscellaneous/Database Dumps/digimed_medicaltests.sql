use yasminamahdy_digimed;

DROP TABLE IF EXISTS `medicaltests`;
CREATE TABLE `medicaltests` (
  `PatientNatID` char(14) NOT NULL,
  `TestID` int NOT NULL,
  `Test_Type` varchar(15) DEFAULT NULL,
  `SubjectOfTest` varchar(50) DEFAULT NULL,
  `Result` varchar(100) DEFAULT NULL,
  `ImageOfScan` varchar(50) DEFAULT NULL,
  `Date_TimeOfUpload` datetime DEFAULT NULL,
  PRIMARY KEY (`PatientNatID`,`TestID`),
  CONSTRAINT `medicaltests_ibfk_1` FOREIGN KEY (`PatientNatID`) REFERENCES `patient` (`NatID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
