CREATE TABLE `Student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL DEFAULT '0',
  `phone` varchar(45) NOT NULL DEFAULT '0',
  `birthday` date DEFAULT NULL,
  `email` varchar(45) NOT NULL DEFAULT '0',
  `address` varchar(3) NOT NULL DEFAULT '0',
  `gender` tinyint(4) NOT NULL DEFAULT '0',
  `dept` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_dept_dept_idx` (`dept`),
  CONSTRAINT `fk_dept_dept` FOREIGN KEY (`dept`) REFERENCES `Dept` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4073 DEFAULT CHARSET=utf8;

CREATE TABLE `Subject` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL DEFAULT '0',
  `prof` smallint(5) unsigned NOT NULL DEFAULT '0',
  `classroom` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `Subject_ibfk_1` (`prof`),
  CONSTRAINT `Subject_ibfk_1` FOREIGN KEY (`prof`) REFERENCES `Prof` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

CREATE TABLE `Prof` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  `likecnt` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

CREATE TABLE `Enroll` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` smallint(5) unsigned NOT NULL,
  `student` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_subject_subject` (`subject`),
  KEY `Enroll_ibfk_1` (`student`),
  CONSTRAINT `Enroll_ibfk_1` FOREIGN KEY (`student`) REFERENCES `Student` (`id`) ON DELETE NO ACTION,
  CONSTRAINT `Enroll_ibfk_2` FOREIGN KEY (`subject`) REFERENCES `Subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3651 DEFAULT CHARSET=utf8;

