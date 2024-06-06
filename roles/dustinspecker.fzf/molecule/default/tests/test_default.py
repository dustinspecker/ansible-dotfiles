import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

fzf_version = '0.53.0'


def test_fzf_cloned_and_checked_out_tag(host):
    cmd = 'git -C ~/.fzf describe --exact-match HEAD'
    assert host.check_output(cmd) == fzf_version


def test_fzf_bin_installed(host):
    cmd = "/home/ubuntu/.fzf/bin/fzf --version | awk '{ print $1 }'"
    assert host.check_output(cmd) == fzf_version


def test_fzf_completions_downloaded(host):
    assert host.file('/home/ubuntu/.fzf/shell/completion.zsh').exists


def test_fzf_key_bindings_downloaded(host):
    assert host.file('/home/ubuntu/.fzf/shell/key-bindings.zsh').exists
