"""Constants for account and device clients."""

import base64


def _d(enc: str, k: int) -> str:
    """Decode a stored constant."""
    return bytes(b ^ k for b in base64.b64decode(enc)).decode()


# Account authorization settings.
OP_CLIENT_ID = _d("cSVzJXB0IXN0IiF/cXZydg==", 71)
OP_CLIENT_SECRET = _d("uuq9vb3ru7GwvLq4vLzv67+7vu+4677q7Lq/vruxubE=", 137)
