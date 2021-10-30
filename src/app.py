from typing import List
from fastapi import FastAPI
from py_ssl_checker import SSLChecker

from .schemas import ValidResult

SSLChecker = SSLChecker()

app = FastAPI(
    title="SSL Check API",
    description="collects SSL/TLS information from hosts",
    version="0.2.0"
)


def check_ssl(host: str):
    cert = SSLChecker.get_cert(host)
    result = SSLChecker.get_cert_info(host, cert)
    res = {"host": result["host"], "valid": result["cert_valid"]}
    return res


@app.get("/isssl/",
         response_model=ValidResult,
         response_description="SSL対応しているか判定した結果")
async def is_ssl(host: str):
    return check_ssl(host)


@app.get("/isssl/bulk/",
         response_model=List[ValidResult],
         response_description="SSL対応しているか判定した結果")
async def is_ssl_bulk(hosts: List[str]):
    res = []
    for host in hosts:
        res.append(check_ssl(host))
    return check_ssl(hosts)
