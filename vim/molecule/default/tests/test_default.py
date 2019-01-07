import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vim_apt_repo_setup(host):
    assert host.file('/etc/apt/sources.list.d/vim.list').exists


def test_vim_installed(host):
    assert host.package('vim').is_installed


def test_vimrc_copied(host):
    assert host.file('/home/ubuntu/.vimrc').exists


def test_vim_plug_installed(host):
    assert host.file('/home/ubuntu/.vim/autoload/plug.vim').exists


def test_vim_plugins_installed(host):
    assert host.file('/home/ubuntu/.vim/plugged').exists
