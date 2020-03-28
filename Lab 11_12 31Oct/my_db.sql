use abc_db;
select database();
show tables;
select * from department;
select * from employee;
select * from project;
select * from employee_has_project;
select * from employee where DEPARTMENT_DID in (select DID from department where DNAME='Production');
select EID,ENAME from employee where SALARY>20000;
select DID from department where DNAME='Production';
select * from employee_has_project where PROJECT_PID in (2011,2012,3011);
select EMPLOYEE_EID from employee_has_project where PROJECT_PID in (select PID from project where PNAME like '%mother%');
create table student(
roll int,
name varchar(25));

select * from student;

select pname from project where DEPARTMENT_DID in (select DID from department where LOCATION='Noida');
select distinct(project.pname), sum(employee.SALARY) from project 
             join employee on employee.DEPARTMENT_DID = project.DEPARTMENT_DID where employee.GENDER='F'group by project.pname;
select * from employee join employee_has_projects on employee.EID=employee_has_projects.EMPLOYEE_EID;
