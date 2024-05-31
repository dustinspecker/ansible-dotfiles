import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

bat_version = '0.24.0'
fd_version = '8.4.0'
shellcheck_version = '0.8.0'


def test_packages_are_installed(host):
    packages = [
        {'name': 'bat', 'version': bat_version},
        {'name': 'fd', 'version': fd_version},
        'httpie',
        'jq',
        'silversearcher-ag',
        'tree'
    ]

    for package in packages:
        if type(package) is str:
            assert host.package(package).is_installed
        else:
            assert host.package(package['name']).is_installed
            assert host.package(package['name']).version == package['version']


def test_executables_are_installed(host):
    executables = [
        {
            'name': 'shellcheck',
            'test_cmd': 'shellcheck --version',
            'expected_version_output': 'version: 0.8.0'
        }
    ]

    for executable in executables:
        test_cmd = executable['test_cmd']
        expected_version_output = executable['expected_version_output']
        assert expected_version_output in host.check_output(test_cmd)
