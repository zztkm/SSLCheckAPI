from typing import List

from fastapi import FastAPI

from .schemas import HostNames, ValidResult
from .ssl_check import bulk_check_ssl, check_ssl

app = FastAPI(
    title="SSL Check API",
    description="collects SSL/TLS information from hosts",
    version="0.4.0",
)


@app.get("/isssl/", response_model=ValidResult, response_description="SSL対応しているか判定した結果")
async def is_ssl(host: str):
    return check_ssl(host)


@app.get(
    "/isssl/bulk/",
    response_model=List[ValidResult],
    response_description="SSL対応しているか判定した結果",
)
async def is_ssl_bulk(req: HostNames):
    res = bulk_check_ssl(req.hostnames)
    return res 
