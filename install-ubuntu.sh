#!/bin/bash

# echo every command and exit if any command fails
set -ex

# update in case this is done on a brand new system that has not updated
sudo apt-get update

# install so additional apt repositories can be installed
sudo apt-get install --yes software-properties-common

# add ansible apt repository and install newest Ansible
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get install --yes ansible

# install git so ansible-dotfiles can be cloned
sudo apt-get install --yes git

# clone repository if not already cloned
if [ -d ~/ansible-dotfiles ]; then
  echo "$HOME/ansible-dotfiles already cloned! Make sure it is a clone of: http://github.com/dustinspecker/ansible-dotfiles.git"
else
  git clone http://github.com/dustinspecker/ansible-dotfiles.git ~/ansible-dotfiles
fi

cd ~/ansible-dotfiles

# update origin references in case it is stale
git fetch

# do not exit if following commands return non-zero exit code
# want to store and use these exit codes
set +e

# only update local git if no local changes uncommitted
(git --no-pager diff --quiet --exit-code)
local_changed_files=$?

# only update local git if local git is not ahead of master
(($(git rev-list --right-only --count origin/master..master) == 0))
ahead_of_origin_master=$?

# go back to exiting if any command fails
set -e

# update local git if zero local changes
if [[ ${local_changed_files} -eq 0 && ${ahead_of_origin_master} -eq 0 ]]; then
  git reset --hard origin/master
else
  echo 'Local git has changes or is ahead of origin/master, so not updating local git.'
fi

# execute playbook to setup development environment
ansible-playbook -i hosts dev-env.yml --ask-become-pass "$@"

echo 'Log out and back in for shell changes to take effect'
