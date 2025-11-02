from flask import (
    abort,
    Blueprint,
    jsonify,
    request,
)
import json
from werkzeug.exceptions import BadRequest

simple_page = Blueprint("simple_page", __name__)

COUNTERS: dict[str, int] = {}
SESSION_ID = "X-Session-Id"


@simple_page.route("/", methods=["GET", "POST"])
def hello_world():
    global COUNTERS
    session_id = request.headers.get(SESSION_ID)

    if session_id is None:
        abort(403, "Session ID not provided")
    if session_id not in COUNTERS:
        abort(403, "Session ID not recognized")

    if request.method == "POST":
        COUNTERS[session_id] += 1

    return jsonify(
        {
            "counter": COUNTERS[session_id],
        }
    )


@simple_page.route("/login", methods=["POST"])
def login():
    global COUNTERS

    try:
        content = request.json
    except json.decoder.JSONDecodeError:
        abort(400, "No request body")
    except BadRequest:
        abort(400, "Bad request body")
    if "username" not in content:
        abort(401, "Username not provided")

    session_id = request.headers.get(SESSION_ID)
    if session_id:
        logout()

    session_id = str(hash(content["username"]))

    # I'm not sure what to do here if a user logs back in when already logged in
    if session_id not in COUNTERS:
        COUNTERS[session_id] = 0

    return jsonify(
        {
            "session_id": session_id,
        }
    )


@simple_page.route("/logout", methods=["POST"])
def logout():
    session_id = request.headers.get(SESSION_ID)

    global COUNTERS
    if session_id in COUNTERS:
        del COUNTERS[session_id]

    return 200  # Should be 204, I guess?
