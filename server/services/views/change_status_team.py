from sanic.response import json
from marshmallow.exceptions import ValidationError
from common.rest_client.base_client_parser import BaseClientParser
from common.utils.decorators import authorized_and_user_has

from services.form import ChangeStatusTeamSchema

parser_client = BaseClientParser()


@authorized_and_user_has("moderate")
async def moderate_team(request, related_team_id):
    request.json["status"] = "moderated"
    try:
        data = ChangeStatusTeamSchema().load(request.json)
    except ValidationError as e:
        return json(e.messages, 422)
    response = await parser_client.change_status_team(team_id=related_team_id, json=data)
    return json(response.json, response.status)


@authorized_and_user_has("approve")
async def approve_team(request, related_team_id):
    request.json["status"] = "approved"
    try:
        data = ChangeStatusTeamSchema().load(request.json)
    except ValidationError as e:
        return json(e.messages, 422)

    response = await parser_client.change_status_team(team_id=related_team_id, json=data)

    return json(response.json, response.status)
