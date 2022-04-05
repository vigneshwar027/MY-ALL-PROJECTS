import pyodbc
import pandas as pd
#
df = pd.read_excel('E:\DJANGOPROJECTS\JK SOFT\chinju.xls')

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-G7RMCQ9\SQLEXPRESS;DATABASE=practice;Trusted_Connection=yes;')

# cursor=connection.cursor()
# cursor.execute("SELECT @@VERSION as version")
#
# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print(row.version)
#
# cursor.close()
# connection.close()
# print('over')


# import pyodbc as py

# print(py.drivers())
df = pd.read_excel('E:\DJANGOPROJECTS\JK SOFT\chinju.xls')
print(df)
#

# connection = create_engine('mysql://root:root@localhost/practicedb')

df.to_sql('new', connection)
print('data uploaded')


# except:
#     # print('connection not made')
#
# print(Drivers)

# connection = py.connect(
#     'driver={SQL Server};'
#     'server = DESKTOP-G7RMCQ9\SQLEXPRESS;'
#     'database = practice;'
#     'trusted_Connection = yes;'
# )

# ['SQL Server', 'SQL Server Native Client 11.0', 'ODBC Driver 17 for SQL Server',
# 'SQL Server Native Client RDA 11.0',
# 'MySQL ODBC 8.0 ANSI Driver', 'MySQL ODBC 8.0 Unicode Driver']
# data uploaded