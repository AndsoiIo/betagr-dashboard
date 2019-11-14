from marshmallow import Schema, fields, validate


class ApproveTeamSchema(Schema):
    related_team_id = fields.Int(required=True)
