from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):

    user = User(
        username='koji',
        email='koji@mail.com',
        password='123'
        )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'koji@mail.com')
    )  # faça um mapeamento e me traga esse objeto

    assert asdict(user) == {
        'id': 1,
        'username': 'enzo',
        'password': 'segredo',
        'email': 'enzo@live.com',
        'created_at': time,
        'updated_at': time,
    }
