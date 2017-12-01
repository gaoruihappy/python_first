#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
def getLastData():

  db=pymysql.connect("localhost","gaorui_weather","123456","weather",charset="utf8")

   
  # 使用cursor()方法获取操作游标 
  cursor = db.cursor()
   
  # SQL 查询语句
  sql = "SELECT * FROM weather_list \
         WHERE id > '%d'" % (304)
  try:
    cursor.execute(sql)
    results = cursor.fetchall()
  except OSError as err:
    print("OS error: {0}".format(err))
   
  # 关闭数据库连接
  finally:
    db.close()
  return results