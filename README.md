# Communication Microservice

## Overview
A microservice to send messages through multiple channels, supporting email and SMS, with logging.

## Setup
### Docker Setup
1. Run `docker-compose up --build` to start the service and database.

### Running Locally
1. Set up a PostgreSQL database and configure `DATABASE_URL` in `config.py`.
2. Run the application with `python app/api.py`.

## API Usage
### Send Message
- Endpoint: `/sendMessage`
- Method: `POST`
- Payload:
  ```json
  {
    "type": "email",
    "recipient": "example@example.com",
    "content": "Hello World"
  }

 docker exec -it c7c0d08dffd1 /bin/bash