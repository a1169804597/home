class School:
    def __init__(self,name,addr,type):
        self.name = name
        self.addr = addr
        self.type = type
    def __repr__(self):
        return 'School(%s,%s)' %(self.name,self.addr)
    def __str__(self):
        return '(%s,%s)' %(self.name,self.addr)
s1=School('小猿圈','北京','私立')


'''
str函数或者print函数调用时--->obj.__str__()
repr或者交互式解释器中调用时--->obj.__repr__()
如果__str__没有被定义,那么就会使用__repr__来代替输出
注意:这俩方法的返回值必须是字符串,否则抛出异常
'''