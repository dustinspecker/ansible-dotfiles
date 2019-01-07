# ansible-dotfiles

> I DevOps'd my dotfiles

## Usage

1. Install `ansible-playbook`
1. Clone this git repository
1. Navigate to the cloned repository
1. `ansible-playbook -i hosts dev-env.yml --ask-become-pass`

## Sets Up

1. Git
1. Gitk
1. Vim with vim-plug

## How to Create New Roles

1. Scaffold via `molecule init -r ROLE_NAME`

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
