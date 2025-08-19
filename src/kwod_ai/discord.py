import os

import httpx


def send_message(msg: str) -> None:
    """
    Send a message to Discord using a webhook.

    Args:
        msg (str): The message to send.

    Raises:
        AssertionError: If the DISCORD_WEBHOOK environment variable is not set.
        httpx.HTTPError: If the request to the API fails.
    """
    payload = {"content": msg}
    headers = {"Content-Type": "application/json"}

    hook = os.getenv("DISCORD_WEBHOOK")
    assert hook is not None, "DISCORD_WEBHOOK environment variable is not set"

    response = httpx.post(hook, json=payload, headers=headers)
    response.raise_for_status()
