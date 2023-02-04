import xml.etree.cElementTree as ET
import eventtime

def genSampleEvent():
    rootArgs = {'xmlns:epcis':'urn:epcglobal:epcis:xsd:1',
            'xmlns:example':'http://ns.example.com/epcis',
            'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance',
            'schemaVersion':'1.2'}
    root = ET.Element('epcis:EPCISDocument', rootArgs)

    EPCISBody = ET.SubElement(root, 'EPCISBody')
    EventList = ET.SubElement(EPCISBody, 'EventList')

    ObjectEvent = ET.SubElement(EventList, 'ObjectEvent')
    ET.SubElement(ObjectEvent, 'eventTime').text = eventtime.now()

    epcList = ET.SubElement(ObjectEvent, 'epcList')
    ET.SubElement(epcList, 'epc').text = 'urn:epc:id:sgtin:0614141.107346.2017'

    ET.SubElement(ObjectEvent, 'action').text = 'OBSERVE'

    readPoint = ET.SubElement(ObjectEvent, 'readPoint')
    ET.SubElement(readPoint, 'id').text = 'urn:epc:id:sgln:0614141.07346.1234'

    return ET.tostring(root, encoding='utf8', method='xml')
    #return ET.tostring(root)

def genObservationEvent(sgtin, sgln, quantity, uom):
    rootArgs = {'xmlns:epcis':'urn:epcglobal:epcis:xsd:1',
            'xmlns:example':'http://ns.example.com/epcis',
            'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance',
            'schemaVersion':'1.2'}
    root = ET.Element('epcis:EPCISDocument', rootArgs)

    EPCISBody = ET.SubElement(root, 'EPCISBody')
    EventList = ET.SubElement(EPCISBody, 'EventList')

    ObjectEvent = ET.SubElement(EventList, 'ObjectEvent')
    ET.SubElement(ObjectEvent, 'eventTime').text = eventtime.now()

    epcList = ET.SubElement(ObjectEvent, 'epcList')
    ET.SubElement(epcList, 'epc').text = 'urn:epc:id:sgtin:'+sgtin

    ET.SubElement(ObjectEvent, 'action').text = 'OBSERVE'

    bizLocation = ET.SubElement(ObjectEvent, 'bizLocation')
    ET.SubElement(bizLocation, 'id').text = 'urn:epc:id:sgln:'+sgln

    extension = ET.SubElement(ObjectEvent, 'extension')
    quantityList = ET.SubElement(extension, 'quantityList')
    quantityElement = ET.SubElement(quantityList, 'quantityElement')
    ET.SubElement(quantityElement, 'quantity').text = quantity
    ET.SubElement(quantityElement, 'uom').text = uom

    return ET.tostring(root, encoding='utf8', method='xml')

def genTransformationEvent():
    pass

def genAggregationEvent():
    pass
