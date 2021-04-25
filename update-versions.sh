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

  role=$(echo "$vars_file" | awk -F/ '{ print $2 }' | sed 's/dustinspecker\.//')

  if [ "$(git status --short "roles/dustinspecker.$role" | wc --lines)" -ne 0 ]; then
    make ROLE="$role" test

    git add "roles/dustinspecker.$role"
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

update_version_via_tags "junegunn" "fzf" roles/dustinspecker.fzf/vars/main.yml roles/dustinspecker.fzf/molecule/default/tests/test_default.py
update_version_via_tags "github" "hub" roles/dustinspecker.hub/vars/main.yml roles/dustinspecker.hub/molecule/default/tests/test_default.py
update_version_via_tags "nvm-sh" "nvm" roles/dustinspecker.nvm/vars/main.yml roles/dustinspecker.nvm/molecule/default/tests/test_default.py
update_version_via_tags "nodejs" "node" roles/dustinspecker.nvm/vars/main.yml roles/dustinspecker.nvm/molecule/default/tests/test_default.py
update_version_via_tags "sharkdp" "bat" roles/dustinspecker.packages_system/vars/main.yml roles/dustinspecker.packages_system/molecule/default/tests/test_default.py
update_version_via_tags "sharkdp" "fd" roles/dustinspecker.packages_system/vars/main.yml roles/dustinspecker.packages_system/molecule/default/tests/test_default.py
update_version_via_releases "tmux" "tmux" roles/dustinspecker.tmux/vars/main.yml roles/dustinspecker.tmux/molecule/default/tests/test_default.py
