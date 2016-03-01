# ansible-role-quassel-core [![Build Status](https://travis-ci.org/elnappo/ansible-role-quassel-core.svg)](https://travis-ci.org/elnappo/ansible-role-quassel-core)

Simply installs and start quassel-core on boot. Get more informations about Quassel at [http://quassel-irc.org/]()

## Requirements
Ubuntu or Debian

## Role Variables
* `quasselcore_port: 4242`: Port to bind quassel-core
* `quasselcore_setup_ufw: True`: Add a ufw rule to allow `quasselcore_port` port

## Dependencies
None.

## Example Playbook

```yaml
- hosts: servers
  remote_user: root
  roles:
     - { role: elnappoo.quassel-core }
```

## Client configuration
Take a look at the Quassel Docs [http://bugs.quassel-irc.org/projects/quassel-irc/wiki]()

## License

MIT

## Author Information

elnappo <elnappo@nerdpol.io>
