#!/usr/bin/env python3

from fake_useragent import UserAgent

DEFAULT_HEADERS = {
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*",
     "Accept-Encoding": "gzip, deflate",
     "Accept-Language": "ru,en-us;q=0.7,en;q=0.3",
     "Accept-Charset": "windows-1251,utf-8;q=0.7,*;q=0.7",
     "Connection": "keep-alive\r\n"
}



class store_data(object):
    __slots__ = ("scheme", "host", "port", "path", "ssl", "fake_agent", "lines", "socket_ip", "socket_port", "p")


    def __init__(self, scheme : str, host : str,
                 port : int, path : str = '/', ssl : bool = False,
                 fake_agent: str = '', lines : list = [], socket_ip : str = None,
                 socket_port : int = None, p : bool = False):

       self.scheme = scheme
       self.host = host
       self.port = port
       self.path = path
       self.ssl = ssl
       self.fake_agent = fake_agent
       self.lines = lines
       self.socket_ip = socket_ip
       self.socket_port = socket_port
       self.p = p


    @classmethod
    def create_fake_useragent(self):
        fake_useragent = ''
        try:
            ua = UserAgent(verify_ssl=False)
            print(ua.random)
            fake_useragent = ua.random
        except fake_useragent.FakeUserAgentError as fe:
            raise exec.UserAgentError("Can't crate fake-agent object.") from fe
        return fake_useragent


    @classmethod
    def prepare_for_sending(self, m):
        self.lines = [
             f"GET {m.path} HTTP/1.1\r\n",
             f"Host: {m.host}\r\n",
             f"User-Agent: {m.fake_agent}\r\n"
        ]

        self.lines.extend([f"{k}: {v}\r\n" for k, v in DEFAULT_HEADERS.items()])







