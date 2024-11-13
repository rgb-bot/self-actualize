import pytest
from app.api import app, db
from flask import Flask, jsonify
from unittest.mock import MagicMock
# Assuming Messages model is imported from your models file
from app.models import Messages
import logging
from unittest.mock import patch


@pytest.fixture
def client():
    with app.test_client() as client:
        # Push the application context
        with app.app_context():
            yield client
        with app.app_context():
            db.drop_all()  # Drop tables after the test is done


def test_send_message_success(client, mocker, caplog):
    # Simulate data to be sent in the request
    payload = {
        "type": "email",
        "recipient": "example@example.com",
        "content": "Hello World"
    }

    # Mock db.session.add and db.session.commit to prevent actual DB interaction
    mock_add = mocker.patch('app.db.session.add', autospec=True)
    mock_commit = mocker.patch('app.db.session.commit', autospec=True)

    # Mock the Messages model creation
    mock_message = MagicMock(spec=Messages)

    with caplog.at_level(logging.INFO):
        # Make the POST request to the /sendMessage endpoint with the mock payload
        response = client.post('/sendMessage', json=payload)

        # Simulate the add operation being called and committing the mock message object
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

        # Check the response status and the returned message
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data['message'] == 'Message Sent'
