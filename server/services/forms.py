from marshmallow import Schema, fields, validate


class ModerateTeamSchema(Schema):
    real_team_id = fields.Int(required=True)
    status = fields.Str(validate=validate.OneOf(["moderated"]))
