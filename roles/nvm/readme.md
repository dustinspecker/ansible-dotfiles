Role Name
=========

Installs nvm and node 10.

Requirements
------------

User will need to source ~/.nvm/nvm.sh to use nvm.

Requires git and wget to be installed.

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
         - { role: nvm, tags: ['nvm'] }

License
-------

MIT
