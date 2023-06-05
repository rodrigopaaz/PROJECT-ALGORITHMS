from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('teste', 'abc')
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(22, 22)

    test_1 = encrypt_message('aabbcc', 3)
    assert test_1 == 'baa_ccb'
    test_2 = encrypt_message('abbcca', 4)
    assert test_2 == 'ac_cbba'
    test_3 = encrypt_message('trybe', 7)
    assert test_3 == ('ebyrt')
