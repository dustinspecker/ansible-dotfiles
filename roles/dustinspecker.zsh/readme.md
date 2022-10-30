Role Name
=========

Installs and configures zsh. Sets user's default shell to /bin/zsh. Sets up pure prompt and z.

Requirements
------------

Git must be installed for zsh-syntax-highlighting to be installed.

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
         - { role: dustinspecker.zsh, tags: ['zsh'] }

License
-------

MIT
