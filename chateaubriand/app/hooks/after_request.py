import logging

from flask import Response, request

from chateaubriand.app.extensions import logger


def after_request(response: Response) -> Response:
    try:
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "deny"
        logger.info(f"{request.remote_addr} - [{request.method} {request.path}] {response.status_code}")
    finally:
        return response