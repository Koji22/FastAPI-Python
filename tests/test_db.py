from fast_zero.models import User


def test_create_user():
    user = User(
        username='koji',
        email='koji@mail.com',
        senha='123')

    assert user.username == 'koji'
