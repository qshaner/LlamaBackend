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
flask run --debug
```

This will make the application available on `localhost:5000` with live-reloading.
