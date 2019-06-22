- **数据准备day41中的tables**

1. 查询男生、女生的人数；

   - select gender, count(gender) from student group by gender;
2. 查询姓“张”的学生名单；

   -  select sname from student where sname like '张%';
3. 课程平均分从高到低显示；

   - select co.cname, sc.avg_num from course co inner join (select  course_id, avg(num) avg_num from score group by course_id) sc on co.cid = sc.course_id order by sc.avg_num desc;
4. 查询有课程成绩小于60分的同学的学号、姓名；

   -  select st.sid, st.sname from student as st inner join (select * from score where num < 60 group by student_id) sc on st.sid=sc.student_id;
5. 查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；

   - select st.sid, st.sname from student st where sid in (select student_id from score where course_id in (select course_id from score where student_id = 1) and student_id != 1);
6. 查询出只选修了一门课程的全部学生的学号和姓名；

   - select sid,sname from student inner join (select student_id from score group by student_id having count(course_id) = 1) sc on sid=sc.student_id;
   - select sid,sname from student where sid in (select student_id from score group by student_id having count(*)=1);
7. 查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

   - select course_id, max(num), min(num) from score group by course_id;

   - select cname,max_num,min_num from course inner join (select sc1.course_id, sc1.max_num, sc2.min_num from ((select course_id,max(num) max_num from score group by course_id) sc1 inner join (select course_id,min(num) min_num from score group by course_id) sc2 on sc1.course_id=sc2.course_id)) sc3 on sc3.course_id=cid;
8. 查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；

   - select sid, sname from student inner join (select sc1.student_id, num1, num2 from (select student_id, num  num1 from score  where course_id =1 group by student_id) sc1 inner join (select student_id, num  num2 from score  where course_id =2 group by student_id) sc2 on sc1.student_id = sc2.student_id where num1 > num2) sc3 on sid=sc3.student_id;
9. 查询“生物”课程比“物理”课程成绩高的所有学生的学号；

   - select sid,sname from student inner join (select sc1.student_id, num1, num2 from (select student_id, num  num1 from score  where course_id =(select cid from course where cname='生物') group by student_id) sc1 inner join (select student_id, num  num2 from score  where course_id in (select cid from course where cname='物理') group by student_id) sc2 on sc1.student_id = sc2.student_id where num1 > num2) sc3 on sid=sc3.student_id;
10. 查询平均成绩大于60分的同学的学号和平均成绩;

    - select sid, sname, avg_num from student  st inner join (select student_id, avg(num) avg_num  from score group by student_id having avg(num) > 60) sc1 where st.sid = sc1.student_id ;
11. 查询所有同学的学号、姓名、选课数、总成绩；

    -  select sid, sname, co_amount, sc_amount from student st inner join (select student_id,count(course_id) co_amount, sum(num) sc_amount  from score group by student_id ) sc1 on sc1.student_id = st.sid;
12. 查询姓“李”的老师的个数；

    - select group_concat(tname) '李**', count(*) num from teacher where tname like '李%';
13. 查询没学过“张磊老师”课的同学的学号、姓名；

    - select st1.sid, st1.sname from student st1 where st1.sid not in (select st.sid from student  st inner join (select student_id from score sc inner join (select cid from course co  inner join (select tid from teacher where tname='张磊老师') te on te.tid=co.teacher_id) tc on  tc.cid=sc.course_id) tcs on tcs.student_id=st.sid);
14. 查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；

    - select sid, sname from student where sid in (select sc1.student_id from (select student_id from score where course_id =1) sc1 inner join (select student_id from score where course_id =2) sc2 on sc1.student_id = sc2.student_id);
15. 查询学过“李平老师”所教的所有课的同学的学号、姓名；

    - select sid, sname from student where sid in (select student_id from score sc inner join (select cid from course where teacher_id = (select tid from teacher where tname='李平老师')) tc on tc.cid=sc.course_id group by student_id having count(*) = (select count(cid) from course where teacher_id = (select tid from teacher where tname='李平老师')));
