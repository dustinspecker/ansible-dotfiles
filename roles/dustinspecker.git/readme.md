Role Name
=========

Installs and configures Git.

Requirements
------------

On Mac, it is expected that homebrew has been installed.

diff-so-fancy is required to be installed.

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
         - { role: dustinspecker.git, tags: ['git'] }

License
-------

MIT
