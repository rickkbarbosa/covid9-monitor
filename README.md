# covid9-monitor
Gets information involving casualities and presents to JSON and Zabbix

![Grafana](grafana_dashboard.png)


### Usage

```
git@github.com:rickkbarbosa/covid9-monitor.git
pip install -r requirements.txt
```

### To Zabbix

Clone repository in a plase acessible by Zabbix (usually, /usr/lib/zabbix/externalscripts)
install python requirements on requirements.txt
Import template to zabbix dashboard (zabbix_template.xml)
Add template to a host

![Using on Zabbix](zabbix_template.png)

### To grafana
Install Zabbix Plugin datasource by [Alexander Zobnin](https://grafana.com/grafana/plugins/alexanderzobnin-zabbix-app)
Import dashboard to grafana
Points your Zabbix datasource
