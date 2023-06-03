from django.test import TestCase, Client
import pytest


def test_main():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200


def test_contact():
    client = Client()
    response = client.get('/Contact')
    assert response.status_code == 200


def test_view_requires_login():
    client = Client()
    response = client.get('/schedule_appointment')
    assert response.status_code == 302
    assert response.url == '/login/?next=/schedule_appointment'
