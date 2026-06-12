from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from dns_utils import dns_lookup
from ssl_utils import check_ssl
from domain_age import get_domain_age
from header_checker import check_headers
from risk import calculate_risk

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UrlRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {
        "message": "URL Safety Checker Running"
    }


@app.post("/scan")
def scan(data: UrlRequest):

    url = data.url

    domain = (
        url.replace("https://", "")
           .replace("http://", "")
           .split("/")[0]
    )

    dns = dns_lookup(domain)

    ssl = check_ssl(domain)

    age = get_domain_age(domain)

    headers = check_headers(url)

    risk = calculate_risk(
        dns["success"],
        ssl["valid"],
        age,
        headers["score"]
    )

    recommendation = ""

    if risk["level"] == "Low":
        recommendation = "Domain appears safe."

    elif risk["level"] == "Medium":
        recommendation = "Proceed with caution."

    else:
        recommendation = "Potentially suspicious domain."

    risk_factors = []

    if not dns["success"]:
        risk_factors.append(
            "DNS Resolution Failed"
        )

    if not ssl["valid"]:
        risk_factors.append(
            "No SSL Certificate"
        )

    if age is not None and age < 1:
        risk_factors.append(
            "Recently Registered Domain"
        )

    if headers["score"] < 2:
        risk_factors.append(
            "Weak Security Headers"
        )

    return {

        "domain": domain,

        "ip": dns["ip"],

        "ssl_valid": ssl["valid"],

        "domain_age": age,

        "security_headers":
        headers["headers"],

        "header_score":
        headers["score"],

        "risk_score":
        risk["score"],

        "risk_level":
        risk["level"],

        "recommendation":
        recommendation,

        "risk_factors":
        risk_factors
    }