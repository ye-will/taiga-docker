FROM nginx:1.7

MAINTAINER Hylke Visser <htdvisser@gmail.com>

ARG TAIGA_FRONT_VER
ENV TAIGA_FRONT_VER ${TAIGA_FRONT_VER:-3.1.3-stable}
ARG TAIGA_GITHUB_AUTH_VER
ENV TAIGA_GITHUB_AUTH_VER ${TAIGA_GITHUB_AUTH_VER:-3.1}

# Install Git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# NginX Configuration
ADD nginx.conf /etc/nginx/nginx.conf
ADD mime.types /etc/nginx/mime.types
ADD web-http.conf /etc/nginx/web-http.conf
ADD web-https.conf /etc/nginx/web-https.conf

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# Install taiga-front-dist
RUN \
  mkdir -p /taiga && \
  cd /taiga && \
  git clone -b "${TAIGA_FRONT_VER}" --single-branch --depth 1 https://github.com/taigaio/taiga-front-dist.git && \
  git clone -b "${TAIGA_GITHUB_AUTH_VER}" --single-branch --depth 1 https://github.com/taigaio/taiga-contrib-github-auth.git && \
  mkdir -p /taiga/taiga-front-dist/dist/plugins && \
  ln -s /taiga/taiga-contrib-github-auth/front/dist /taiga/taiga-front-dist/dist/plugins/github-auth

# Configuration and Start scripts
ADD ./configure /taiga/configure
ADD ./start /taiga/start
RUN chmod +x /taiga/configure /taiga/start

EXPOSE 80 443

CMD ["/taiga/start"]
