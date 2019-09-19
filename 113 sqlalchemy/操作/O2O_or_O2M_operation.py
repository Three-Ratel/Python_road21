from sqlalchemy.orm import sessionmaker

from 操作.O2O_or_O2M import School, Student, engine

select_db = sessionmaker(engine)
db_session = select_db()

# 正向插入
stu = Student(name='iris', stu2sch=School(name='BeiJing'))
db_session.add(stu)
db_session.commit()
db_session.close()