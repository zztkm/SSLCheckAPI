import logging
import socket
import ssl
from concurrent import futures
from socket import getdefaulttimeout, setdefaulttimeout
from typing import List

from .schemas import ValidResult

logger = logging.getLogger(__name__)

setdefaulttimeout(5.0)
context = ssl.create_default_context()


ssl_check_max_workers = 15
ssl_check_executor = futures.ThreadPoolExecutor(max_workers=ssl_check_max_workers)


def check_ssl(hostname: str):
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
        return ValidResult(host=hostname, valid=cert_valid, version=version, error=err)


def bulk_check_ssl(hostnames: List[str]):
    res = []
    future_to_ssl_check = {
        ssl_check_executor.submit(check_ssl, host): host for host in hostnames
    }
    for future in futures.as_completed(future_to_ssl_check):
        try:
            result = future.result()
            res.append(result)
        except Exception as err:
            logger.error(err)

    return res
