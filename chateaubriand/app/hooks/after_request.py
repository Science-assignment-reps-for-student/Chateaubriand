import logging

from flask import Response, request


def after_request(response: Response) -> Response:
    try:
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "deny"
        logger = logging.getLogger('waitress')
        logger.info(f"{request.remote_addr}, {request.path}, {request.method}, {response.status_code}")
    finally:
        return response