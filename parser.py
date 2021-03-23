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
            "-u", "--url", action="store", type=str, required=True,
            help="Specify the url of the target server"
        )
        parser.add_argument(
            "-c", "--connection-count", default=247, action="store",
            help="Count of active connections (default = 247)"
        )
        parser.add_argument(
             "-p", "--proxy", default=False, action="store", type=bool,
            help="Do you want to send the request through a proxy to see how the request looks"
        )
        parser.add_argument(
            "-pp", "--proxyport", action="store", type=int,
            help='Enter the port of your proxy'
        )
        parser.add_argument(
            "-ph", "--proxyhost", action="store", type=str,
            help='Enter the ip of your proxy'
        )

        args = parser.parse_args()
        return_value = {}
        try:
            return_value["url"] = args.url
        except:
            parser.print_help()
            SystemExit

        return_value["proxy"] = args.proxy
        return_value["proxyport"] = args.proxyport
        return_value["proxyhost"] = args.proxyhost

        return_value["connection_count"] = args.connection_count
        return return_value


