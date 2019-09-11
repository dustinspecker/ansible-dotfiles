import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages_are_installed(host):
    packages = [
        {'name': 'bat', 'version': '0.9.0'},
        'jq',
        'silversearcher-ag'
    ]

    for package in packages:
        if type(package) is str:
            assert host.package(package).is_installed
        else:
            assert host.package(package['name']).is_installed
            assert host.package(package['name']).version == package['version']
