import mig_util2 as mu

connection = mu.get_oracle_conn()

with connection:

   cursor = connection.cursor()
#--------------------------------------------------------- Employee

   sql_employee = '''select employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id
           from Employees'''

   cursor.execute(sql_employee)
   employee = cursor.fetchall()

#--------------------------------------------------------- Department

   sql_department = '''select department_id, department_name, manager_id from Departments'''
   cursor.execute(sql_department)
   department = cursor.fetchall()

# -------------------------------------------------------- Job
   sql_job = '''select job_id, job_title, min_salary, max_salary from Jobs'''
   cursor.execute(sql_job)
   job = cursor.fetchall()



# --------------------------------connection 'dadb'
conn_dadb = mu.get_mysql_conn('dadb')
with conn_dadb:
   cur = conn_dadb.cursor()

#--------------------------------------------------------- Employee
   cur.execute("drop table if exists Employee")
   employee_create = '''create table Employee(
                   id int unsigned not null auto_increment primary key,
                   first_name varchar(20),
                   last_name varchar(25) not null ,
                   email varchar(25) not null,
                   phone_number varchar(20),
                   hire_date date not null,
                   job_id varchar(10) not null,
                   salary int unsigned,
                   commission_pct decimal(3, 2),
                   manager_id int unsigned,
                   department_id smallint(4)
                   )'''
   cur.execute(employee_create)
   employee_insert = '''insert into Employee(id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id)
                   values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
   cur.executemany(employee_insert, employee)
   print("AffectedRows-->", cur.rowcount)
#--------------------------------------------------------- Department
   cur.execute("drop table if exists Department")
   department_create = '''create table Department(
                   id smallint(4) not null auto_increment primary key,
                   department_name varchar(30) not null,
                   manager_id int unsigned
                   )'''

   cur.execute(department_create)
   department_insert = '''insert into Department(id, department_name, manager_id)
                   values(%s, %s, %s)'''
   cur.executemany(department_insert, department)
   print("AffectedRows-->", cur.rowcount)
# -------------------------------------------------------- Job
   cur.execute("drop table if exists Job")
   job_create = '''create table Job(
                   id varchar(10) not null primary key,
                   job_title varchar(35) not null,
                   min_salary int unsigned,
                   max_salary int unsigned
                   );'''

   cur.execute(job_create)
   job_insert = '''insert into Job(id, job_title, min_salary, max_salary)
                   values(%s, %s, %s, %s)'''
   cur.executemany(job_insert, job)



   print("AffectedRows-->", cur.rowcount)


   conn_dadb.commit()