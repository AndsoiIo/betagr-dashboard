from marshmallow import Schema, fields, validate


class ChangeStatusTeamSchema(Schema):
    real_team_id = fields.Int(required=True)
    status = permission = fields.Str(validate=validate.OneOf(["moderated", "approved"]))
