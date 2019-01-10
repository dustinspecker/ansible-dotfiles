import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zshrc_installed(host):
    assert host.package('zsh').is_installed


def test_zshrc_copied(host):
    assert host.file('/home/ubuntu/.zshrc').exists


def test_zshrc_is_user_default_shell(host):
    assert host.user('ubuntu').shell == '/bin/zsh'
