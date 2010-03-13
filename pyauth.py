#!/usr/bin/python
# coding=utf-8

# The py-authserver project is Email Ware 
# author: Mark Weirath aka xlr8or
# 
# You have to send me an email before you are allowed to use this code.
# 
# The publication of this program on CD-Roms, periodicals or other media
# needs to be permitted by the author.
# 
# Please get in Contact with me, if you intend to do so.
# 
# DO NOT USE THIS CODE IF YOU DON'T LIKE THESE RULES
# THIS CODE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. 
# USE IT AT YOUR OWN RISK. IN NO EVENT SHALL I BE LIABLE FOR ANY DAMAGES 
# WHATSOEVER INCLUDING DIRECT, INDIRECT, INCIDENTAL, CONSEQUENTIAL, LOSS 
# OF BUSINESS PROFITS OR SPECIAL DAMAGES.
# 
# This License can be changed anytime by the author.


# Python implementation of a basic authentication server as used in q3a based games.
# This project was started for personal use to test interaction with an existing gameserver

import SocketServer

class MyUDPHandler(SocketServer.BaseRequestHandler):
    _masterServers = ("127.0.0.1",)

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        data = data.lstrip('ÿ')
        try:
            array = data.split()
            command = array[0]
            if command == "getIpAuthorize":
                serial = array[1]
                clientIp = array[2]
                print "Received: %s" % data
                #insert voodoo to calculate guid here
                message = "ÿÿÿÿipAuthorize %s accept KEY_IS_GOOD %s " % serial
                print "Sent: %s" % message
                socket.sendto(message, self.client_address)
            elif command == "getKeyAuthorize":
                print "Received: %s" % data
                key = array[2]
                print "Client key: %s" % key
                #insert voodoo to calculate guid here
                message = "ÿÿÿÿkeyAuthorize %s accept KEY_IS_GOOD %s " % key
                print "Sent: %s" % message
                socket.sendto(message, self.client_address)
        except:
            pass

if __name__ == "__main__":
   HOST, PORT = "localhost", 20500
   server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
   server.serve_forever()

