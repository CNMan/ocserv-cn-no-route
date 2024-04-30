# -*- coding: utf-8 -*-

import os,re,netaddr,requests
from netaddr import *

r = requests.get('https://raw.githubusercontent.com/CNMan/chinaroute/master/cnroute_merged.txt')
cnroute_merged = open('cnroute_merged.txt', 'w')
cnroute_merged.write(r.text)
cnroute_merged.close()

# 将所有/12-/32替换为/11
mergedlines = [line.rstrip('\n') for line in open('cnroute_merged.txt')]
mergedlines = [w.replace('/12','/11') for w in mergedlines]
mergedlines = [w.replace('/13','/11') for w in mergedlines]
mergedlines = [w.replace('/14','/11') for w in mergedlines]
mergedlines = [w.replace('/15','/11') for w in mergedlines]
mergedlines = [w.replace('/16','/11') for w in mergedlines]
mergedlines = [w.replace('/17','/11') for w in mergedlines]
mergedlines = [w.replace('/18','/11') for w in mergedlines]
mergedlines = [w.replace('/19','/11') for w in mergedlines]
mergedlines = [w.replace('/20','/11') for w in mergedlines]
mergedlines = [w.replace('/21','/11') for w in mergedlines]
mergedlines = [w.replace('/22','/11') for w in mergedlines]
mergedlines = [w.replace('/23','/11') for w in mergedlines]
mergedlines = [w.replace('/24','/11') for w in mergedlines]
mergedlines = [w.replace('/25','/11') for w in mergedlines]
mergedlines = [w.replace('/26','/11') for w in mergedlines]
mergedlines = [w.replace('/27','/11') for w in mergedlines]
mergedlines = [w.replace('/28','/11') for w in mergedlines]
mergedlines = [w.replace('/29','/11') for w in mergedlines]
mergedlines = [w.replace('/30','/11') for w in mergedlines]
mergedlines = [w.replace('/31','/11') for w in mergedlines]
mergedlines = [w.replace('/32','/11') for w in mergedlines]

# 生成不含保留IP的cn-no-route1.txt
summary = netaddr.cidr_merge(sorted(mergedlines))
s = IPSet(summary)
s.remove('0.0.0.0/8')
s.remove('10.0.0.0/8')
s.remove('100.64.0.0/10')
s.remove('127.0.0.0/8')
s.remove('169.254.0.0/16')
s.remove('172.16.0.0/12')
s.remove('192.0.0.0/24')
s.remove('192.0.2.0/24')
s.remove('192.88.99.0/24')
s.remove('192.168.0.0/16')
s.remove('198.18.0.0/15')
s.remove('198.51.100.0/24')
s.remove('203.0.113.0/24')
s.remove('224.0.0.0/4')
s.remove('240.0.0.0/4')
s.remove('255.255.255.255/32')
summary = netaddr.cidr_merge(sorted(s.iter_cidrs()))
norouteone = open('cn-no-route1.txt', 'w')
norouteone.write('\n'.join([ 'no-route = ' + str(x.ip) + '/' + str(x.netmask) for x in summary ]))
norouteone.close()

# 生成含保留IP的cn-no-route2.txt
s = IPSet(summary)
s.add('0.0.0.0/8')
s.add('10.0.0.0/8')
s.add('100.64.0.0/10')
s.add('127.0.0.0/8')
s.add('169.254.0.0/16')
s.add('172.16.0.0/12')
s.add('192.0.0.0/24')
s.add('192.0.2.0/24')
s.add('192.88.99.0/24')
s.add('192.168.0.0/16')
s.add('198.18.0.0/15')
s.add('198.51.100.0/24')
s.add('203.0.113.0/24')
s.add('224.0.0.0/4')
s.add('240.0.0.0/4')
s.add('255.255.255.255/32')
summary = netaddr.cidr_merge(sorted(s.iter_cidrs()))
noroute = open('cn-no-route.txt', 'w')
noroute.write('\n'.join([ 'no-route = ' + str(x.ip) + '/' + str(x.netmask) for x in summary ]))
noroute.close()

# 例外处理192.168.0.0/24
open('cn-no-route2.txt', 'w').write(re.sub('no-route = 192.168.0.0/255.255.0.0', 'no-route = 192.168.0.0/255.255.255.0\nno-route = 192.168.1.0/255.255.255.0\nno-route = 192.168.2.0/255.255.254.0\nno-route = 192.168.4.0/255.255.252.0\nno-route = 192.168.8.0/255.255.248.0\nno-route = 192.168.16.0/255.255.240.0\nno-route = 192.168.32.0/255.255.224.0\nno-route = 192.168.64.0/255.255.192.0\nno-route = 192.168.128.0/255.255.128.0', open('cn-no-route.txt', 'r').read()))
os.remove('cn-no-route.txt')

os.remove('cnroute_merged.txt')
