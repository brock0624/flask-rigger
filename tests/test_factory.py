# -*- coding:utf-8 -*-
import pytest


def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"


if __name__ == '__main__':
    pytest.main(["-s", "test_factory.py"])
