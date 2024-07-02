import requests

request_url = "https://api.stagingeb.com/v1/contact_requests?page=1&limit=20"
api_key = 'l7u502p8v46ba3ppgvj5y2aad50lb9'
request_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
request_headers = {"accept": "application/json",
                   "X-Authorization": api_key,
                   "User-Agent": request_user_agent
                   }


def get_contacts_names():
    response = requests.get(
        url=request_url,
        headers=request_headers,
    )

    if response.status_code == 200:
        data = response.json()
        return data["content"]
