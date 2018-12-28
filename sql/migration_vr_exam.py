import mysql_migration as mm

# -------------검증 1번-------------------
conn_dooodb = mm.get_mysql_conn('dooodb')
with conn_dooodb:
    dooo_cnt_emp = mm.get_count(conn_dooodb, 'Employee')
    dooo_cnt_dept = mm.get_count(conn_dooodb, 'Department')
    dooo_cnt_job = mm.get_count(conn_dooodb, 'Job')
    dooo_cnt_jobhis = mm.get_count(conn_dooodb, 'Job_history')

connection = mm.get_oracle_conn()
with connection:
    ora_cnt_emp = mm.get_count(connection, 'Employees')
    ora_cnt_dept = mm.get_count(connection, 'Departments')
    ora_cnt_job = mm.get_count(connection, 'Jobs')
    ora_cnt_jobhis = mm.get_count(connection, 'Job_history')
# ------------------함수화 질문---------------------------------
# ---------------------Dooo, dadb 이름 바꾸기 -------------------
if  dooo_cnt_emp != ora_cnt_emp:
    print("========================Employee Failed==================================")
    exit()

else:
    print("OK", "Dooo-->" , dooo_cnt_emp, "Oracle--->", ora_cnt_emp)
    
    connection = mm.get_oracle_conn()
    with connection:
        curs = connection.cursor()
        rand = '''select * from (
                select  employee_id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id 
                from Employees order by DBMS_RANDOM.RANDOM)
                where rownum <= 5 '''
        curs.execute(rand)
        rand_oracle_employee = curs.fetchall()
        a = []
        for i in range(0,5):
            a.append(rand_oracle_employee[i][0])



    conn_dooodb = mm.get_mysql_conn('dooodb')
    with conn_dooodb:
        cur = conn_dooodb.cursor()
        vr = '''select 
                id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id
                from Employee where id = %s'''
        vr_dooodb = []
        for i in a:
            (cur.execute(vr, i))
            vr_dooodb.append(cur.fetchone())
            
        if rand_oracle_employee == list(vr_dooodb):
            print("-Oo----------------------------------------------====OK")



if dooo_cnt_dept != ora_cnt_dept:
    print("========================Department Failed==================================")
    exit()

else:
    print("OK", "Dooo-->" , dooo_cnt_dept, "Oracle--->", ora_cnt_dept)
    connection = mm.get_oracle_conn()
    with connection:
        curs = connection.cursor()
        rand = '''select * from (
            select department_id, department_name, manager_id
                from Departments order by DBMS_RANDOM.RANDOM)
                where rownum <= 5 '''
        curs.execute(rand)
        rand_oracle_department = curs.fetchall()
        a = []
        for i in range(0,5):
            a.append(rand_oracle_department[i][0])



    conn_dooodb = mm.get_mysql_conn('dooodb')
    with conn_dooodb:
        cur = conn_dooodb.cursor()
        vr = '''select 
                id, department_name, manager_id
                from Department where id = %s'''
        vr_dooodb = []
        for i in a:
            (cur.execute(vr, i))
            vr_dooodb.append(cur.fetchone())
            
        if rand_oracle_department == list(vr_dooodb):
            print("-Oo----------------------------------------------====OK")





if dooo_cnt_job != ora_cnt_job:
    print("========================Job Failed==================================")
    exit()
else:
    print("OK", "Dooo-->" , dooo_cnt_job, "Oracle--->", ora_cnt_job)
    connection = mm.get_oracle_conn()
    with connection:
        curs = connection.cursor()
        rand = '''select * from (
            select job_id, job_title, min_salary, max_salary from jobs order by DBMS_RANDOM.RANDOM)
                where rownum <= 5  '''
        curs.execute(rand)
        rand_oracle_job = curs.fetchall()
        a = []
        for i in range(0,5):
            a.append(rand_oracle_job[i][0])



    conn_dooodb = mm.get_mysql_conn('dooodb')
    with conn_dooodb:
        cur = conn_dooodb.cursor()
        vr = '''select 
                id, job_title, min_salary, max_salary
                from Job where id = %s'''
        vr_dooodb = []
        for i in a:
            (cur.execute(vr, i))
            vr_dooodb.append(cur.fetchone())
            
        if rand_oracle_job == list(vr_dooodb):
            print("-Oo----------------------------------------------====OK")







if dooo_cnt_jobhis != ora_cnt_jobhis:
    print("========================Job_history Failed==================================")
    exit()
else:
    print("OK", "Dooo-->" , dooo_cnt_jobhis, "Oracle--->", ora_cnt_jobhis)
    connection = mm.get_oracle_conn()
    with connection:
        curs = connection.cursor()
        rand = '''select * from (select 
            employee_id, start_date, end_date, job_id, department_id from job_history order by DBMS_RANDOM.RANDOM)
                where rownum <= 5  '''
        curs.execute(rand)
        rand_oracle_jobhis = curs.fetchall()
        a = []
        for i in range(0,5):
            a.append(rand_oracle_jobhis[i][0])



    conn_dooodb = mm.get_mysql_conn('dooodb')
    with conn_dooodb:
        cur = conn_dooodb.cursor()
        vr = '''select 
                employee_id, start_date, end_date, job_id, department_id
                from Job_history where employee_id = %s'''
        vr_dooodb = []
        for i in a:
            (cur.execute(vr, i))
            vr_dooodb.append(cur.fetchone())
            
        if rand_oracle_jobhis == list(vr_dooodb):
            print("-Oo----------------------------------------------====OK")










# # -------------------------검증 2번-------------------------------
# connection = mm.get_oracle_conn()
# with connection:
#     curs = connection.cursor()
#     rand = '''select * from (
#             select  employee_id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id 
#             from Employees order by DBMS_RANDOM.RANDOM)
#             where rownum <= 5 '''
#     curs.execute(rand)
#     rand_oracle_employee = curs.fetchall()



# a = []
# for i in range(0,5):
#     a.append(rand_oracle_employee[i][0])



# conn_dooodb = mm.get_mysql_conn('dooodb')
# with conn_dooodb:
#     cur = conn_dooodb.cursor()
#     vr = '''select 
#               id, first_name, last_name, email, phone_number, hire_date, job_id, round(salary), round(commission_pct * 100), manager_id, department_id
#             from Employee where id = %s'''
#     vr_dooodb = []
#     for i in a:
#         (cur.execute(vr, i))
#         vr_dooodb.append(cur.fetchone())
        

# if rand_oracle_employee == list(vr_dooodb):
#     print("-Oo----------------------------------------------====OK")



