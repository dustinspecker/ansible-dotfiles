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
  local repo_name="$1"
  local url="$2"
  local jqFilter="$3"
  local vars_file="$4"
  local test_file="$5"

  local upper_repo_name
  upper_repo_name="$(echo "$repo_name" | tr '[:lower:]' '[:upper:]')"

  latest_version=$(http "$url"| jq -crM "$jqFilter" | sed 's/^v//')

  sed -Ei.bak "s/(${upper_repo_name}_VERSION: ).*/\1$latest_version/g" "$vars_file"
  sed -Ei.bak "s/(${upper_repo_name}_VERSION = ').*/\1$latest_version'/g" "$test_file"

  role=$(echo "$vars_file" | awk -F/ '{ print $1 }')

  if [ "$(git status --short "$role" | wc --lines)" -ne 0 ]; then
    make ROLE="$role" test

    git add "$role"
    git commit --message="feat($role): update $repo_name to $latest_version"
  fi
}

update_version_via_releases() {
  local github_org="$1"
  local repo_name="$2"
  local vars_file="$3"
  local test_file="$4"

  url="https://api.github.com/repos/$github_org/$repo_name/releases"
  jqFilter="first(.[] | select(.prerelease == false)) | .tag_name"

  update_version "$repo_name" "$url" "$jqFilter" "$vars_file" "$test_file"
}

update_version_via_tags() {
  local github_org="$1"
  local repo_name="$2"
  local vars_file="$3"
  local test_file="$4"

  url="https://api.github.com/repos/$github_org/$repo_name/tags"
  jqFilter="first(.[]) | .name"

  update_version "$repo_name" "$url" "$jqFilter" "$vars_file" "$test_file"
}

update_version_via_tags "junegunn" "fzf" fzf/vars/main.yml fzf/molecule/default/tests/test_default.py
update_version_via_tags "github" "hub" hub/vars/main.yml hub/molecule/default/tests/test_default.py
update_version_via_tags "nvm-sh" "nvm" nvm/vars/main.yml nvm/molecule/default/tests/test_default.py
update_version_via_tags "nodejs" "node" nvm/vars/main.yml nvm/molecule/default/tests/test_default.py
update_version_via_tags "sharkdp" "bat" packages_system/vars/main.yml packages_system/molecule/default/tests/test_default.py
update_version_via_tags "sharkdp" "fd" packages_system/vars/main.yml packages_system/molecule/default/tests/test_default.py
update_version_via_releases "tmux" "tmux" tmux/vars/main.yml tmux/molecule/default/tests/test_default.py
