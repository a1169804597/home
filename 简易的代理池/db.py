
from redis import *

Pool =ConnectionPool(host='localhost',port=6379,db=0,password='foobared')
Redis=StrictRedis(connection_pool=Pool)


def save_to_redis(i,result):
    Redis.set(i,result)
def get_to_redis(i):
    proxy=Redis.get(i)
    if proxy==None:
        pass
    else:
        return  proxy.decode()