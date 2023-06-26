from http import HTTPStatus
from urllib.parse import urljoin

from flask import jsonify, request

from settings import (
    NO_REQUIRED_FIELDS_GIVEN_MESSAGE,
    NOT_FOUND_MESSAGE,
    NO_BODY_MESSAGE,
    DUPLICATE_MESSAGE_FOR_API,
)
from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.views import get_unique_short_id


@app.route("/api/id/<string:short_id>", methods=["GET"])
def get_original_url(short):
    urlmap = URLMap.query.filter_by(short=short).first()
    if urlmap is None:
        raise InvalidAPIUsage(NOT_FOUND_MESSAGE, HTTPStatus.NOT_FOUND)
    return jsonify({"url": urlmap.original}), HTTPStatus.OK


@app.route("/api/id/", methods=["POST"])
def add_urlmap():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(NO_BODY_MESSAGE)
    if "url" not in data:
        raise InvalidAPIUsage(NO_REQUIRED_FIELDS_GIVEN_MESSAGE)
    short = data.get("custom_id") or get_unique_short_id()
    if URLMap.query.filter_by(short=short).first() is not None:
        raise InvalidAPIUsage(DUPLICATE_MESSAGE_FOR_API.format(short))
    urlmap = URLMap(original=data["url"], short=short)
    db.session.add(urlmap)
    db.session.commit()
    return (
        jsonify(
            {"url": urlmap.original, "short_link": urljoin(request.url_root, short)}
        ),
        HTTPStatus.CREATED,
    )
