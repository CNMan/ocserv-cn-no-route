# ocserv-cn-no-route

## 產生過程

1、生成最新国内IP列表chnroute.txt

```
wget -N http://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-extended-latest
wget -N http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-extended-latest
wget -N http://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest
wget -N http://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest
wget -N http://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest
cat delegated-afrinic-extended-latest delegated-apnic-extended-latest delegated-arin-extended-latest delegated-lacnic-extended-latest delegated-ripencc-extended-latest>>delegated-all-latest
cat delegated-all-latest | grep ipv4 | grep CN | awk -F\| '{ printf("%s/%d\n", $4, 32-log($5)/log(2)) }' >chnroute.txt
```

2、合并chnroute.txt(336909056 IPs)，生成chnroute_merged.txt(336909056 IPs)

3、将所有/12及以上改成/11，并合并，生成11_143.txt(713031680 IPs)

4、生成不含保留IP的cn-no-route1.txt(712965888 IPs)

剔除11_143.txt中保留IP：192.168.0.0/16、203.0.113.0/24

5、添加保留IP并合并，生成cn-no-route2.txt(1305674752 IPs)

192.168.0.0/24需单列，否则Windows客户端192.168.x.x整段无法接收。

## 注意事項

1、0.10.5 及之前版本ocserv需要修改src/vpn.h来支持超过96行(ocserv默认值)但不超过200行(Cisco AnyConnect最大值)的路由表:

```
#define MAX_CONFIG_ENTRIES 96
```

96改为200以上

0.10.6 及之后版本ocserv不需要修改，参考[https://gitlab.com/ocserv/ocserv/issues/17](https://gitlab.com/ocserv/ocserv/issues/17)

2、根据[Cisco官方文档](http://www.cisco.com/c/en/us/products/collateral/security/ios-sslvpn/prod_white_paper0900aecd80512071.html)，no-route和route不能同时使用。

```
You can specify either split-include or split-exclude, but you cannot specify both options.
```

## Q&A

为什么选择将所有/12及以上改成/11，而不是将所有/13及以上改成/12或将所有/11及以上改成/10？

* 若將所有/13及以上改成/12，則不含保留IP的路由表是261條(580911104 IPs)，超過了客戶端限制的最高200條。
* 若將所有/12及以上改成/11，則不含保留IP的路由表是143條(713031680 IPs)。
* 若將所有/11及以上改成/10，則不含保留IP的路由表是69條(847249408 IPs)，IP範圍進一步擴大，誤差進一步擴大。

## [保留IP](http://en.wikipedia.org/wiki/Reserved_IP_addresses) (592708864 IPs)
```
0.0.0.0/8
10.0.0.0/8
100.64.0.0/10
127.0.0.0/8
169.254.0.0/16
172.16.0.0/12
192.0.0.0/24
192.0.2.0/24
192.88.99.0/24
192.168.0.0/16
198.18.0.0/15
198.51.100.0/24
203.0.113.0/24
224.0.0.0/4
240.0.0.0/4
255.255.255.255/32
```

##原样保留部分
```
52.80.0.0/14
54.222.0.0/15
91.234.36.0/24
137.59.88.0/22
152.104.128.0/17
159.226.0.0/16
161.207.0.0/16
162.105.0.0/16
166.111.0.0/16
168.160.0.0/16
170.179.0.0/16
47.92.0.0/14
47.96.0.0/11
192.124.154.0/24
192.188.170.0/24
40.72.0.0/15
40.125.128.0/17
40.126.64.0/18
167.139.0.0/16
167.189.0.0/16
167.220.244.0/22
144.0.0.0/16
144.7.0.0/16
144.12.0.0/16
144.52.0.0/16
144.123.0.0/16
144.255.0.0/16
211.64.0.0/13
211.80.0.0/12
211.96.0.0/13
211.136.0.0/13
211.144.0.0/12
211.160.0.0/13
157.0.0.0/16
157.18.0.0/16
157.61.0.0/16
157.122.0.0/16
157.148.0.0/16
157.156.0.0/16
157.255.0.0/16
```
