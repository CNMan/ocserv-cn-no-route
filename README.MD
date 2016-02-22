# ocserv-cn-no-route

## OpenConnect VPN Server

主页：[http://www.infradead.org/ocserv/](http://www.infradead.org/ocserv/)

下载：[http://www.infradead.org/ocserv/download.html](http://www.infradead.org/ocserv/download.html)

更新历史：[http://www.infradead.org/ocserv/changelog.html](http://www.infradead.org/ocserv/changelog.html)

源码：[https://gitlab.com/ocserv/ocserv.git](https://gitlab.com/ocserv/ocserv.git)

## OpenConnect VPN Client

主页：[http://www.infradead.org/openconnect/](http://www.infradead.org/openconnect/)

下载：[http://www.infradead.org/openconnect/download.html](http://www.infradead.org/openconnect/download.html)

更新历史：[http://www.infradead.org/openconnect/changelog.html](http://www.infradead.org/openconnect/changelog.html)

源码：[http://git.infradead.org/users/dwmw2/openconnect.git](http://git.infradead.org/users/dwmw2/openconnect.git)

## Cisco AnyConnect VPN Client

下载：[https://cnlic.com/share/client.html](https://cnlic.com/share/client.html)

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

## 喜讯

2015/12/08 Debian有官方ocserv源了：[https://tracker.debian.org/pkg/ocserv](https://tracker.debian.org/pkg/ocserv)

```
echo 'deb http://ftp.debian.org/debian/ unstable main contrib non-free' >> /etc/apt/sources.list
apt-get update
apt-get install ocserv
```
