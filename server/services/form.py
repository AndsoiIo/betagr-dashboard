from marshmallow import Schema, fields, validate


class ApproveTeamSchema(Schema):
    real_team_id = fields.Int(required=True)
