from core.follow import follow
from core.login import login


def test_follows():
    session = login("username", "password")
    result = follow(session)
    assert session == True
    assert result == True

