URL Safety Checker

A cybersecurity-focused web application that helps users quickly assess whether a URL appears safe before visiting it.
I built this project to explore the fundamentals of web security, threat analysis, and risk assessment while gaining hands-on experience with FastAPI, cybersecurity concepts, and full-stack development.
Rather than simply checking if a website is online, the application performs multiple security checks and combines the results into an overall risk score, helping users make more informed decisions about unfamiliar websites.

<img width="1807" height="382" alt="Screenshot 2026-06-12 155957" src="https://github.com/user-attachments/assets/41d8b0ca-3033-4a8c-a9fb-09aca1f4082d" />

<img width="1861" height="802" alt="Screenshot 2026-06-12 160012" src="https://github.com/user-attachments/assets/7032a93f-9e4a-4906-88a1-eae903e88a83" />

Features:

-> SSL Certificate Validation

Checks whether a website has a valid SSL/TLS certificate configured correctly.

-> DNS Resolution Analysis

Performs DNS lookups to verify whether a domain resolves successfully and retrieves its associated IP address.

-> Domain Age Intelligence

Uses WHOIS data to estimate how long a domain has existed. Newly registered domains can sometimes be associated with phishing campaigns or malicious activity.

-> Security Header Inspection

Analyzes important HTTP security headers, including:

* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options

-> Risk Scoring Engine

Combines the results of all checks into a simple risk score and classifies domains as:

* Low Risk
* Medium Risk
* High Risk

-> Security Recommendations

Provides clear explanations and recommendations based on detected weaknesses.

Why I Built This

As someone interested in cybersecurity, software engineering, and machine learning, I wanted to build a project that moved beyond tutorials and focused on real-world security concepts.

This project helped me understand:

* How DNS works behind the scenes
* SSL/TLS certificate validation
* HTTP security headers
* Domain intelligence gathering
* Risk assessment methodologies
* Building REST APIs with FastAPI
* Connecting a frontend application to a backend service

Tech Stack:

Backend

* Python
* FastAPI
* Python-WHOIS

Frontend

* HTML
* CSS
* JavaScript

Cybersecurity Concepts

* DNS Analysis
* SSL/TLS Validation
* WHOIS Intelligence
* Security Headers
* Risk Assessment

How to Run the Project:

Start the Backend

```powershell
cd backend
uvicorn main:app --reload
```

Backend will run on:

```text
http://127.0.0.1:8000
```

### Start the Frontend

```powershell
cd frontend
python -m http.server 5500
```

Frontend will run on:

```text
http://localhost:5500
```

Example Analysis

The application evaluates domains based on:

SSL Certificate Status

DNS Resolution

Domain Age

Security Headers

Overall Risk Score

and generates recommendations to help identify potentially suspicious websites.

Future Improvements:

Some ideas for future development include:

* Phishing detection models
* URL reputation databases
* AI-powered security analysis
* Exportable security reports

Key Takeaways

Building this project strengthened my understanding of both software engineering and cybersecurity by combining backend development, web technologies, and practical security analysis into a single application.

It was also a great opportunity to learn how real security tools gather information, assess risk, and present findings in a way that is useful to users.

