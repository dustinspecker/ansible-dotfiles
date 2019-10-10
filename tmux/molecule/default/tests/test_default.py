import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

TMUX_VERSION = '2.8'
TPM_VERSION = '3.0.0'


def test_tmux_installed(host):
    assert host.check_output('tmux -V') == 'tmux %s' % TMUX_VERSION


def test_tmp_tmux_cleaned_up(host):
    assert not host.file('/tmp/tmux-%s' % TMUX_VERSION).exists


def test_xsel_installed(host):
    assert host.package('xsel').is_installed


def test_tmux_conf_copied(host):
    assert host.file('/home/ubuntu/.tmux.conf').exists


def test_tmux_package_manager_installed(host):
    cmd = 'git -C ~/.tmux/plugins/tpm describe --exact-match HEAD'
    assert host.check_output(cmd) == 'v%s' % TPM_VERSION


def test_tmux_plugins_installed(host):
    plugins_installed = '/bin/bash -c "(($(ls ~/.tmux/plugins | wc -l) > 1))"'

    assert host.run_expect([0], plugins_installed)
