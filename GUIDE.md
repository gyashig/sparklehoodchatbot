## Hosting guide

[culled from here](https://jqn.medium.com/deploy-a-flask-app-on-aws-ec2-1850ae4b0d41)

- Select the Ubuntu Server 16.04 LTS (HVM), SSD Volume Type — ami-43a15f3e instead of the Amazon Linux
- Click on Review and Launch.
- set http tcp 80 under security groups and ssh tcp 22 to access from anywhere
- run sudo apt-get update
- run sudo apt-get install apache2
- run sudo apt-get install libapache2-mod-wsgi-py3
- test run your public 1pv4 address
- sudo apt-get install python-pip
- clone code
- cd into code directory
- sudo ln -sT ~/sparklehoodchatbot /var/www/html/sparklehoodchatbot
- create a wsgi file
- Go to /etc/apache2/sites-enabled/000-default.conf
- Add the following block after the `DocumentRoot /var/www/html` line

```
WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi
<Directory flaskapp>
    WSGIProcessGroup flaskapp
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
```

- Restart the server by running `sudo service apache2 restart`
