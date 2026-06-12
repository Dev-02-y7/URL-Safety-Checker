async function scanURL(){

    const url =
    document.getElementById(
        "urlInput"
    ).value;

    const response =
    await fetch(
        "http://127.0.0.1:8000/scan",
        {
            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({
                url:url
            })
        }
    );

    const data =
    await response.json();

    renderResults(data);
}

function renderResults(data){

    const results =
    document.getElementById(
        "results"
    );

    results.innerHTML = `

    <div class="result-card">

        <h2>
            Scan Report
        </h2>

        <div class="metric">

            <strong>Domain</strong>

            <span>
            ${data.domain}
            </span>

        </div>

        <div class="metric">

            <strong>IP Address</strong>

            <span>
            ${data.ip}
            </span>

        </div>

        <div class="metric">

            <strong>SSL Certificate</strong>

            <span>
            ${
                data.ssl_valid
                ?
                "Valid"
                :
                "Invalid"
            }
            </span>

        </div>

        <div class="metric">

            <strong>Domain Age</strong>

            <span>
            ${data.domain_age}
            years
            </span>

        </div>
        
        <h3>
        Security Headers
        </h3>

        <ul>

        ${data.security_headers
        .map(
        h =>
        `<li>${h}</li>`
        )
        .join("")}

        </ul>

        <h3>
        Risk Factors
        </h3>

        <ul>

        ${data.risk_factors
        .map(
        f =>
        `<li>${f}</li>`
        )
        .join("")}

        </ul>

        <div class="metric">

            <strong>Header Score</strong>

            <span>
            ${data.header_score}/4
            </span>

        </div>

        <div class="metric">

            <strong>Risk Score</strong>

            <span>
            ${data.risk_score}/100
            </span>

        </div>
        
        <div class="metric">

            <strong>
            Recommendation
            </strong>

            <span>
            ${data.recommendation}
            </span>

        </div>

        <div class="metric">

            <strong>Risk Level</strong>

            <span class="
            ${data.risk_level.toLowerCase()}
            ">
            ${data.risk_level}
            </span>

        </div>

    </div>

    `;
}