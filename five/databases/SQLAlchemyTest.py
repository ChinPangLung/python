# ORM框架
# pip3 install sqlalchemy

# 导入orm框架
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()


class User(Base):
    # 表的名称
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据的链接
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
db_session = DBSession()
print('==================================')
# 创建新User对象(insert into)
# new_user = User(id='2', name='chinpang')
# add to session
# db_session.add(new_user)
print('==================================')
# query data
user = db_session.query(User).filter(User.id == '1').one()
print(type(user))
print(user.id)
print(user.name)
print('==================================')
db_session.commit()
db_session.close()
