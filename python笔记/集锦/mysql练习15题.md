1、查询“生物”课程比“物理”课程成绩高的所有学生的学号；

select * from( 

 (select * from score where course_id in (select cid from course where cname = '生物')) t1  

left join 

 (select * from score where course_id in (select cid from course where cname = '物理')) t2  

on  t1.student_id = t2.student_id) 

where t1.num > t2.num;

 

2、查询平均成绩大于60分的同学的学号和平均成绩;

\# 先查看每个同学的平均分数

select student_id,avg(num) from score group by student_id;

\# 在筛选成绩大于60分的同学的学号和平均成绩；

\# select student_id,avg(num) from score group by student_id having avg(num) > 60;

 

3、查询所有同学的学号、姓名、选课数、总成绩；

\# 先查看每个同学的总成绩

select student_id,sum(num) from score group by student_id;

\# 学生和课程的关系只有成绩表中存在，因此要获取每个学生选择的课程，需要通过score表

select count(sid),student_id from score group by student_id;

\# 将上面两步合并

select sum(num),count(sid),student_id from score group by student_id;

\# 将学生的信息和成绩选课情况拼在一起

select sid,sname,sum_num ,count_stu 

from student  

left join 

 (select sum(num) sum_num,count(sid) count_stu,student_id from score group by student_id) t2  

on  sid = student_id;

\# 还可以更严谨，那些没有选课的同学选课数和总成绩应该是0

select sid,sname,

 (

​           CASE

​           WHEN sum_num is  null THEN 0   

   ELSE sum_num

​           END

​         ) as sum_num ,

 (

​           CASE

​           WHEN count_stu is  null THEN 0   

   ELSE count_stu

​           END

​         ) as count_stu 

from student  

left join 

 (select sum(num) sum_num,count(sid) count_stu,student_id from score group by student_id) t2  

on  sid = student_id;

 

4、查询姓“李”的老师的个数；

\# 找到所有姓李的

 \# 方法一

 \# select * from teacher where tname like '李%';

 \# 方法二

 \# select * from teacher where tname regexp '^李';

\# 统计个数

 select count(tid) from teacher where tname regexp '^李';

 或者

 select count(id) from teacher where tname like '李%';

 

5、查询没学过“张磊老师”课的同学的学号、姓名；

\# 找到张磊老师的id 

select tid from teacher where tname == '张磊老师';

\# 找到张磊老师所教课程

select cid from course where teacher_id = (select tid from teacher where tname = '张磊老师');

\# 找到所有学习这门课的学生id

select student_id from score where course_id = (select cid from course where teacher_id = (select tid from teacher where tname = '张磊老师'));

\# 找到没有学过这门课的学生对应的学生学号、姓名

select sid,sname from student where sid not in 

 (select student_id from score where course_id = (select cid from course where teacher_id = (select tid from teacher where tname = '张磊老师'))

);

 

6、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；

\# 先查询学习课程id为1的所有学生

select * from score where course_id = 1;

\# 先查询学习课程id为2的所有学生

select * from score where course_id = 2;

\# 把这两张表按照学生的id 内连接起来 去掉只学习某一门课程的学生

select t1.student_id from

(select student_id from score where course_id = 1)  t1

inner join

(select student_id from score where course_id = 2) t2

on t1.student_id = t2.student_id

\# 根据学号在学生表中找到对应的姓名

select sid,sname from student where sid in (select t1.student_id from (select student_id from score where course_id = 1)  t1 inner join (select student_id from score where course_id = 2) t2 on t1.student_id = t2.student_id);

 

7、查询学过“李平老师”所教的所有课的同学的学号、姓名；

\#找到李平老师的tid

select tid from teacher where tname ='李平老师';

\# 找到李平老师教的所有课程cid

 select cid from course where teacher_id in (select tid from teacher where tname ='李平老师');

\# 找到李平老师教的所有课程数

 select count(cid) from course where teacher_id in (select tid from teacher where tname ='李平老师');

