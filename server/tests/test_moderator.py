import pytest


@pytest.mark.moderator
async def test_moderator_patch_valid_data(test_cli, fill_up_tables):
    data = {'related_team_id': 1}
    resp = await test_cli.patch('/api/approve/teams/1', data=data)

    assert resp.status == 204

@pytest.mark.moderator
async def test_moderator_patch_not_valid_data(test_cli, fill_up_tables):
    data = {'related_team_id': '1'}
    resp = await test_cli.patch('/api/approve/teams/999', data=data)

    assert resp.status == 422

@pytest.mark.moderator
async def test_moderator_patch_id_is_not_present(test_cli, fill_up_tables):
    data = {'related_team_id': 1}
    # real team id is not present in table
    resp = await test_cli.patch('/api/approve/teams/666', data=data)
    assert resp.status == 422
    # related team id is not present in table
    data['related_team_id'] = 666
    resp = await test_cli.patch('/api/approve/teams/1', data=data)
    assert resp.status == 422
