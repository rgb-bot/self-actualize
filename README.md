# Communication Microservice

## Overview
A little mock service to send messages through multiple channels, supporting email and SMS, with logging.

## Setup
###
Run `bash setup.sh`

## API Usage
### Send Message
- Endpoint: `/sendMessage`
- Method: `POST`
- Payload:
  ```json
  {
    "type": "email" | "SMS",
    "recipient": "example@example.com" | "324-234-2343",
    "content": "Hello World"
  }
  ``````
  Run this in your terminal:
  ```
  curl -X POST http://localhost:5050/sendMessage -H "Content-Type: application/json" -d '{
  "type": "email",
  "recipient": "example@example.com",
  "content": "Why do you drive in a parkway but park in a driveway?"
  }'

## Seeing the db
### Check database to ensure logs are there
1. Execute `docker ps` and copy and paste the container id for db-container
2.  `docker exec -it <container_id> /bin/bash`
3. `psql`
4. Execute the desired Postgres commands
## Using Tests
Run `pytest -s`   