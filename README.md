# Communication Microservice

## Overview
A little mock service to send messages (email and SMS), with logging.

In short, this service has:

1. Automated docker set up for the app and db
2. Validation for the request, and specific validation for phone num / email
3. Simple business logic that inserts messages into Postgres
4. Returns a success / fail based on successful validation and db storage
5. Functional CI on Github action that runs all the tests (found in `.github/`)

### Database `message` Table Structure:

 | id | type  |   recipient     |   content   | status  |   timestamp   |
 | -- | ----- | --------------- | ----------- |-------- | --------------|
 | 1 | email | example@example.com | Hello World | success | 2024-11-13 21:17:50.305058 |

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
2. `psql -U user -d messages`
3. Execute the desired Postgres commands (e.g., `\list`)
## Using Tests
Run `pytest -s` 
