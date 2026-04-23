#!/usr/bin/env python3

import requests

r =requests.get("http://localhost:1234/")
print(r.text)
