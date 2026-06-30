FROM nginx:alpine
# Cache-bust: ensure latest static files are copied
COPY . /usr/share/nginx/html
EXPOSE 80
