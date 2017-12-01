CREATE TABLE weather_list(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `location` VARCHAR(16) NOT NULL,
   `time` INT UNSIGNED NOT NULL,
   `temperature` TINYINT NOT NULL,
   `cond` VARCHAR(16) NOT NULL,
   `wind_dir` SMALLINT NOT NULL,
   `wind_spd` TINYINT NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;