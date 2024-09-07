from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    with session.begin():
        user = User(
            username='tockinha123',
            email='tockinha@123.com',
            password='sexozinho',
        )

        session.add(user)

    result = session.scalar(
        select(User).where(User.email == 'tockinha@123.com')
    )

    assert result.username == 'tockinha123'
