FROM nginx:stable-alpine
ADD ./nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /var/www/html/static \
 && mkdir -p /var/run/django
VOLUME "/var/www/html"
VOLUME "/var/run/django"