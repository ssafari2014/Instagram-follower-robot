from core.login import login

def test_login():
    result = login('s.saffari2014@yahoo.com', 'Abc@12345')
    assert result is True