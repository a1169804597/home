#接口函数，127.0.0.1:5555
#/Welcome to Proxy Pool System
#/random 随机产生代理
#/count 将获取代理池的容量
from flask import Flask, g

from 简易的代理池.db import *

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = Redis
    return g.redis  #代理是从redis数据库中获取的


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_to_redis
    return conn.random()

if __name__ == '__main__':
    app.run()
