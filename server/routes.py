from listeners import acquire_con, close_con
from services.views.moderator import Moderator


def add_routes(app):
    app.register_listener(acquire_con, "before_server_start")
    app.register_listener(close_con, "after_server_stop")

    app.add_route(Moderator.as_view(), 'api/approve/teams/<real_team_id:int>', methods=['PATCH'])