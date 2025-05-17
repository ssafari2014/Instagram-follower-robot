from core.follow import follow
from core.login import login


def test_follows():
    session = login("sajad__saffari", "Abc@12345")
    result = follow(session)
    assert session == True
    assert result == True

