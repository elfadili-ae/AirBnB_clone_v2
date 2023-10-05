# Server configuration

$conf = "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        add_header X-Served-By ${hostname};

        location /hbnb_static {
                alias /data/web_static/current/;
        }
        error_page 404 /custom_404.html;
        location = /custom_404.html {
                 root /var/www/html;
                 internal;
        }
        location /redirect_me {
                 return 301 https://www.youtube.com/watch?v=3lFkDc6dFoY;
        }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

-> file { '/data':
  ensure  => 'directory'
}

-> file { '/data/web_static':
  ensure => 'directory'
}

-> file { '/data/web_static/releases':
  ensure => 'directory'
}

-> file { '/data/web_static/releases/test':
  ensure => 'directory'
}

-> file { '/data/web_static/shared':
  ensure => 'directory'
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School\n"
}

-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
}

-> file { '/var/www/html':
  ensure => 'directory'
}

-> file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n"
}

-> file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
}

-> file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $conf
}

-> service {'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
