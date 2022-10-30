import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

bat_version = '0.22.1'
fd_version = '8.4.0'


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
