import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hub_installed(host):
    test_cmd = 'hub --version | grep hub'

    assert host.check_output(test_cmd) == 'hub version 2.7.0'
