#!/usr/bin/python3
 
import pymysql
import sys 
import time  
def writeDataBase(item):
	# 打开数据库连接
	db=pymysql.connect("localhost","gaorui_weather","123456","weather",charset="utf8")
	# 使用cursor()方法获取操作游标 
	cursor=db.cursor()

	# SQL 插入语句
	sql = "INSERT INTO weather_list(location, time, temperature, cond, wind_dir, wind_spd) VALUES (%(location)s, %(time)s, %(temperature)s, %(cond)s, %(wind_dir)s, %(wind_spd)s)"
	value = {
		'location':item['basic']['location'],
		'time':time.mktime(time.strptime(item['update']['loc'],"%Y-%m-%d %H:%M")),
		'temperature':item['now']['tmp'],
		'cond':item['now']['cond_txt'],
		'wind_spd':item['now']['wind_deg'],
		'wind_dir':item['now']['wind_spd']
	}
	#print(sql)
	try:
		# 执行sql语句
		cursor.execute(sql,value)
		# 提交到数据库执行
		db.commit()
	except OSError as err:
		print("OS error: {0}".format(err))
		# info=sys.exc_info()
		# 如果发生错误则回滚
		db.rollback()
	# 关闭数据库连接
	finally:
		db.close()
	