from sanic.exceptions import abort
from sanic.views import HTTPMethodView
from sanic.response import json
import json as json_build_in

from services.form import ApproveTeamSchema
from marshmallow.exceptions import ValidationError
from common.rest_client.base_client_parser import BaseClientParser


class Moderator(HTTPMethodView):
    async def patch(self, request, related_team_id, *args, **kwargs):
        try:
            data = ApproveTeamSchema().load(request.json)
        except ValidationError as e:
            return json(e.messages, 422)

        parser_client = BaseClientParser()
        response = await parser_client.patch(api_uri=f'approve-team/{related_team_id}', data=data)

        return json(response.json)

