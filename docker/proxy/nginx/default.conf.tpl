server {
    listen 80;
    server_name 185.196.213.35 www.185.196.213.35

    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}