\# 找到所有学习李平老师课程的学生

select * from score where course_id in ( select cid from course where teacher_id in (select tid from teacher where tname ='李平老师'));

\# 查看所有学习李平老师课程的学生选课数

select student_id,count(course_id) from score where course_id in ( select cid from course where teacher_id in (select tid from teacher where tname ='李平老师')) group by student_id;

\# 找到所有选择了李平老师所有课程的学生id

select  student_id from (

select student_id,count(course_id) course_count from score where course_id in ( select cid from course where teacher_id in (select tid from teacher where tname ='李平老师')) group by student_id) t1

where t1.course_count =

(select count(cid) from course where teacher_id in (select tid from teacher where tname ='李平老师'));

\# 找到学生的其他信息

select sid,sname from student where sid in (

select  student_id from (

select student_id,count(course_id) course_count from score where course_id in ( select cid from course where teacher_id in (select tid from teacher where tname ='李平老师')) group by student_id) t1

where t1.course_count =

(select count(cid) from course where teacher_id in (select tid from teacher where tname ='李平老师'))

);

 

8、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；

\# 先找到每个学生的课程编号“1”的和课程编号“2”的成绩组成一张表

select t1.student_id from (select num num2,student_id from score where course_id = 2) t2 inner join (select student_id,num num1 from score where course_id = 1) t1 on t1.student_id = t2.student_id

\# 再找到课程编号“2”的成绩比课程编号“1”课程低的所有学生的学号

select t1.student_id from (select num num2,student_id from score where course_id = 2) t2 inner join (select student_id,num num1 from score where course_id = 1) t1 on t1.student_id = t2.student_id where num2 < num1

\# 再找到所有学生的学号、姓名

select sid,sname from student where sid in(select t1.student_id from (select num num2,student_id from score where course_id = 2) t2 inner join (select student_id,num num1 from score where course_id = 1) t1 on t1.student_id = t2.student_id where num2 < num1);

 

9、查询有课程成绩小于60分的同学的学号、姓名；

\# 先查询成绩小于60分的同学的学号

select distinct student_id from score where num < 60;

\# 再查询有课程成绩小于60分的同学的学号、姓名

select sid,sname from student where sid in (select distinct student_id from score where num < 60);

 

10、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；

\# 先看看学号为1的同学都学了哪些课程

select course_id from score where student_id = 1

\# 找到学习 学号为1的同学所学课程 的学号

select distinct student_id from score where course_id in (select course_id from score where student_id = 1);

\#  找到学习 学号为1的同学所学课程 的学号\姓名

select sid,sname from student where sid in (select distinct student_id from score where course_id in (select course_id from score where student_id = 1));

 

11、课程平均分从高到低显示

select course_id,avg(num) avg_num from score group by course_id order by avg_num desc;

 

12、查询出只选修了一门课程的全部学生的学号和姓名；

\# 查询出只选修了一门课程的全部学生的学号

select student_id,count(student_id) from score group by student_id having count(student_id) =1;

\# 查询出只选修了一门课程的全部学生的学号和姓名；

select sid,sname from student where sid in (select student_id from score group by student_id having count(student_id) =1);

 

13、查询男生、女生的人数；

select gender,count(sid) from student group by gender;

 

14、查询姓“张”的学生名单；

select * from student where sname like '张%';

 

15、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

\# 查询成绩的最高分

select course_id c1,max(num) from score group by course_id

\# 查询成绩的最低分

select course_id c1,min(num) from score group by course_id

\# 查询成绩的最高分和最低分拼接

select * from ( (select course_id c1,max(num) from score group by course_id) t1 inner join (select course_id c2,min(num) from score group by course_id) t2 on t1.c1 = t2.c2 );

\# 格式整理

select t1.c1,t1.max_num,t2.min_num from ( (select course_id c1,max(num) max_num from score group by course_id) t1 inner join (select course_id c2,min(num) min_num from score group by course_id) t2 on t1.c1 = t2.c2 );