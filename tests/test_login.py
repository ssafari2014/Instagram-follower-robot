from core.login import login

def test_login():
    result = login('username', 'password')
    assert result is True

