# ansible-dotfiles

> I DevOps'd my dotfiles

[![Build Status](https://travis-ci.org/dustinspecker/ansible-dotfiles.svg?branch=master)](https://travis-ci.org/dustinspecker/ansible-dotfiles)

## Usage (Ubuntu only)

If you're comfortable piping `wget` output to `bash`, you may do the following:

```bash
wget -O - https://raw.githubusercontent.com/dustinspecker/ansible-dotfiles/master/install-ubuntu.sh | bash
```

This will install `ansible`, fetch this repository, and execute the playbook.

## Manual Usage

1. Install `ansible-playbook`
   - [Mac](https://hvops.com/articles/ansible-mac-osx/)
   - [Ubuntu](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#latest-releases-via-apt-ubuntu)
1. Clone this git repository
1. Navigate to the cloned repository
1. `ansible-playbook -i hosts dev-env.yml --ask-become-pass`

## Sets Up

1. fzf
1. Git (with gitk)
1. go
1. hub
1. nvm
1. packages_system
   - bat
   - fd
   - jq
   - silversearcher-ag
   - tree
1. Tmux with (tmux package manager)
1. Vim with vim-plug
1. Zsh (with pure-prompt and z)

## How to Develop Roles

1. Install Docker and make sure it's running
1. Install [pipenv](https://github.com/pypa/pipenv#installation)
  - `python3.8 -m pip install pipenv==2020.11.15`
1. Navigate to ansible-dotfiles directory
1. Run `pipenv sync --dev` to install dependencies
1. Run `pipenv shell` to activate a virtualenv
1. Navigate to role (such as git)
1. Run `molecule test` to execute tests for respective role

## How to Update Versions

1. Install Docker and make sure it's running
1. Install [pipenv](https://github.com/pypa/pipenv#installation)
1. Navigate to ansible-dotfiles directory
1. Run `pipenv sync --dev` to install dependencies
1. Run `pipenv shell` to activate a virtualenv
1. Run `./update-versions.sh`

## How to Create New Roles

1. Scaffold via `molecule init role -r ROLE_NAME`

## License
MIT
