import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tmux_installed(host):
    assert host.package('tmux').is_installed


def test_xsel_installed(host):
    assert host.package('xsel').is_installed


def test_tmux_conf_copied(host):
    assert host.file('/home/ubuntu/.tmux.conf').exists


def test_tmux_package_manager_installed(host):
    tpm = host.file('/home/ubuntu/.tmux/plugins/tpm')

    assert tpm.exists
    assert tpm.is_directory


def test_tmux_plugins_installed(host):
    plugins_installed = '/bin/bash -c "(($(ls ~/.tmux/plugins | wc -l) > 1))"'

    assert host.run_expect([0], plugins_installed)