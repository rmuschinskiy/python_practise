__author__ = 'Sindbad the Sailor'

import os
import re
req_dict = {}
resp_dict = {}
f = open('C:\\Users\\Sindbad the Sailor\\Documents\\xai.trc.2015-09-24','r')
client_info = 'ELO'
myregex = "(?<=\\\\)\d{5} Origin IP:[0-9]+(?:\.[0-9]+){3} user: " + client_info + " XML length:\d+"
print(myregex)
for line in f:
    if 'Request At' and client_info in line:
        m = re.search(myregex, line.strip())
        print(line.strip())
        id_str_req = m.group(0)
        if id_str_req not in req_dict:
            req_dict[id_str_req] = []
        req_dict[id_str_req].append({line: f.next()})
    elif 'Response At' and client_info in line:
        m = re.search(myregex, line.strip())
        id_str_resp = m.group(0)
        if id_str_resp not in resp_dict:
            resp_dict[id_str_resp] = []
        resp_dict[id_str_resp].append({line: f.next()})

for req_key in req_dict:
    for resp_key in resp_dict:
        if req_dict[req_key].__len__() != resp_dict[resp_key].__len__():
            print("mismatch found:")
            print(req_dict[req_key])
            print(resp_dict[resp_key])


f.close()