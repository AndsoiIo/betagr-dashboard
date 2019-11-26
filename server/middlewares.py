import logging

from app import app
from common.rest_client.base_client_sso import BaseClientSSO


@app.middleware('request')
async def is_authorized(request):
    logging.debug('Authorization requests:', request)
    sso = BaseClientSSO()
    if await sso.is_permission_granted(cookies=request.cookies, permission='Admin').status == 200:
        permission = 'special'
    elif await sso.is_permission_granted(cookies=request.cookies, permission='Moderator').status == 200:
        permission = 'moderate'
    else:
        permission = 'view'

    request.headers['User permission'] = permission
