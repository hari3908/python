import requests
import json
import os
import sys

payload={
    "name": "Bob",
    "job":  "IT"
}

res = requests.post("https://reqres.in/api/users",json=payload)

print(res.content)
print(res.status_code)