use yasminamahdy_digimed;

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `NatID` char(14) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `MiddleName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) NOT NULL,
  `Street` varchar(250) DEFAULT NULL,
  `Region` varchar(250) DEFAULT NULL,
  `City` varchar(250) DEFAULT NULL,
  `PhoneNumber` varchar(17) DEFAULT NULL,
  `Email` varchar(150) DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `BloodType` varchar(3) DEFAULT NULL,
  `Height` decimal(4,1) DEFAULT NULL,
  `Weight` decimal(4,1) DEFAULT NULL,
  PRIMARY KEY (`NatID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

