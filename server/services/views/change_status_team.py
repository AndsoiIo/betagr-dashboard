from http import HTTPStatus

from sanic.response import json
from marshmallow.exceptions import ValidationError
from common.rest_client.base_client_betting_data import BaseClientBettingData
from common.utils.decorators import authorized_and_user_has

from services.forms import ModerateTeamSchema

client = BaseClientBettingData()


@authorized_and_user_has("moderate")
async def moderate_team(request, related_team_id):
    request.json["status"] = "moderated"
    try:
        data = ModerateTeamSchema().load(request.json)
    except ValidationError as e:
        return json(e.messages, HTTPStatus.UNPROCESSABLE_ENTITY)
    response = await client.change_status_team(team_id=related_team_id, json=data)
    return json(response.json, response.status)


@authorized_and_user_has("approve")
async def approve_team(request, related_team_id):
    response = await client.change_status_team(team_id=related_team_id, json={"status": "approved"})
    return json(response.json, response.status)
