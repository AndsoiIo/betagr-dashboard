from sanic.exceptions import abort
from sanic.views import HTTPMethodView
from sanic.response import text

from services.form import ApproveTeamSchema
from marshmallow.exceptions import ValidationError

from engine import Connection
from services.utils import approve_team


class Moderator(HTTPMethodView):
    async def patch(self, request, real_team_id, *args, **kwargs):
        try:
            data = ApproveTeamSchema().load(request.form)
            data['real_team_id'] = real_team_id

        except ValidationError as e:
            return text(e, 400)
        else:
            async with Connection() as conn:
                if not await approve_team(conn, data):
                    return text("Unprocessable Entity", 422)
                return text("Ok", 204)