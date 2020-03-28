from __future__ import print_function
from datetime import date, datetime, timedelta
import pymysql


connection = pymysql.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='abc_db',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
                              #use_pure=False)
cursor = connection.cursor()

############  part -- 1  ####
##
##query = ("SELECT eid, ename FROM employee ")
##cursor.execute(query)
##result = cursor.fetchall()
##print(result)
##print(type(result))
##for res in result:
##    print("{}, {} are record".format(res['eid'], res['ename']))

##############


##
############    part -- 2    #####
##add_student = ("INSERT INTO student "
##               "(roll, name) "
##               "VALUES (%s, %s)")
##data_student = ('1001', 'Sangita')
### Insert new student
##cursor.execute(add_student, data_student)
##connection.commit()   ##vv imp, needs to save the data
##print("Data Inserted")

##
##
###############  part --3 ####
##add_student = ("INSERT INTO student "
##               "(roll, name) "
##               "VALUES (%(roll)s, %(name)s)")
##data_student = {'roll':'1002', 'name':'Shyam'}
## Insert new student
##cursor.execute(add_student, data_student)
##connection.commit()
##print("Data Inserted")



###############  part -- 4 ####
##query2 = ("select ename, sex, dob, joindate, salary, dname "
##"from employee as e, department as d "
##"where e.DEPARTMENT_did = d.did "
##"and d.dname = %s and e.sex = %s")
##dname = 'Production'
##sex = 'M'
##cursor.execute(query2, (dname, sex))
##result = cursor.fetchall()
##
##for res in result:
##    print("{}, {} , {}, {}, {}, {}"\
##          .format(res['ename'], res['sex'], res['dob'], res['joindate'], \
##                  res['salary'], res['dname']))


#####################  part -- 5 #################
##
try:
    cursor.execute("select * from staff")
    result = cursor.fetchall()
    print(result)
except pymysql.Error as err:
    print(err)

cursor.close()
connection.close()



