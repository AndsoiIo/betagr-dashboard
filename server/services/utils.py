import logging

from models import tb_team


async def approve_team(conn, data):
    try:
        result = await conn.execute(tb_team.update().values(real_team_id=data['real_team_id']).\
                                           where(tb_team.c.team_id == data['related_team_id']))
        if not result.rowcount:
            return False

    except Exception as e:
        logging.error(f"DB Update error: {e.__class__.__name__}: {e}", exc_info=True)
        return False
    return True