#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db=pymysql.connect("localhost","gaorui_weather","123456","weather",charset="utf8")


# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM weather_list WHERE wind_dir > '%d'" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭连接
db.close()