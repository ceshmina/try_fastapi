FROM nginx:1.27.3

COPY nginx/default.conf /etc/nginx/conf.d/default.conf
