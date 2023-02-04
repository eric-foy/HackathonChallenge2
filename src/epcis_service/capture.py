import requests

def captureExample():
    f = open('Example Shipping - Receiving.xml')
    xml = f.read()

    headers = {'Content-Type': 'application/xml'}
    requests.post('https://freepcis.gs1.org/server/SaladMaker/capture', data=xml, headers=headers).text

def capture(xml):
    headers = {'Content-Type': 'application/xml'}
    requests.post('https://freepcis.gs1.org/server/SaladMaker/capture', data=xml, headers=headers).text
