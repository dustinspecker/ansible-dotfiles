Role Name
=========

Installs and configures Vim with vim-plug.

Requirements
------------

Git is required for vim-plug to install plugins.

On Mac, it is expected that homebrew has been installed.

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

    - hosts: localhost
      roles:
         - { role: vim, tags: ['vim'] }

License
-------

MIT
