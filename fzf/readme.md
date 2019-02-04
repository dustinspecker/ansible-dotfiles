Role Name
=========

Installs fzf, sets up completions, and key bindings.

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

    - hosts: localhsot
      roles:
         - { role: fzf, tags: ['fzf'] }

License
-------

MIT
