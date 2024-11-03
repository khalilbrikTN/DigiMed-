use yasminamahdy_digimed;

DROP TABLE IF EXISTS `org`;

CREATE TABLE `org` (
  `OrgNo` int NOT NULL,
  `OrgName` varchar(150) NOT NULL,
  `OpeningDetails` varchar(300) NOT NULL,
  `Notes` varchar(500) NOT NULL,
  PRIMARY KEY (`OrgNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
