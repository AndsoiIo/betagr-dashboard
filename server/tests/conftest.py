import pytest
from sanic import Sanic

from routes import add_routes
from engine import Connection, Engine
from datetime import datetime
from sqlalchemy.schema import CreateTable, DropTable
from models import tb_real_team, tb_team


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "moderator: moderator tests")


async def create_tables():
    async with Connection() as conn:
        await conn.execute(CreateTable(tb_real_team))
        await conn.execute(CreateTable(tb_team))

        await conn.execute(tb_team.insert().values(team_id=1,
                                                   name="Team A",
                                                   created_on=datetime.utcnow(),
                                                   site_name="Some site",
                                                   real_team_id=None))

        await conn.execute(tb_real_team.insert().values(real_team_id=1,
                                                        name='Real Team A',
                                                        created_on=datetime.utcnow()))

async def drop_tables():
    async with Connection() as conn:
        await conn.execute(DropTable(tb_team))
        await conn.execute(DropTable(tb_real_team))


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
async def fill_up_tables(test_cli):
    await create_tables()

    yield

    await drop_tables()

