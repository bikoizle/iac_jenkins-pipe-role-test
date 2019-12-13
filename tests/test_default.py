def test_os_release_file(host):
    f = host.file('/etc/os-release')
    assert f.exists
