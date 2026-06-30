FROM nginx:alpine
# Cache-bust: ensure latest static files are copied
COPY . /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
