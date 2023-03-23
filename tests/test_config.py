from localstack_client import config


def test_default_endpoint():
    assert config.get_service_endpoint("sqs") == "http://localhost:4566"


def test_with_localstack_host(monkeypatch):
    monkeypatch.setenv("LOCALSTACK_HOST", "foobar:9999")
    assert config.get_service_endpoint("sqs") == "http://foobar:9999"


def test_without_port(monkeypatch):
    monkeypatch.setenv("LOCALSTACK_HOST", "foobar")
    assert config.get_service_endpoint("sqs") == "http://foobar:4566"


def test_without_host(monkeypatch):
    monkeypatch.setenv("LOCALSTACK_HOST", ":4566")
    assert config.get_service_endpoint("sqs") == "http://localhost:4566"
