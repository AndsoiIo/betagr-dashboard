from http import HTTPStatus
from unittest import mock

import pytest

from common.rest_client.base_client_sso import BaseClientSSO


from common.rest_client.base_client_betting_data import BaseClientBettingData


@pytest.mark.moderate
async def test_moderate_patch_valid_data(test_cli, mock_resp):
    with mock.patch.object(BaseClientSSO, 'check_auth_and_user_has', return_value=mock_resp):
        with mock.patch.object(BaseClientBettingData, 'change_status_team', return_value=mock_resp):
            resp = await test_cli.patch('/api/moderate-team/1', json={"real_team_id": 1})

            assert resp.status == HTTPStatus.OK
            assert await resp.json() == "Ok"


@pytest.mark.moderate
async def test_moderate_patch_not_valid_data(test_cli, mock_resp):
    with mock.patch.object(BaseClientSSO, 'check_auth_and_user_has', return_value=mock_resp):
        with mock.patch.object(BaseClientBettingData, 'change_status_team', return_value=mock_resp):
            resp = await test_cli.patch('/api/moderate-team/1', json={"wrong_key": 1})

            assert resp.status == HTTPStatus.UNPROCESSABLE_ENTITY
            assert await resp.json() == {'real_team_id': ['Missing data for required field.'],
                                         'wrong_key': ['Unknown field.']}

            resp = await test_cli.patch('/api/moderate-team/1', json={"real_team_id": "wrong_type_value"})

            assert resp.status == HTTPStatus.UNPROCESSABLE_ENTITY
            assert await resp.json() == {'real_team_id': ['Not a valid integer.']}
