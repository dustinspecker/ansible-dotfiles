#!/bin/bash

if ! [ -x "$(command -v http)" ]; then
  echo "Error: httpie must be installed" >&2
  exit 1
fi

if ! [ -x "$(command -v jq)" ]; then
  echo "Error: jq must be installed" >&2
  exit 1
fi

update_version() {
  local github_org="$1"
  local repo_name="$2"

  local upper_repo_name
  upper_repo_name="$(echo "$repo_name" | tr '[:lower:]' '[:upper:]')"

  latest_version=$(http "https://api.github.com/repos/$github_org/$repo_name/releases" | jq -crM 'first(.[]) | .tag_name' | sed 's/^v//')

  sed -Ei.bak "s/(${upper_repo_name}_VERSION: ).*/\1$latest_version/g" packages-system/tasks/debian.yml
  sed -Ei.bak "s/(${upper_repo_name}_VERSION = ').*/\1$latest_version'/g" packages-system/molecule/default/tests/test_default.py
}

update_version "sharkdp" "bat"
update_version "sharkdp" "fd"
