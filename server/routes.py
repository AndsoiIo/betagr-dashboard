from listeners import acquire_con, close_con
from services.views.change_status_team import moderate_team, approve_team


def add_routes(app):
    app.register_listener(acquire_con, "before_server_start")
    app.register_listener(close_con, "after_server_stop")

    app.add_route(moderate_team, 'api/moderate-team/<related_team_id:int>', methods=['PATCH'])
    app.add_route(approve_team, 'api/approve-team/<related_team_id:int>', methods=['PATCH'])
