1、查询没有学全所有课的同学的学号、姓名；

\# 先统计一共有多少门课程

select count(cid) from course;

\# 查看每个学生选择的课程书

select count(course_id) from score group by student_id;

\# 查询所学课程数小于总课程数的学生学号

select student_id

from (select count(course_id) c_course_id,student_id from score group by student_id) t1 

where t1.c_course_id <  (select count(cid) from course) ;

\# 查询没有学全所有课的同学的学号、姓名；

select sid,sname from student where sid in (

 select student_id from (select count(course_id) c_course_id,student_id from score group by student_id

 ) t1 where t1.c_course_id <  (select count(cid) from course)

) ;

 

2、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；

\# 先查询2号同学学了哪些课程

select * from score where student_id =2;

\# 找到学习了2号同学没学习课程的所有同学（找到所有和2号同学学习的课程不一样的同学）

select student_id from score where course_id not in (select course_id from score where student_id=2)

\# 找到score表中所有的学生并且把 2号同学 以及（和2号同学学习的课程不一样的同学）排除出去

select student_id from score where student_id not in (select student_id from score where course_id not in (select course_id from score where student_id=2)) and student_id !=2

\# 对剩余的和2号同学所选课程没有不同的同学所选课程数进行统计，如果和2号同学的课程数相同，就是选择了相同的课程

select student_id from score where student_id not in (

 select student_id from score where course_id not in (select course_id from score where student_id=2)

 ) and student_id !=2

group by student_id 

having count(course_id)= (select count(course_id) from score where student_id=2);

 

3、删除学习“叶平”老师课的SC(score)表记录；

\# 先查出李平老师的id

select tid from teacher where tname = '李平老师';

\# 查看李平老师所教授的课程

