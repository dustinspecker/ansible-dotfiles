#!/bin/bash

if ! [ -x "$(command -v http)" ]; then
  echo "Error: httpie must be installed" >&2
  exit 1
fi

if ! [ -x "$(command -v jq)" ]; then
  echo "Error: jq must be installed" >&2
  exit 1
fi

update_version_via_tags() {
  local github_org="$1"
  local repo_name="$2"
  local task_file="${3:-packages-system/tasks/debian.yml}"
  local test_file="${4:-packages-system/molecule/default/tests/test_default.py}"

  local upper_repo_name
  upper_repo_name="$(echo "$repo_name" | tr '[:lower:]' '[:upper:]')"

  latest_version=$(http "https://api.github.com/repos/$github_org/$repo_name/tags" | jq -crM 'first(.[]) | .name' | sed 's/^v//')

  sed -Ei.bak "s/(${upper_repo_name}_VERSION: ).*/\1$latest_version/g" "$task_file"
  sed -Ei.bak "s/(${upper_repo_name}_VERSION = ').*/\1$latest_version'/g" "$test_file"
}

update_version_via_tags "junegunn" "fzf" fzf/vars/main.yml fzf/molecule/default/tests/test_default.py
update_version_via_tags "github" "hub" hub/vars/main.yml hub/molecule/default/tests/test_default.py
update_version_via_tags "nvm-sh" "nvm" nvm/vars/main.yml nvm/molecule/default/tests/test_default.py
update_version_via_tags "nodejs" "node" nvm/vars/main.yml nvm/molecule/default/tests/test_default.py
update_version_via_tags "sharkdp" "bat"
update_version_via_tags "sharkdp" "fd"
