from multiprocessing import Process, Pool
import time, os


def Foo(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100


def Bar(arg):
    print('-->exec done:', arg, os.getpid())


if __name__ == '__main__':
    pool = Pool(5)

    print("主进程：", os.getpid())  # 打印主进程id
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)
        ##callback叫做回调，就是当执行完了func=Foo后，才会执行callback=Bar(每个进程执行完了后都会执行回调)。
        ## 回调可以用于当执行完代码后做一些后续操作，比如查看完命令后，通过回调进行备份；或者执行完什么动作后，做个日志等。
        ## 备份、写日志等在子进程中也可以执行，但是为什么要用回调呢！ 这是因为如果用子进程，有10个子进程就得连接数据库十次，而使用回调的话是用主进程连接数据库，所以只连接一次就可以了，这样写能大大提高运行效率。
        ##通过主进程建立数据库的连接的话，因为在同一个进程中只能在数据库建立一次连接，所以即使是多次被子进程回调，也不会重复建立连接的，因为数据库会限制同一个进程最大连接数，这都是有数据库设置的。

    print('end')
    pool.close()
    pool.join()