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


def test_zsh_pure_prompt_is_selected(host):
    assert host.run_expect([0], '/bin/zsh -i -c "prompt -c | grep pure"')


def test_zsh_syntax_highlighting_enabled(host):
    zsh_source = host.run('/bin/zsh -i -o SOURCE_TRACE')

    expected_file_path = (
        '/home/ubuntu/.zscripts/zsh-syntax-highlighting/'
        'zsh-syntax-highlighting.zsh'
    )

    assert (expected_file_path in zsh_source.stderr)
    assert ('no such file' not in zsh_source.stderr)


def test_zsh_autosuggestion_enabled(host):
    zsh_source = host.run('/bin/zsh -i -o SOURCE_TRACE')

    expected_file_path = (
        '/home/ubuntu/.zscripts/zsh-autosuggestions/zsh-autosuggestions.zsh'
    )

    assert (expected_file_path in zsh_source.stderr)
    assert ('no such file' not in zsh_source.stderr)


def test_zsh_incremental_search_pattern_bound(host):
    backward_bind = (
        '/bin/zsh -i -c "bindkey -a | '
        'grep \'\\"/\\" history-incremental-pattern-search-backward\'"'
    )
    forward_bind = (
        '/bin/zsh -i -c "bindkey -a | '
        'grep \'\\"?\\" history-incremental-pattern-search-forward\'"'
    )

    assert host.run_expect([0], backward_bind)
    assert host.run_expect([0], forward_bind)


def test_zsh_z_tool_sourced(host):
    assert host.run_expect([0], '/bin/zsh -i -c "z --help"')


def test_zsh_hub_completions_setup(host):
    assert host.file('/home/ubuntu/.zcompletions/_hub').exists
