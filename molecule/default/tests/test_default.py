import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_quasselcore_server_is_installed(host):
    quasselcore = host.package('quassel-core')

    assert quasselcore.is_installed


def test_quasselcore_is_running(host):
    quasselcore = host.service('quasselcore')

    assert quasselcore.is_running
    assert quasselcore.is_enabled


def test_quasselcore_is_listening(host):
    assert host.socket("tcp://0.0.0.0:4242").is_listening
