#!/usr/bin/env python3

import urllib.request

print("client start")

fp = urllib.request.urlopen("http://192.168.198.128:1234/")
#fp = urllib.request.urlopen("http://localhost:1234/")
print("fp request created")

encodedContent = fp.read()
print("fp request readed")

decodedContent = encodedContent.decode("utf8")
print("decodedContent done")

print(decodedContent)

fp.close()
print("fp close done")
