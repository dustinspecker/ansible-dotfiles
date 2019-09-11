import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages_are_installed(host):
    packages = [
        'bat',
        'jq',
        'silversearcher-ag'
    ]

    for package in packages:
        assert host.package(package).is_installed
