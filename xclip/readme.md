Role Name
=========

Installs xclip on Debian-based systems. This is needed for vim-fakeclip to work on Debian.

Requirements
------------

None

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
         - { role: xclip, tags: ['xclip'] }

License
-------

MIT
