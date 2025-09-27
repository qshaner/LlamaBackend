from flask import Blueprint

simple_page = Blueprint("simple_page", __name__)

COUNTER: int = 0


@simple_page.route("/")
def hello_world():
    global COUNTER
    COUNTER = COUNTER + 1
    return {"counter": COUNTER}
