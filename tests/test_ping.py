from api.ping import ping_db


def test_it():
    print(ping_db())
