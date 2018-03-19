FROM python:3.4

MAINTAINER Will Ye <yeah_well@live.com>

EXPOSE 8000

ARG TAIGA_BACK_VER
ENV TAIGA_BACK_VER ${TAIGA_BACK_VER:-3.2.2}

# Install dependencies
RUN \
  apt-get update -qq && \
  apt-get install -y netcat gettext && \
  rm -rf /var/lib/apt/lists/*

# Install taiga-back
RUN \
  mkdir -p /taiga && \
  useradd -d /taiga taiga && \
  mkdir /taiga/media /taiga/static && \
  git clone -b "${TAIGA_BACK_VER}" --single-branch --depth 1 https://github.com/taigaio/taiga-back.git /taiga/taiga-back && \
  cd /taiga/taiga-back && \
  pip install -r requirements.txt

ADD ./plugins.txt /taiga/taiga-back/plugins.txt
RUN cd /taiga/taiga-back && pip install -r plugins.txt

# Add Taiga Configuration
ADD ./local.py /taiga/taiga-back/settings/local.py

# Configure and Start scripts
ADD ./docker-entrypoint.sh /taiga/taiga-back/docker-entrypoint.sh
RUN chmod +x /taiga/taiga-back/docker-entrypoint.sh

VOLUME /taiga/media
VOLUME /taiga/static

WORKDIR /taiga/taiga-back
CMD ["./docker-entrypoint.sh"]
