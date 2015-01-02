# ansible-role-apt-cacher-ng
[![Build Status](https://travis-ci.org/elnappo/ansible-role-quassel-core.svg)](https://travis-ci.org/elnappo/ansible-role-quassel-core)

Simply installs and start quassel-core on boot. Get more informations about Quassel at [http://quassel-irc.org/]()

## Requirements
Ubuntu or Debian

## Role Variables
* `quassel-core_port: 4242`: Port to bind quassel-core
* `quassel-core_setup_ufw: True`: Add a ufw rule to allow `quassel-core_port` port

## Dependencies
None.

## Example Playbook
    - hosts: servers
      roles:
         - { role: elnappoo.quassel-core }

## Client configuration
Take a look at the Quassel Docs [http://bugs.quassel-irc.org/projects/quassel-irc/wiki]()

## License
MIT

## Author Information
elnappo <elnappoo@gmail.com>
