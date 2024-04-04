#!/usr/bin/env bash
# set up a web server for deployment

app-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
  <head>
    </head>
      <body>
          Holberton School
	    </body>"> /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgr -R ubuntu /data/

printf %S "server{
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-served-By $HOSTNAME;
      root /var/www/html;
      index index.html index.html;

      location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
    }
    location /redirect_me {
       return 301 http://http://btechmedservise.tech/;
     }
   error_page 404 /404.html;
   location /404 {
     root /var/www/html;
     internal;
}
}" > /etc/nginx/sites-available/default

service nginx restart
   

