import requests
import json
import os
import sys

payload={
    "name": str(sys.argv[1]),
    "job":  str(sys.argv[2])
}

res = requests.post("https://reqres.in/api/users",json=payload)

print(res.content)
print(res.status_code)