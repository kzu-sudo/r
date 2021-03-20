#!/usr/bin/env python3

import fake_useragent

DEFAULT_HEADERS = {
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*",
     "Accept-Encoding": "gzip, deflate",
     "Accept-Language": "ru,en-us;q=0.7,en;q=0.3",
     "Accept-Charset": "windows-1251,utf-8;q=0.7,*;q=0.7",
     "Connection": "keep-alive"
}


class store_data(object):
    __slots__ = ("scheme", "host", "port", "path", "ssl", "fake_agent", "lines")

    def __init__(self, scheme : str, host : str,
                 port : int, path : str, ssl : bool = False
    ):
       self.scheme = scheme
       self.host = host
       self.port = port
       self.path = path
       self.ssl = ssl

    @classmethod
    def create_fake_useragent(self):
        try:
            self.fake_agent = fake_useragent.UserAgent()
        except fake_useragent.FakeUserAgentError as fe:
            raise exec.UserAgentError("Can't crate fake-agent object.") from fe


    @classmethod
    def prepare_for_sending(self):
        self.lines = [
             f"GET {self.path} HTTP/1.1\r\n",
             f"Host: {self.host}\r\n",
             f"User-Agent: {self.fake_agent}\r\n"
        ]

        self.lines.extend([f"{k}: {v}\r\n" for k, v in DEFAULT_HEADERS.items()])









