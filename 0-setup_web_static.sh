#!/usr/bin/env bash
# Script using bash to setup webservers for deployment of simple HTML


apt-get update 
apt-get install -y nginx 
mkdir -p -m=755 /data/web_static/{releases/test,shared} || exit 0
echo 'Test file' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0

