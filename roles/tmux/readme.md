Role Name
=========

Installs and configures Tmux with TPM.

Requirements
------------

On Mac, it is expected that homebrew has been installed.

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: tmux, tags: ['tmux'] }

License
-------

MIT
