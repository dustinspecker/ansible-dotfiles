#!/bin/bash
set -ex

docker run \
  --env LOG_LEVEL=debug \
  --rm \
  renovate/renovate:37.382.3 \
  --token "$(gh auth token)" \
  dustinspecker/ansible-dotfiles
