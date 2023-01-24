server {
    listen 80;
    server_name 185.196.213.35 www.185.196.213.35;

    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen  443 ssl;
    server_name 185.196.213.35 www.185.196.213.35;

    ssl_certificate /etc/letsencrypt/live/185.196.213.35/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/185.196.213.35/privkey.pem

    include /etc/nginx/options-ssl-nginx.conf;

    ssl_dhparam /vol/proxy/ssl-dhparams.pem;

    add_header Strict-Transport-Security "max-age=31536000;
    includeSubDomains" always;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass 185.196.213.35:8000;
        include /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
}