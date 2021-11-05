import socket
import ssl
from os import error
from socket import getdefaulttimeout, setdefaulttimeout

from .schemas import ValidResult

setdefaulttimeout(5.0)
context = ssl.create_default_context()


def check_ssl(hostname: str) -> str:
    cert_valid = False
    version = None
    err = None
    try:
        with socket.create_connection(
            (hostname, 443), timeout=getdefaulttimeout()
        ) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                version = ssock.version()
                if version:
                    cert_valid = True
    except ssl.SSLCertVerificationError:
        err = "CERTIFICATE_VERIFY_FAILED"
    except ConnectionRefusedError:
        err = "CONNECTION_REFUSED_ERROR"
    except socket.timeout:
        err = "TIME_OUT"
    finally:
        return ValidResult(
            host=hostname, valid=cert_valid, version=version, error=err
        )
