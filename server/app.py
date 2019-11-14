import asyncio
import uvloop
import logging

import config

from sanic import Sanic
from routes import add_routes


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()

app = Sanic(__name__, load_env='DASHBOARD_')
add_routes(app)

if config.DEBUG:

    @app.middleware('response')
    async def request_log(request, response):
        logging.info(
            f'{request.method} - {request.url} - {response.status}')


if __name__ == '__main__':
    app.run(port=config.DASHBOARD_PORT,
            workers=config.DASHBOARD_WORKERS,
            debug=config.DEBUG,
            access_log=config.DASHBOARD_ACCESS_LOG)