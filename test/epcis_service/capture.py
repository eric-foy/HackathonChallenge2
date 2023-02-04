import requests

f = open('Example Shipping - Receiving.xml')
xml = f.read()

headers = {'Content-Type': 'application/xml'} # set what your server accepts
print(requests.post('https://freepcis.gs1.org/server/SaladMaker/capture', data=xml, headers=headers).text)
