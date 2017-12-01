import pymysql
from ConnectSQL import *
def mysql_insert(location, time, temperature, cond, wind_dir, wind_spd):
     try:
             ExecNonQuery('insert into weather_list values(%s,%d,%d,%s,%d,%d)' % (location, time, temperature, cond, wind_dir, wind_spd))
     except:
             return 0
mysql_insert('北京5', 151, 20, 'xx', 1,3)