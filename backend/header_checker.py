import requests

SECURITY_HEADERS = [

    "Content-Security-Policy",

    "Strict-Transport-Security",

    "X-Frame-Options",

    "X-Content-Type-Options"

]

def check_headers(url):

    try:

        response = requests.get(
            url,
            timeout=5
        )

        found = []

        for header in SECURITY_HEADERS:

            if header in response.headers:

                found.append(header)

        return {
            "score": len(found),
            "headers": found
        }

    except:

        return {
            "score": 0,
            "headers": []
        }