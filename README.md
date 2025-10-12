# LlamaBackend

Initial backend codebase for LlamaRama.

# Usage

## Initial Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
```

## Running for Development

```
flask run --debug --host=0.0.0.0
```

This will make the application available on `localhost:5000` with live-reloading.

# API

All

## POST `/login`

Input: `{"username": str}`
Output: `{"session_id": int}`

This will set the session's counter to 0.

## GET `/`

Input: `{"session_id": int}`
Output: `{"counter": int}`

This will increment, then return the value of the counter for this session.

If

## POST `/logout`

Input: `{"session_id": int}`

This will discard this session's counter.