16. 查询没有学全所有课的同学的学号、姓名；

    - select sid, sname from student where sid in (select student_id from (select student_id, count(course_id) co_amount from score group by student_id) sc inner join (select count(*) amount from course) co on co.amount>sc.co_amount);
17. 查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；

    - select sid, sname from student where sid in (select student_id from (select student_id, sc1.course_id from score sc1 inner join (select course_id from score where student_id=2) sc2 on sc2.course_id = sc1.course_id) sc3 group by sc3.student_id having count(*) = (select count(course_id) from score where student_id=2));
18. 删除学习“张磊老师 ”老师课的SC表记录；

    -  delete from score where course_id = (select cid from course where teacher_id=(select tid from teacher where tname='张磊老师'));
19. 向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 

    - 
20. 按平均成绩从低到高显示所有学生的“物理”、“美术”、“体育”三门的课程成绩，按如下形式显示： 学生ID,物理,美术,体育,有效课程数,有效平均分；
```mysql
# 查找物理课程，对应的学生和成绩
select student_id,num from score where course_id = (select cid from course where cname = '物理');
# 查找美术课程，对应的学生和成绩
select student_id,num from score where course_id = (select cid from course where cname = '美术');
# 查找体育课程，对应的学生和成绩
select student_id,num from score where course_id = (select cid from course where cname = '体育');
# 平均分
select student_id,avg(num),count(num) from score group by student_id;
# 最终结果
select sid 学生ID,t1.num 美术, t2.num 物理, t3.num 体育,t4.count_course 有效课程数,t4.avg_num 有效平均分 from student
left join (select student_id,num from score where course_id = (select cid from course where cname = '美术')) t1 on student.sid = t1.student_id

left join (select student_id,num from score where course_id = (select cid from course where cname = '物理')) t2 on student.sid = t2.student_id

left join (select student_id,num from score where course_id = (select cid from course where cname = '体育')) t3 on student.sid = t3.student_id

left join (select student_id,avg(num) avg_num,count(num) count_course from score group by student_id)  t4 on student.sid = t4.student_id
```

21. 查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

```mysql
select course_id 课程ID, max(num) 最高分, min(num) 最低分 from score group by course_id;
```

#### 22. 按各科平均成绩从低到高和及格率的百分数从高到低顺序；

```mysql
# 平均成绩
select course_id,avg(num) from score group by course_id;
# 及格人数
select course_id, count(*) from score where num > 60 group by course_id;
# 及格率
select t1.course_id, t1.count1/t2.count2 及格率 from
(select course_id, count(*) count1 from score where num > 60  group by  course_id) t1 left join (select course_id, count(*) count2 from score group by course_id) t2 on t1.course_id=t2.course_id;
# 最终结果
select t1.course_id, t1.avgnum 平均分, t2.rate 及格率 from (select course_id,avg(num) avgnum from score group by course_id) t1 
left join (select t1.course_id, t1.count1/t2.count2 rate from (select course_id, count(*) count1 from score where num > 60  group by  course_id) t1 left join (select course_id, count(*) count2 from score group by course_id) t2 on t1.course_id=t2.course_id) t2 on t1.course_id=t2.course_id order by t1.avgnum desc, t2.rate;
```

#### 23. 查询各科成绩前三名的记录:(不考虑成绩并列情况) 

```mysql

```



1. 查询每门课程被选修的学生数；
2. 查询同名同姓学生名单，并统计同名人数；
3. 查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
4. 查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
5. 查询课程名称为“数学”，且分数低于60的学生姓名和分数；
6. 查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 
7. 求选了课程的学生人数
8. 查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
9. 查询各个课程及相应的选修人数；
10. 查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
11. 查询每门课程成绩最好的前两名；
12. 检索至少选修两门课程的学生学号；
13. 查询全部学生都选修的课程的课程号和课程名；
14. 查询没学过“叶平”老师讲授的任一门课程的学生姓名；
15. 查询两门以上不及格课程的同学的学号及其平均成绩；
16. 检索“004”课程分数小于60，按分数降序排列的同学学号；
17. 删除“002”同学的“001”课程的成绩；