import pymysql
import sys   

# 打开数据库连接

def ExecNonQuery(sql):
	db = pymysql.connect("localhost","gaorui_weather","123456","weather",charset="utf8")
	cursor=db.cursor()
	try:
		# 执行sql语句
		print(1)
		cursor.execute(sql)
		# 提交到数据库执行
		print(2)
		db.commit()
		print(3)
	except:
		info=sys.exc_info()
		print(info)
		print(4)
		# 如果发生错误则回滚
		db.rollback()
	# 关闭数据库连接
	db.close()