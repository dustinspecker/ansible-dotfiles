import os
import platform

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

go_version = '1.18'


def test_go_installed(host):
    test_cmd = '/usr/local/go/bin/go version'

    dist = platform.system().lower()
    expected_output = 'go version go%s %s/amd64' % (go_version, dist)
    assert host.check_output(test_cmd) == expected_output


def test_previous_go_files_deleted(host):
    temp_dir = host.run('mktemp --directory').stdout.strip()
    main_file_content = """package main
import "fmt"

func main() {
    fmt.Println("Hello!")
}"""
    main_file = os.path.join(temp_dir, 'main.go')
    host.run('echo %s > %s', main_file_content, main_file)
    test_cmd = 'cd %s;/usr/local/go/bin/go run main.go'
    assert host.check_output(test_cmd, temp_dir) == 'Hello!'
