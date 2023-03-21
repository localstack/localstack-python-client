from localstack_client import config


def test_default_endpoint():
    assert config.get_service_endpoint("sqs") == "http://localhost:4566"


def test_with_localstack_host(monkeypatch):
    monkeypatch.setenv("LOCALSTACK_HOST", "foobar:9999")
    assert config.get_service_endpoint("sqs") == "http://foobar:9999"
