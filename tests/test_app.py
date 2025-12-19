from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)  # toda vez que uma funcao de teste receber um parametro chamado 'client'
                            # ele vai executar essa função e vai passar o retorno dela para nosso teste


def test_read_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo'}  # Assert


def test_create_user(client):

    response = client.post('/users/', json={
        'username': 'testusername',
        'password': 'password',
        'email': 'test@test.com',
    }
    )  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1}

    def test_read_users(client):
        client.get('/users')

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {'users': [
            {
                'username': 'testusername1',
                'email': 'test@test1.com',
                'id': 1,
            }
        ]
        }


def test_update_user(client):
        response = client.put('/users/1', json={
                'password': '123',
                'username': 'testusername2',
                'email': 'test@test.com',
                'id': 1,
                }
            )
        assert response.json() == {
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        }


def test_delete_user(client):
     response = client.delete('/users/1')
     assert response.json() == {'message': 'User deleted'}


def test_not_found_put(client):
     response = client.put('/users/5',
                           json={'username': 'joao',
                                 'email': 'joao@email.com',
                                 'password': '111senha'})
     assert response.status_code == HTTPStatus.NOT_FOUND
     assert response.json() == {'detail': 'User not found'}


def test_not_found_delete(client):
     response = client.delete('/users/8')
     assert response.status_code == HTTPStatus.NOT_FOUND
     assert response.json() == {'detail': 'User not found'}


def test_get_user_by_id(client):
     response = client.get('/users/1')

     assert response.status_code == HTTPStatus.OK
     assert response.json() == {'username': 'matheus',
                                 'email': 'math@email.com',
                                 'id': 1, }


def test_user_not_found_get_user_by_id(client):
     response = client.get('/users/555')

     assert response.status_code == HTTPStatus.NOT_FOUND
     assert response.json() == {'detail': 'User not found'}
