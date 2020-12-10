#!/bin/bash
set -x

if [ -z "$ROLE" ]; then
  echo "ROLE must be set" >&2
  exit 1
fi

COMMIT_RANGE="${COMMIT_RANGE:-origin/master..HEAD}"

git diff --name-only "${COMMIT_RANGE}" | grep --extended-regexp "$ROLE|Pipfile|Makefile"
