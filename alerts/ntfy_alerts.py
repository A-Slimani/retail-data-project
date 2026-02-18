import requests

def ntfy_basic(title: str, data: str, server: str, topic: str):
    requests.post(
        f"{server}/{topic}",
        data = data,
        headers = {
            "Title": title,
            "Priority": "default"
        }
    )


def ntfy_detailed():
    pass