select cid from course where teacher_id = (select tid from teacher where tname = '李平老师’);

\# 查看李平老师所教课程的成绩数据

select * from score where course_id in (select cid from course where teacher_id = (select tid from teacher where tname = '李平老师'));

\# 执行删除命令

delete from score where course_id in (select cid from course where teacher_id = (select tid from teacher where tname = '李平老师'));

 

4、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 

\#  先找寻上过2号课程的同学

select student_id from score where course_id = 2;

\# 再找到没上过2号课程的所有同学

select * from student where sid not in (select student_id from score where course_id = 2);

\#  计算出学习2号课程的同学的平均成绩

select avg(num) from score where course_id = 2 group by course_id;

\# 用笛卡尔积将上述两个表拼起来

select * from (select sid from student where sid not in (select student_id from score where course_id = 2)) t1,(select avg(num) from score where course_id = 2 group by course_id) t2;

\#  向SC表中插入记录

insert into score (course_id,student_id,num)   select 2,t1.sid,t2.avg_num from (select sid from student where sid not in (select student_id from score where course_id = 2)) t1,(select avg(num) avg_num from score where course_id = 2 group by course_id) t2;

 

5、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；

\# 查看每个学生的数学成绩

select student_id,num from score where course_id = (select cid from course where cname = '数学');

\#  查看每个学生的语文成绩

select student_id,num from score where course_id = (select cid from course where cname = '语文');

\#  查看每个学生的英语成绩

select student_id,num from score where course_id = (select cid from course where cname = '英语');

\# 查看每个学生的平均成绩

select student_id,avg(num),count(num) from score group by student_id;

\# 将上面的几张表拼接起来,为了生成所有学生的信息，用student表作为左连接的第一张表

select sid 学生ID,t2.num 语文,t1.num 数学, t3.num 英语,t4.count_course 有效课程数,t4.avg_num 有效平均分 from student 

 left join (select student_id,num from score where course_id = (select cid from course where cname = '数学')) t1

 on student.sid = t1.student_id

 left join (select student_id,num from score where course_id = (select cid from course where cname = '语文')) t2

 on student.sid = t2.student_id

 left join (select student_id,num from score where course_id = (select cid from course where cname = '英语')) t3

 on student.sid = t3.student_id

 left join (select student_id,avg(num) avg_num,count(num) count_course from score group by student_id)  t4

 on student.sid = t4.student_id

 

6、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

select course_id 课程ID,max(num) 最高分,min(num) 最低分 from score group by course_id;

 

7、按各科平均成绩从低到高和及格率的百分数从高到低顺序；

\# 方法1:

\# 先求平均成绩

select course_id,avg(num) from score group by course_id;

\# 解决计算各科及格率的问题

所有及格的人/所有人数

select t1.course_id,t1.count1/t2.count2 from 

(select course_id,count(course_id) count1 from score where num>60 group by course_id) t1 

left join

(select course_id,count(course_id) count2 from score group by course_id) t2

on t1.course_id = t2.course_id;

\# 根据上述内容进行表的拼接

select  t_out1.course_id,t_out1.avgnum, t_out2.pass_per from 

(select course_id,avg(num) avgnum from score group by course_id ) t_out1

left join 

(select t1.course_id,t1.count1/t2.count2 pass_per from 

(select course_id,count(course_id) count1 from score where num>60 group by course_id) t1 

left join

(select course_id,count(course_id) count2 from score group by course_id) t2

on t1.course_id = t2.course_id) t_out2

on  t_out1.course_id = t_out2.course_id

\# 加上排序

select  t_out1.course_id,t_out1.avgnum, t_out2.pass_per from  (select course_id,avg(num) avgnum from score group by course_id ) t_out1 left join  (select t1.course_id,t1.count1/t2.count2 pass_per from  (select course_id,count(course_id) count1 from score where num>60 group by course_id) t1  left join (select course_id,count(course_id) count2 from score group by course_id) t2 on t1.course_id = t2.course_id) t_out2 on  t_out1.course_id = t_out2.course_id order by avgnum ,pass_per desc;

 

 

\# 方法2 

\# 使用case when直接计算合格率

select 

sum(case when num>60 then 1 else 0 end)/count(course_id)

from score group by course_id

\# 加上课程id和平均值

select  course_id,avg(num),

sum(case when num>60 then 1 else 0 end)/count(course_id)

from score group by course_id

\# 加上排序

select  course_id,avg(num) avgnum,

sum(case when num>60 then 1 else 0 end)/count(course_id) pass_per 

from score group by course_id

 order by avgnum ,pass_per desc;

 

 

8、查询各科成绩前三名的记录:(不考虑成绩并列情况) 

```mysql
select
t1.sid,t1.student_id,t1.course_id,t1.num from score t1
left join
    (
    select sid,course_id,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0, 1) as first_num,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 1, 1) as second_num,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 2, 1) as third_num
    from score as s1
    ) t2
on t1.sid = t2.sid
where t1.num = t2.first_num or t1.num = t2.second_num or t1.num = t2.third_num;
```

 

 

 

9、查询每门课程被选修的学生数；

select course_id,count(course_id) from score group by course_id;

 

10、查询同名同姓学生名单，并统计同名人数；

select sname,count(1) as count from student group by sname;

 

11、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

select course_id,avg(if(isnull(num), 0 ,num)) as avg from score group by course_id order by avg  asc,course_id desc;

 

12、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；

select student_id,sname, avg(if(isnull(num), 0 ,num)) from score left join student on score.student_id = student.sid group by student_id;

 

13、查询课程名称为“数学”，且分数低于60的学生姓名和分数；

select student.sname,score.num from score

left join course on score.course_id = course.cid

left join student on score.student_id = student.sid

where score.num < 60 and course.cname = '数学'

 

 

14、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 

select * from score where score.student_id = 3 and score.num > 80

 

15、求选了课程的学生人数

select sid,sname from student where sid not in (select student_id from score group by student_id);

 

16、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；

\# 先找到“杨艳”老师的教师id

select tid from teacher where tname = '杨艳';

\# 再找到杨艳老师教的所有课程

select cid from course where teacher_id in (select tid from teacher where tname = '杨艳');

\# 再找到杨艳老师教的所有课程的最高分

select max(num) from score where course_id in (select cid from course where teacher_id in (select tid from teacher where tname = '李平老师'));

\# 再找到杨艳老师教的所有课程的最高分对应的学生

select distinct student_id,num from score 

where num = (select max(num) from score where course_id in (select cid from course where teacher_id in (select tid from teacher where tname = '李平老师'))) 

and course_id in   (select cid from course where teacher_id in (select tid from teacher where tname = '李平老师'));

\# 找到学生的姓名

select student.sname,t1.num from(

select distinct student_id,num from score 

where num = (select max(num) from score where course_id in (select cid from course where teacher_id in (select tid from teacher where tname = '李平老师'))) 

and course_id in   (select cid from course where teacher_id in (select tid from teacher where tname = '李平老师'))

) t1

left join

student

on 

t1.student_id = student.sid;

 

17、查询各个课程及相应的选修人数；

select course.cname,count(1) from score

left join course on score.course_id = course.cid

group by course_id;

 

18、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；

select DISTINCT s1.course_id,s2.course_id,s1.num,s2.num from score as s1, score as s2 where s1.num = s2.num and s1.course_id != s2.course_id;

 

19、查询每门课程成绩最好的前两名；

   先查询每条数据对应学科成绩的第一名和第二名，这里必须要保留所有的s1，以便后续进行连表查询

```
select sid,course_id,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0, 1) as first_num,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 1, 1) as second_num
from score as s1

按照sid连表，把学生的成绩和对应的第一名、第二名成绩连起来
select
* from score t1
left join
    (
    select sid,course_id,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0, 1) as first_num,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 1, 1) as second_num
    from score as s1
    ) t2
on t1.sid = t2.sid

判断如果学生的成绩是第一名、第二名的成绩，那么就符合条件，显示学生的id、学科和成绩
select
t1.sid,t1.student_id,t1.course_id,t1.num from score t1
left join
    (
    select sid,course_id,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0, 1) as first_num,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 1, 1) as second_num
    from score as s1
    ) t2
on t1.sid = t2.sid
where t1.num = t2.first_num or t1.num = t2.second_num;
```

20、检索至少选修两门课程的学生学号；

select student_id from score group by student_id having count(student_id) > 1;

 

21、查询全部学生都选修的课程的课程号和课程名；

\# 先查看一共有多少学生

select count(sid) from student;

\#  查看哪一门课选秀的学生个数和学生的总个数相等

select course_id from score group by course_id having count(student_id) = (select count(sid) from student);

 

22、查询没学过“叶平”老师讲授的任一门课程的学生姓名；

\# 先查看要查找老师的id

select tid from teacher where tname = '李平老师';

\# 查看该老师交了哪些课程

select cid from course where teacher_id in (select tid from teacher where tname = '李平老师')

\# 看看有多少学生学习了该老师的课程

select distinct student_id from score where course_id in (select cid from course where teacher_id in (select tid from teacher where tname = '李平老师'));

\# 把不在上表中的学生姓名查出来

select sname from student where sid not in (select distinct student_id from score where course_id in (select cid from course where teacher_id in (select tid from teacher where tname = '李平老师')));

 

23、查询两门以上不及格课程的同学的学号及其平均成绩；

select student_id,avg(num) from score where num<60 group by student_id having count(num)>=2;

 

 

24、检索“004”课程分数小于60，按分数降序排列的同学学号；

select student_id from score where num< 60 and course_id = 4 order by num desc;

 

25、删除“002”同学的“001”课程的成绩；

delete from score where course_id = 1 and student_id = 2