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
    zsh_source = host.ansible(
        'raw',
        '/bin/zsh -i -o SOURCE_TRACE',
        check=False)

    expected_file_path = (
        '/home/ubuntu/.zscripts/zsh-syntax-highlighting/'
        'zsh-syntax-highlighting.zsh'
    )

    assert (expected_file_path in ''.join(zsh_source['stderr_lines']))
    assert ('no such file' not in ''.join(zsh_source['stderr_lines']))


def test_zsh_syntax_highlighting_version(host):
    expected_syntax_version = '0.7.1'

    cmd = ('git '
           '--git-dir=/home/ubuntu/.zscripts/zsh-syntax-highlighting/.git/ '
           'describe --tags')
    actual_version = host.check_output(cmd)

    assert expected_syntax_version == actual_version


def test_zsh_autosuggestion_enabled(host):
    zsh_source = host.ansible(
        'raw',
        '/bin/zsh -i -o SOURCE_TRACE',
        check=False)

    expected_file_path = (
        '/home/ubuntu/.zscripts/zsh-autosuggestions/zsh-autosuggestions.zsh'
    )

    assert (expected_file_path in ''.join(zsh_source['stderr_lines']))
    assert ('no such file' not in ''.join(zsh_source['stderr_lines']))


def test_zsh_autosuggestions_version(host):
    expected_suggestions_version = 'v0.7.0'

    cmd = ('git --git-dir=/home/ubuntu/.zscripts/zsh-autosuggestions/.git/ '
           'describe --tags')
    actual_version = host.check_output(cmd)

    assert expected_suggestions_version == actual_version


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
