__author__ = 'Sindbad the Sailor'


import os

resp_dict = {'65545': [{'req1': 'request1'}, {'req2': 'request2'}, {'req3': 'request3'}], '64234': [{'req4': 'request4'}, {'req5': 'request5'}, {'req6': 'request6'}]}

""" get request """
print(resp_dict['65545'][0]['req1'])

""" get list length """
print(resp_dict['65545'].__len__())

""" add element to the dict """

if '65545' not in resp_dict:
    resp_dict['65545'] = []
    resp_dict['65545'].append({'resp1': 'response1'})
else:
    resp_dict['65545'].append({'resp1': 'response1'})

if '65545' not in resp_dict:
    resp_dict['65545'] = []
resp_dict['65545'].append({'resp1': 'response1'})

print(resp_dict['65545'])


answer = 
