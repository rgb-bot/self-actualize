from app.models import db, Messages
import logging


def commit_log(data, logger):
    # If all validations pass, proceed with the business logic
    logger.info(f"Validated data: {data}")

    message_type = data.get('type')
    recipient = data.get('recipient')
    content = data.get('content')
    # Log message status
    log = Messages(type=message_type, recipient=recipient,
                   content=content, status="success")
    db.session.add(log)
    logger.info(f"Adding message: {log}")

    db.session.commit()
