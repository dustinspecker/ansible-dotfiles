import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

NODE_VERSION = '13.2.0'
NVM_VERSION = '0.35.1'


def test_nvm_installed(host):
    test_cmd = 'source /home/ubuntu/.nvm/nvm.sh && nvm --version'

    version = host.check_output('/bin/bash -c "{}"'.format(test_cmd))

    assert version == NVM_VERSION


def test_nvm_install_deleted(host):
    assert not host.file('/tmp/nvm-install.sh').exists


def test_node_installed(host):
    test_cmd = 'source /home/ubuntu/.nvm/nvm.sh && nvm use "{}"' \
        .format(NODE_VERSION)

    assert host.run_expect([0], '/bin/bash -c "{}"'.format(test_cmd))


def test_npm_packages_installed(host):
    packages = ['diff-so-fancy']

    source_nvm = 'source /home/ubuntu/.nvm/nvm.sh && '
    for package in packages:
        npm_ls = 'npm list --depth 1 --global {}'.format(package)

        test_cmd = source_nvm + npm_ls

        assert host.run_expect([0], '/bin/bash -c "{}"'.format(test_cmd))
