FROM public.ecr.aws/nginx/nginx:alpine
# Cache-bust: force rebuild with latest static files
COPY . /usr/share/nginx/html
EXPOSE 80
