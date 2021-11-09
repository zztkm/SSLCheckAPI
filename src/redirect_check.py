from urllib.request import urlopen, Request
from urllib.parse import urlunsplit, urlencode

import src

from .schemas import CheckRedirectResponse


def _generate_http_url(host: str):
    return urlunsplit(("http", host, "", "", ""))


def _create_request(url):
    req = Request(url)
    # fake_user_agent はここから取得
    # https://generatefakename.com/user-agent
    fake_user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5340 (KHTML, like Gecko) Chrome/36.0.888.0 Mobile Safari/5340"
    req.add_header("User-Agent", fake_user_agent)
    return req


# リダイレクト先URLを取得する関数
def _get_redirect_url(src_url):
    req = _create_request(src_url)
    with urlopen(req) as res:
        url = res.url  # 最終的な URL を取得
        if src_url == url:
            return None  # 指定された URL と同じなのでリダイレクトしていない
        else:
            return str(url)  # 指定された URL と異なるのでリダイレクトしている


async def check_redirect(host: str):
    url = _generate_http_url(host)
    redirect_url = _get_redirect_url(url)
    return CheckRedirectResponse(host=host, request_url=url, redirect_url=redirect_url)
