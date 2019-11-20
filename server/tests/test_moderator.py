import pytest


@pytest.mark.moderator
async def test_moderator_patch_valid_data(test_cli, fill_up_tables):
    data = {'related_team_id': 1}
    resp = await test_cli.patch('/api/approve/teams/1', data=data)

    assert resp.status == 204

@pytest.mark.moderator
async def test_moderator_patch_not_valid_data(test_cli, fill_up_tables):
    data = {'related_team_id': 'sss'}
    resp = await test_cli.patch('/api/approve/teams/999', data=data)
    assert resp.status == 422

    data = {'sss': 1}
    resp = await test_cli.patch('/api/approve/teams/999', data=data)
    assert resp.status == 422