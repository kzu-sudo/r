#!/usr/bin/env python3

import argparse

class Parser(object):

    @classmethod
    def parse_arguments(self) -> list:
        parser = argparse.ArgumentParser(
            add_help = True,
            description="This is a script to perform a slowloris attack"
        )
        parser.add_argument(
            "-u", "--url", action="store", type=str, required=False,
            help="specify the url of the target server"
        )
        parser.add_argument(
            "-c", "--connection-count", default=247, action="store",
            help="count of active connections (default = 247)"
        )
        parser.add_argument(
            "-p", "--port", default=80, action='store_true',
            help="specify the port of the server you want to attack",
        )

        args = parser.parse_args()
        return_value = {}
        try:
            return_value["url"] = args.url
        except:
            parser.print_help()
            SystemExit
        return_value["connection_count"] = args.connection_count
        return_value["port"] = args.port
        return return_value

