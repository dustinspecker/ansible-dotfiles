import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages_are_installed(host):
    assert host.package('bat').is_installed
    assert host.package('jq').is_installed
    assert host.package('silversearcher-ag').is_installed
