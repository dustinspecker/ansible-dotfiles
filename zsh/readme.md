Role Name
=========

Installs and configures zsh. Sets user's default shell to /bin/zsh. Sets up pure prompt.

Requirements
------------

On Mac, it is expected for homebrew to be installed.

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
         - { role: zsh, tags: ['zsh'] }

License
-------

MIT
