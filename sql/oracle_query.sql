
desc Employee;
desc Department;
desc Job;
desc Job_history;

insert into Employee (id, first_name, last_name, email, 
					  phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) 
					  values() ;

insert into Department (id, department_name, manager_id) values() ;

insert into Job (id, job_title, min_salary, max_salary) values ();

insert into Job_history (id, start_date, end_date, job_id, department_id) values ();