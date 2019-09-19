from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy?charset=utf8')

# 一对多关系
from sqlalchemy.orm import relationship


class School(BaseModel):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)


class Student(BaseModel):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    stu2sch = Column(Integer, ForeignKey('school.id'))

    sch2stu = relationship('School', backref='sch2stu')


BaseModel.metadata.create_all(engine)
