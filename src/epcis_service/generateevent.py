import xml.etree.cElementTree as ET

def genSampleEvent():
    rootArgs = {'xmlns:epcis':'urn:epcglobal:epcis:xsd:1',
            'xmlns:example':'http://ns.example.com/epcis',
            'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance',
            'schemaVersion':'1.2'}
    root = ET.Element('epcis:EPCISDocument', rootArgs)

    EPCISBody = ET.SubElement(root, 'EPCISBody')
    EventList = ET.SubElement(EPCISBody, 'EventList')

    ObjectEvent = ET.SubElement(EventList, 'ObjectEvent')
    ET.SubElement(ObjectEvent, 'eventTime').text = '2005-04-03T20:33:31.116-06:00'
    ET.SubElement(ObjectEvent, 'eventTimeZoneOffset').text = '-06:00'

    epcList = ET.SubElement(ObjectEvent, 'epcList')
    ET.SubElement(epcList, 'epc').text = 'urn:epc:id:sgtin:0614141.107346.2017'

    ET.SubElement(ObjectEvent, 'action').text = 'OBSERVE'

    readPoint = ET.SubElement(ObjectEvent, 'readPoint')
    ET.SubElement(readPoint, 'id').text = 'urn:epc:id:sgln:0614141.07346.1234'

    return ET.tostring(root, encoding='utf8', method='xml')
    #return ET.tostring(root)
