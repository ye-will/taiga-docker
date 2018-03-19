FROM node:6-alpine

MAINTAINER Will Ye <yeah_well@live.com>

EXPOSE 8888

RUN \
  apk --update add --no-cache git

# Install taiga-event
RUN \
  mkdir -p /taiga/taiga-events && \
  git clone --single-branch --depth 1 https://github.com/taigaio/taiga-events.git /taiga/taiga-events && \
  cd /taiga/taiga-events && \
  npm install && \
  npm install -g coffee-script

ADD ./docker-entrypoint.sh /taiga/taiga-events/docker-entrypoint.sh
RUN chmod +x /taiga/taiga-events/docker-entrypoint.sh

WORKDIR /taiga/taiga-events
CMD ["./docker-entrypoint.sh"]
