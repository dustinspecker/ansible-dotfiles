#!/bin/bash

if [ -z "$ROLE" ]; then
  echo "ROLE must be set" >&2
  exit 1
fi

git diff --name-only | grep "$ROLE"
