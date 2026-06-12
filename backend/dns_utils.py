import socket

def dns_lookup(domain):

    try:

        ip = socket.gethostbyname(domain)

        return {
            "success": True,
            "ip": ip
        }

    except:

        return {
            "success": False,
            "ip": None
        }