from fastapi import FastAPI
from py_ssl_checker import SSLChecker

from schemas import ValidResult

SSLChecker = SSLChecker()

app = FastAPI(
    title="SSL Check API",
    description="collects SSL/TLS information from hosts",
    version="0.1.0"
)


def check_ssl(host: str):
    cert = SSLChecker.get_cert(host)
    result = SSLChecker.get_cert_info(host, cert)
    res = {"host": result["host"], "valid": result["cert_valid"]}
    return res


@app.get("/ssl-check/",
         response_model=ValidResult,
         response_description="SSLチェック結果")
async def read_item(host: str):
    return check_ssl(host)
