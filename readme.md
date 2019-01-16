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

1. Bat
1. Git
1. Gitk
1. hub
1. nvm
1. Tmux with (tmux package manager)
1. Vim with vim-plug
1. Zsh (with pure-prompt and z)

## How to Create New Roles

1. Scaffold via `molecule init role -r ROLE_NAME`

## How to Develop Roles

1. Navigate to role (such as git)
1. Install Docker and make sure it's running
1. Install pip
1. Install virtualenv via `pip install virtualenv`
1. Setup virtualenv via `virtualenv .venv`
1. Activate virtualenv via `source .venv/bin/activate`
1. Run `pip install molecule docker`
1. Run `molecule test` to execute tests for respective role

## License
MIT
