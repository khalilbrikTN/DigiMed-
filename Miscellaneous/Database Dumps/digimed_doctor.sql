use yasminamahdy_digimed;

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `NatID` char(14) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `MiddleName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) NOT NULL,
  `Specialty` varchar(250) DEFAULT NULL,
  `SubSpecialty` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`NatID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
