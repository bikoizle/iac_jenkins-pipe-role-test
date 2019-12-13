import pytest


def test_os_release_file(host):
    f = host.file('/etc/os-release')
    assert f.exists


def test_firewalld_service_is_active_and_enabled(host):
    assert host.service("firewalld").is_running
    assert host.service("firewalld").is_enabled
