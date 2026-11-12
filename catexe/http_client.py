"""Client HTTP commun aux modules CAT.EXE."""
from __future__ import annotations

import requests

USER_AGENT = "CATEXE-OSINT/6.3 (+https://github.com/diego1505-Art/osint_tool_code_cat.exe)"


def create_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": USER_AGENT,
        "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
    })
    return session
