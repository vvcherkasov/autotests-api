import pytest

from clients.authentication.authentication_client import get_authentication_client, AuthClient

@pytest.fixture
def authentication_client() -> AuthClient:
    return get_authentication_client()
