import asyncio

import pytest
from sanic import Sanic

from routes import add_routes
from engine import Engine


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "moderate: moderate tests")
    config.addinivalue_line("markers", "approve: approve tests")


@pytest.fixture
def test_cli(loop, sanic_client):
    app = Sanic('test_dashboard_app')
    add_routes(app)
    return loop.run_until_complete(sanic_client(app))


@pytest.fixture
async def connection():
    await Engine.init()

    yield

    await Engine.close()


@pytest.fixture
async def mock_resp(test_cli):
    class Empty:
        status = 200
        json = "Ok"

    future = asyncio.Future()
    future.set_result(Empty())
    return future
