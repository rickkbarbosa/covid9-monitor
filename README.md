# covid19-monitor
Gets information involving CORONAVIRUS - COVID19 casualities and presents to JSON and Zabbix

![Grafana](grafana_dashboard.png)


### Usage

```
git@github.com:rickkbarbosa/covid9-monitor.git
pip install -r requirements.txt
```

### To Zabbix

Clone repository in a plase acessible by Zabbix (usually, /usr/lib/zabbix/externalscripts)
install python requirements on requirements.txt
Import template to zabbix dashboard (zabbix/zabbix_template.xml - Zabbix server 4.0 and above)
Add template to a host

![Using on Zabbix](zabbix_template.png)


## Additional adjustment on Zabbix 4.0.x versions:

Zabbiux 4.0.x contains a limitation involving number of dependendant items. 
A proposed workaround was sugested by [@hardwareadictos](https://github.com/rickkbarbosa/covid9-monitor/issues/10):

*  Change _/usr/share/zabbix/include/defines.inc.php:define('ZBX_DEPENDENT_ITEM_MAX_COUNT', 999)_; to 2999. 


### To grafana


* Install Zabbix Plugin datasource by [Alexander Zobnin](https://grafana.com/grafana/plugins/alexanderzobnin-zabbix-app)
* Install Worldmap Panel plugin(https://grafana.com/grafana/plugins/grafana-worldmap-panel/installation)
* Install Polystat Grafana plugin(https://grafana.com/grafana/plugins/grafana-polystat-panel/installation)
* Install Multistat Grafana plugin(https://grafana.com/grafana/plugins/michaeldmoore-multistat-panel)
* Install Pie Chart plugin(https://grafana.com/grafana/plugins/grafana-piechart-panel)
* Import dashboard _grafana_dashboard.json_ to grafana 
* Points your Zabbix datasource

### License

See LICENSE


### Thanks 

* [Zabbix Brasil](https://t.me/ZabbixBrasil) , for reviews and help with cleanup/garbage collecting
* Everaldo Santos Cabral, for Suggested applications organiztions and Zabbix 4.0 retro-compatible template
* [MrBits](https://github.com/mrbitsdcf)


### Donate 


* [Paypal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=29JLND674CAGY&currency_code=BRL)

* ![Grafana](qr_code.png)