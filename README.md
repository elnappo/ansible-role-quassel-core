# ansible-role-quassel-core
[![Build Status](https://travis-ci.org/elnappo/ansible-role-quassel-core.svg)](https://travis-ci.org/elnappo/ansible-role-quassel-core) [![Ansible Galaxy](https://img.shields.io/badge/galaxy-elnappo.quassel--core-blue.svg?style=flat)](https://galaxy.ansible.com/elnappo/quassel-core/)

Simply installs and start quassel-core on boot. Get more information about Quassel at [http://quassel-irc.org/]().

## Requirements

Ubuntu or Debian

## Role Variables

* `quasselcore_use_ppa: true`
* `quasselcore_setup_ufw: true` Add a ufw rule to allow port 4242

## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  remote_user: root
  roles:
     - elnappo.quassel_core
```

## Client configuration

Take a look at the Quassel docs [http://bugs.quassel-irc.org/projects/quassel-irc/wiki]()

## License

MIT

## Author Information

elnappo <elnappo@nerdpol.io>
