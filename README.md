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
1.  `docker exec -it db-container /bin/bash`
2. `psql`
3. Execute the desired Postgres commands (e.g., `\list`)
## Using Tests
Run `pytest -s` 