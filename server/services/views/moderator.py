from sanic.views import HTTPMethodView
from sanic.response import json

from services.form import ApproveTeamSchema
from marshmallow.exceptions import ValidationError
from common.rest_client.base_client_parser import BaseClientParser


class Moderator(HTTPMethodView):
    async def patch(self, request, related_team_id, *args, **kwargs):
        if request.headers.get('User permission') == 'view':
            return json('Forbidden', 403)

        try:
            data = ApproveTeamSchema().load(request.json)
        except ValidationError as e:
            return json(e.messages, 422)

        data['User permission'] = request.headers.get('User permission', 'view')

        parser_client = BaseClientParser()
        response = await parser_client.approve_team(team_id=related_team_id, data=data)

        return json(response.reason, response.status)
