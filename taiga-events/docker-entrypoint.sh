#!/bin/sh

cat > ./config.json << EOF
{
    "url": "${EVENT_AMQP_URL}",
    "secret": "${SECRET_KEY}",
    "webSocketServer": {
        "port": ${EVENT_PORT:-8888}
    }
}
EOF

coffee index.coffee
