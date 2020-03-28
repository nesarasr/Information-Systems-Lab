create database abc_db;
use abc_db;
select database();
show tables;

CREATE TABLE `department` (
  `did` int(11) NOT NULL,
  `dname` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `employee` (
  `eid` int(11) NOT NULL,
  `ename` varchar(45) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `joindate` date DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `DEPARTMENT_did` int(11) NOT NULL,
  PRIMARY KEY (`eid`),
  KEY `fk_EMPLOYEE_DEPARTMENT_idx` (`DEPARTMENT_did`),
  CONSTRAINT `fk_EMPLOYEE_DEPARTMENT` FOREIGN KEY (`DEPARTMENT_did`) REFERENCES `department` (`did`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `project` (
  `pid` int(11) NOT NULL,
  `pname` varchar(45) DEFAULT NULL,
  `startdate` date DEFAULT NULL,
  `deadline` int(11) DEFAULT NULL,
  `DEPARTMENT_did` int(11) NOT NULL,
  PRIMARY KEY (`pid`),
  KEY `fk_PROJECT_DEPARTMENT1_idx` (`DEPARTMENT_did`),
  CONSTRAINT `fk_PROJECT_DEPARTMENT1` FOREIGN KEY (`DEPARTMENT_did`) REFERENCES `department` (`did`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `employee_has_project` (
  `EMPLOYEE_eid` int(11) NOT NULL,
  `PROJECT_pid` int(11) NOT NULL,
  `workhour` int(11) DEFAULT NULL,
  PRIMARY KEY (`EMPLOYEE_eid`,`PROJECT_pid`),
  KEY `fk_EMPLOYEE_has_PROJECT_PROJECT1_idx` (`PROJECT_pid`),
  KEY `fk_EMPLOYEE_has_PROJECT_EMPLOYEE1_idx` (`EMPLOYEE_eid`),
  CONSTRAINT `fk_EMPLOYEE_has_PROJECT_EMPLOYEE1` FOREIGN KEY (`EMPLOYEE_eid`) REFERENCES `employee` (`eid`),
  CONSTRAINT `fk_EMPLOYEE_has_PROJECT_PROJECT1` FOREIGN KEY (`PROJECT_pid`) REFERENCES `project` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `abc_db`.`department`
(`did`,
`dname`,
`location`)
VALUES
(101,
'Production',
'Gurgaon');

INSERT INTO `abc_db`.`department`
(`did`,
`dname`,
`location`)
VALUES
(201,
'Assembly',
'Noida');

INSERT INTO `abc_db`.`department`
(`did`,
`dname`,
`location`)
VALUES
(301,
'Marketing',
'Delhi');

select * from department;


INSERT INTO `abc_db`.`employee`
(`eid`,
`ename`,
`sex`,
`dob`,
`joindate`,
`salary`,
`DEPARTMENT_did`)
VALUES
(1101,
'Ram Yadav',
'M',
'1988-04-12',
'2017-01-25',
19000,
101);

INSERT INTO employee VALUES (1102, 'Raghav P', 'M', '1985-06-10', '2017-11-05', 18000, 101);
INSERT INTO employee VALUES (1103, 'M Reddy', 'M', '1990-06-17', '2018-01-10', 15000, 101);
INSERT INTO employee VALUES (2101, 'Megha', 'F', '1989-08-10', '2017-07-01', 21000, 201);
INSERT INTO employee VALUES (2102, 'Karanvir', 'M', '1985-12-10', '2017-11-05', 20000, 201);
INSERT INTO employee VALUES (2103, 'Sundar S', 'M', '1991-02-15', '2018-06-15', 15000, 201);
INSERT INTO employee VALUES (3101, 'Rama P', 'F', '1985-06-10', '2017-02-05', 30000, 301);
INSERT INTO employee VALUES (3102, 'Radhika Bera', 'F', '1991-08-22', '2017-06-15', 27000, 301);

SELECT * FROM EMPLOYEE;

INSERT INTO PROJECT VALUES (1011, 'Special CMOS gate for BEL', '2017-01-01',36,101);
INSERT INTO PROJECT VALUES (1012, 'RAM for KINGSTON', '2017-06-01',36,101);
INSERT INTO PROJECT VALUES (2011, 'mother board for ASUS', '2017-01-01',24,201);
INSERT INTO PROJECT VALUES (2012, 'mother board for ACER', '2017-09-01',24,201);
INSERT INTO PROJECT VALUES (3011, 'target new assembly contract', '2018-06-01', 06, 301);



select * from Project;

INSERT INTO employee_has_project VALUES (1101, 1011, 4);
INSERT INTO employee_has_project VALUES (1101, 1012, 4);
INSERT INTO employee_has_project VALUES (1102, 1011, 6);
INSERT INTO employee_has_project VALUES (1102, 1012, 2);
INSERT INTO employee_has_project VALUES (1103, 1012, 8);

INSERT INTO employee_has_project VALUES (2101, 2011, 8);
INSERT INTO employee_has_project VALUES (2102, 2011, 2);
INSERT INTO employee_has_project VALUES (2102, 2012, 6);
INSERT INTO employee_has_project VALUES (2103, 2012, 8);

INSERT INTO employee_has_project VALUES (3101, 3011, 8);
INSERT INTO employee_has_project VALUES (3102, 3011, 8);

select * from employee;
select * from employee_has_project;
select ename from employee;
select * from employee where salary > 20000;
select * from employee where salary < 20000;
select * from employee where salary < 20000 and ename like 'R%';
select * from employee where ename like '% %';
select * from employee where sex = 'M';
select * from employee where joindate > '2018-01-01';

### Neseted query
select * from department;
select dname from department;
select did from department where dname = 'Production'; 
select * from employee where DEPARTMENT_did = 101;

describe employee;

select * from employee where DEPARTMENT_did = (select did from department where dname = 'Production');

select * from department;

select * from project;

select * from project where pname like 'mother board %';
select pid from project where pname like 'mother board %';

select * from employee_has_project;
select * from employee_has_project where PROJECT_pid in (2011, 2012);
select EMPLOYEE_eid from employee_has_project where PROJECT_pid in (2011, 2012);
select EMPLOYEE_eid from employee_has_project 
where PROJECT_pid in (select pid from project where pname like 'mother board %');

select * from employee where eid in (
select EMPLOYEE_eid from employee_has_project where PROJECT_pid in ( 
select pid from project where pname like 'mother board %'));

### join query
select * from employee , department
where employee.DEPARTMENT_did = department.did;

select * from employee e, department d
where e.DEPARTMENT_did = d.did;

select * from employee as e, department as d
where e.DEPARTMENT_did = d.did;

select e.ename, e.sex, e.dob, e.joindate, e.salary, d.dname 
from employee as e, department as d
where e.DEPARTMENT_did = d.did;

select e.ename, e.sex, e.dob, e.joindate, e.salary, d.dname 
from employee as e, department as d
where e.DEPARTMENT_did = d.did
and d.dname = 'Production';

select * from employee;
select * from employee_has_project;
select * from project;
select * from employee as e, employee_has_project as ep
where e.eid = ep.EMPLOYEE_eid;
select * from
employee_has_project as ep, project as p
where ep.PROJECT_pid = p.pid;
select * from
employee as e, employee_has_project as ep, project as p
where e.eid = ep.EMPLOYEE_eid and ep.PROJECT_pid = p.pid;
select e.ename, e.sex, e.dob, e.joindate, e.salary, p.pname from 
employee as e, employee_has_project as ep, project as p
where e.eid = ep.EMPLOYEE_eid and ep.PROJECT_pid = p.pid
and p.pname like 'mother board %';

########## Aggregation Query  ############
select max(salary) from employee;
select min(salary) from employee;

select * from employee where salary = (select max(salary) from employee);
select max(salary) from employee where salary < (select max(salary) from employee);
select * from employee where salary =
(select max(salary) from employee where salary < (select max(salary) from employee));

select avg(salary) from employee;

select avg(salary), DEPARTMENT_did from employee 
group by DEPARTMENT_did;

select avg(salary) as avg_sal, DEPARTMENT_did from employee 
group by DEPARTMENT_did
having avg_sal < 20000;

select avg(salary) as avg_sal, DEPARTMENT_did from employee 
group by DEPARTMENT_did
having avg_sal < 20000 
order by avg_sal desc;

select count(*) from employee where salary > (select avg(salary) from employee);
select * from employee where salary > (select avg(salary) from employee);

select * from employee where salary between 15000 and 20000;

######### join
select * from
employee as e join department as d
on e.DEPARTMENT_did = d.did;

insert into department values (401, 'NEW DEP', Null);

select * from department;

select * from
employee as e right join department as d
on e.DEPARTMENT_did = d.did;

select * from
department as d left join employee as e 
on d.did = e.DEPARTMENT_did ;

select * from department where location is null;






















create database test_db;
use test_db;
select database();

create table employee 
(eid int not null,
 ename varchar(45),
 primary key (eid));
 
 select * from employee;
 
 use sakila;
 select * from actor;
 select * from address;
 select * from city;
 
