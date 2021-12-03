import os
import platform

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

GO_VERSION = '1.17.4'


def test_go_installed(host):
    test_cmd = '/usr/local/go/bin/go version'

    dist = platform.system().lower()
    expected_output = 'go version go%s %s/amd64' % (GO_VERSION, dist)
    assert host.check_output(test_cmd) == expected_output
