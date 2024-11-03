use yasminamahdy_digimed;

DROP TABLE IF EXISTS `orglocation`;

CREATE TABLE `orglocation` (
  `OrgNo` int NOT NULL,
  `Location` varchar(250) NOT NULL,
  PRIMARY KEY (`OrgNo`,`Location`),
  CONSTRAINT `orglocation_ibfk_1` FOREIGN KEY (`OrgNo`) REFERENCES `org` (`OrgNo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

