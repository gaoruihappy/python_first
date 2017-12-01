#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","gaorui_weather","123456","weather")

 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS weather_list")
 
# 使用预处理语句创建表
sql = """CREATE TABLE weather_list (
	`id` INT UNSIGNED AUTO_INCREMENT,
	`location` VARCHAR(16) NOT NULL,
	`time` INT UNSIGNED NOT NULL,
	`temperature` TINYINT NOT NULL,
	`cond` VARCHAR(16) NOT NULL,
	`wind_dir` SMALLINT NOT NULL,
	`wind_spd` TINYINT NOT NULL,
	PRIMARY KEY ( `id` ))"""
 
cursor.execute(sql)
 
# 关闭数据库连接
db.close()