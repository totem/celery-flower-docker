#!/bin/sh -e

# Defaults
export LOG_LEVEL="${LOG_LEVEL:-info}"
export HOST_IP="${HOST_IP:-$(/sbin/ip route|awk '/default/ { print $3 }')}"
export AMQP_HOST="${AMQP_HOST:-$HOST_IP}"
export AMQP_ADMIN_HOST="${AMQP_ADMIN_HOST:-$HOST_IP}"
export DISCOVER_RABBITMQ="${DISCOVER_RABBITMQ:-false}"
export ETCD_HOST="${ETCD_HOST:-$HOST_IP}"
export ETCD_PORT="${ETCD_PORT:-4001}"
export ETCD_URL="${ETCD_URL:-http://$ETCD_HOST:$ETCD_PORT}"
export ETCDCTL="${ETCDCTL:-etcdctl --peers $ETCD_URL}"
export ETCD_TOTEM_BASE="${ETCD_TOTEM_BASE:-/totem}"

if [ "$DISCOVER_RABBITMQ" == "true" ]; then
  until $ETCDCTL cluster-health; do
    >&2 echo "Etcdctl cluster not healthy - sleeping"
    sleep 10
  done

  export AMQP_HOST="$($ETCDCTL ls $ETCD_TOTEM_BASE/rabbitmq/nodes | xargs -n 1  $ETCDCTL get | xargs echo -n | tr ' ' ',')"
  until [ ! -z "$AMQP_HOST" ]; do
    >&2 echo "Rabbitmq could not be discovered - sleeping"
    sleep 10
    export AMQP_HOST="$($ETCDCTL ls $ETCD_TOTEM_BASE/rabbitmq/nodes | xargs -n 1  $ETCDCTL get | xargs echo -n | tr ' ' ',')"
  done
fi

/usr/local/bin/celery --loglevel="$LOG_LEVEL" flower
