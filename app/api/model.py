from api.databases import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__='Blog'

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    body=Column(String(100))
    user_id=Column(Integer,ForeignKey('User.id'))
    creator=relationship('User',back_populates='blogs')

class User(Base):
    __tablename__='User'
    id=Column(Integer,primary_key=True,index=True) # it is auto increment show it will not be show at the time of inserting data
    name=Column(String(100))
    email=Column(String(100))
    password=Column(String(100))
    blogs=relationship('Blog',back_populates='creator')

class NewUser(Base):
    __tablename__='newuser'
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String(100))

class Data(Base):
    __tablename__='data'
    id=Column(Integer,primary_key=True,index=True)
    group=Column(Integer)
    subgroup_id=Column(Integer)
    tenant_id=Column(Integer)
    email=Column(String(50))
    role=Column(String(50))
    firstname=Column(String(50))
    lastname=Column(String(50))
    password=Column(String(50))
    cell_number=Column(String(50))
    level_twomanager=Column(String(50))
    company_name=Column(String(50))
    account_name=Column(String(50))
    title=Column(String(50))
    country=Column(String(50))
    line_manager=Column(String(50))
    address=Column(String(50))
    department=Column(String(50))
    job_title=Column(String(50))
    date_of_birth=Column(String(50))
    start_date=Column(String(50))
    town=Column(String(50))
    postcode=Column(Integer)
    
 
