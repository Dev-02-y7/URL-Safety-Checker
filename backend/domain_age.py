import whois
from datetime import datetime

def get_domain_age(domain):

    try:

        info = whois.whois(domain)

        created = info.creation_date

        if isinstance(created,list):
            created = created[0]

        age_days = (
            datetime.now() -
            created
        ).days

        age_years = round(
            age_days / 365,
            1
        )

        return age_years

    except:

        return None