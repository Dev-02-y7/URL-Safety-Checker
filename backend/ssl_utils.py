import ssl
import socket

def check_ssl(domain):

    try:

        context = ssl.create_default_context()

        with context.wrap_socket(
            socket.socket(),
            server_hostname=domain
        ) as sock:

            sock.settimeout(5)

            sock.connect((domain,443))

            cert = sock.getpeercert()

            return {
                "valid": True,
                "issuer": str(cert.get("issuer"))
            }

    except:

        return {
            "valid": False,
            "issuer": None
        }