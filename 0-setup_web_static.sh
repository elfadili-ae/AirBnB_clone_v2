#!/usr/bin/env bash
#deply web_static to servers

sudo apt -y update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

hbnb_static="        location /hbnb_static {
                alias /data/web_static/current/;
}"
sudo sed -i '54r /dev/stdin'  /etc/nginx/sites-enabled/default <<< "$hbnb_static"

sudo service nginx restart
