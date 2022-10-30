Role Name
=========

Installs and configures Vim with vim-plug.

Requirements
------------

Git is required for vim-plug to install plugins.

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
         - { role: dustinspecker.vim, tags: ['vim'] }

License
-------

MIT
