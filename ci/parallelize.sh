#!/bin/bash
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

case "$CIRCLE_NODE_INDEX" in
  0)
    ${DIR}/release.sh 1
    ;;
  1)
    ${DIR}/release.sh 2
    ;;
  2)
    ${DIR}/release.sh 3
    ;;
esac
