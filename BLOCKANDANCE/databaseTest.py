import mysql.connector
# from _mysql_connector import Error

conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
if conn.is_connected():
    db_info = conn.get_server_version
    print('Connected to MySQL Server version', db_info)

