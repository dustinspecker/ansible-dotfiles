import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_apt_repo_setup(host):
    assert host.file('/etc/apt/sources.list.d/git.list').exists


def test_git_installed(host):
    assert host.package('git').is_installed
    assert host.package('gitk').is_installed
    assert host.package('tig').is_installed


def test_gitconfig_copied(host):
    assert host.file('/home/ubuntu/.gitconfig').exists


def test_git_gerrit_not_cloned(host):
    assert not host.file('/home/ubuntu/git-gerrit/git-gerrit').exists
