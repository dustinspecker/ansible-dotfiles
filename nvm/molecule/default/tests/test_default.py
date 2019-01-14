import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nvm_installed(host):
    test_cmd = 'source /home/ubuntu/.nvm/nvm.sh && nvm --version'

    assert host.run_expect([0], '/bin/bash -c "{}"'.format(test_cmd))


def test_node_installed(host):
    test_cmd = 'source /home/ubuntu/.nvm/nvm.sh && nvm use 10'

    assert host.run_expect([0], '/bin/bash -c "{}"'.format(test_cmd))
