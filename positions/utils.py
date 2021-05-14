from uuid import uuid4


def create_random_code():
    return str(uuid4()).replace("-", "")[:10]
