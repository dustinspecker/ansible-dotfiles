import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fzf_cloned_and_checked_out_tag(host):
    cmd = 'git -C ~/.fzf describe --exact-match HEAD'
    FZF_VERSION = '0.17.5'
    assert host.check_output(cmd) == FZF_VERSION


def test_fzf_installed(host):
    assert host.file('/home/ubuntu/.fzf/bin/fzf').exists


def test_fzf_completions_downloaded(host):
    assert host.file('/home/ubuntu/.fzf/shell/completion.zsh').exists


def test_fzf_key_bindings_downloaded(host):
    assert host.file('/home/ubuntu/.fzf/shell/key-bindings.zsh').exists
