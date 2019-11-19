#!/bin/bash
set -ex

if ! [ -x "$(command -v http)" ]; then
  echo "Error: httpie must be installed" >&2
  exit 1
fi

if ! [ -x "$(command -v jq)" ]; then
  echo "Error: jq must be installed" >&2
  exit 1
fi

update_version() {
  local url="$1"
  local jqFilter="$2"
  local vars_file="$3"
  local test_file="$4"

  local upper_repo_name
  upper_repo_name="$(echo "$repo_name" | tr '[:lower:]' '[:upper:]')"

  latest_version=$(http "$url"| jq -crM "$jqFilter" | sed 's/^v//')

  sed -Ei.bak "s/(${upper_repo_name}_VERSION: ).*/\1$latest_version/g" "$vars_file"
  sed -Ei.bak "s/(${upper_repo_name}_VERSION = ').*/\1$latest_version'/g" "$test_file"
}

update_version_via_releases() {
  local github_org="$1"
  local repo_name="$2"
  local vars_file="$3"
  local test_file="$4"

  local upper_repo_name
  upper_repo_name="$(echo "$repo_name" | tr '[:lower:]' '[:upper:]')"

  url="https://api.github.com/repos/$github_org/$repo_name/releases"
  jqFilter="first(.[] | select(.prerelease == false)) | .tag_name"

  update_version "$url" "$jqFilter" "$vars_file" "$test_file"
}

update_version_via_tags() {
  local github_org="$1"
  local repo_name="$2"
  local vars_file="$3"
  local test_file="$4"

  local upper_repo_name
  upper_repo_name="$(echo "$repo_name" | tr '[:lower:]' '[:upper:]')"

  url="https://api.github.com/repos/$github_org/$repo_name/tags"
  jqFilter="first(.[]) | .name"

  update_version "$url" "$jqFilter" "$vars_file" "$test_file"
}

update_version_via_tags "junegunn" "fzf" fzf/vars/main.yml fzf/molecule/default/tests/test_default.py
update_version_via_tags "github" "hub" hub/vars/main.yml hub/molecule/default/tests/test_default.py
update_version_via_tags "nvm-sh" "nvm" nvm/vars/main.yml nvm/molecule/default/tests/test_default.py
update_version_via_tags "nodejs" "node" nvm/vars/main.yml nvm/molecule/default/tests/test_default.py
update_version_via_tags "sharkdp" "bat" packages-system/tasks/main.yml packages-system/molecule/default/tests/test_default.py
update_version_via_tags "sharkdp" "fd" packages-system/tasks/main.yml packages-system/molecule/default/tests/test_default.py
update_version_via_releases "tmux" "tmux" tmux/vars/main.yml tmux/molecule/default/tests/test_default.py
