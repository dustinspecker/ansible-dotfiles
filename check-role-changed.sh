#!/bin/bash
set -x

if [ -z "$ROLE" ]; then
  echo "ROLE must be set" >&2
  exit 1
fi

git diff --name-only "${TRAVIS_COMMIT_RANGE:-HEAD^}" | grep --extended-regexp "$ROLE|Pipfile|Makefile"
