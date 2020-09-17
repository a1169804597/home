#__author:  Administrator
#date:  2016/11/1
from src.repository.user_type import UserTypeRepository
def add_type():
    caption = input('请输入用户类型的标题：')
    # 执行SQL语句
    obj = UserTypeRepository()
    obj.add(caption)

