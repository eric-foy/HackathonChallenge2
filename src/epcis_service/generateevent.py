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

def genTransformationEvent(sgtinIn1, sgtinIn2, sgtinIn3, sgtinOut, sgln, quantity1, quantity2, quantity3, quantityOut, uom1, uom2, uom3, uomOut):
    rootArgs = {'xmlns:epcis':'urn:epcglobal:epcis:xsd:1',
            'xmlns:example':'http://ns.example.com/epcis',
            'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance',
            'schemaVersion':'1.2'}
    root = ET.Element('epcis:EPCISDocument', rootArgs)

    EPCISBody = ET.SubElement(root, 'EPCISBody')
    EventList = ET.SubElement(EPCISBody, 'EventList')

    extension = ET.SubElement(EventList, 'extension')
    TransformationEvent = ET.SubElement(extension, 'TransformationEvent')
    ET.SubElement(TransformationEvent, 'eventTime').text = eventtime.now()

    inputEPCList = ET.SubElement(TransformationEvent, 'inputEPCList')
    ET.SubElement(inputEPCList, 'epc').text = 'urn:epc:id:sgtin:'+sgtinIn1
    ET.SubElement(inputEPCList, 'epc').text = 'urn:epc:id:sgtin:'+sgtinIn2
    
    inputQuantityList = ET.SubElement(TransformationEvent, 'inputQuantityList')
    
    quantityElement = ET.SubElement(inputQuantityList, 'quantityElement')
    ET.SubElement(quantityElement, 'epcClass').text = 'urn:epc:idpat:sgtin:'+sgtinIn1[:-1]+'*'
    ET.SubElement(quantityElement, 'quantity').text = quantity1
    ET.SubElement(quantityElement, 'uom').text = uom1

    quantityElement = ET.SubElement(inputQuantityList, 'quantityElement')
    ET.SubElement(quantityElement, 'epcClass').text = 'urn:epc:idpat:sgtin:'+sgtinIn2[:-1]+'*'
    ET.SubElement(quantityElement, 'quantity').text = quantity2
    ET.SubElement(quantityElement, 'uom').text = uom2

    quantityElement = ET.SubElement(inputQuantityList, 'quantityElement')
    ET.SubElement(quantityElement, 'epcClass').text = 'urn:epc:idpat:sgtin:'+sgtinIn3[:-1]+'*'
    ET.SubElement(quantityElement, 'quantity').text = quantity3
    ET.SubElement(quantityElement, 'uom').text = uom3

    outputEPCList = ET.SubElement(TransformationEvent, 'outputEPCList')
    ET.SubElement(outputEPCList, 'epc').text = 'urn:epc:id:sgtin:'+sgtinOut

    outputQuantityList = ET.SubElement(TransformationEvent, 'outputQuantityList')
    quantityElement = ET.SubElement(outputQuantityList, 'quantityElement')
    ET.SubElement(quantityElement, 'epcClass').text = 'urn:epc:idpat:sgtin:'+sgtinOut[:-1]+'*'
    ET.SubElement(quantityElement, 'quantity').text = quantityOut
    ET.SubElement(quantityElement, 'uom').text = uomOut

    bizLocation = ET.SubElement(TransformationEvent, 'bizLocation')
    ET.SubElement(bizLocation, 'id').text = 'urn:epc:id:sgln:'+sgln

    return ET.tostring(root, encoding='utf8', method='xml')

def genAggregationEvent(sgtin, sgln, quantity, uom):
    rootArgs = {'xmlns:epcis':'urn:epcglobal:epcis:xsd:1',
            'xmlns:example':'http://ns.example.com/epcis',
            'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance',
            'schemaVersion':'1.2'}
    root = ET.Element('epcis:EPCISDocument', rootArgs)

    EPCISBody = ET.SubElement(root, 'EPCISBody')
    EventList = ET.SubElement(EPCISBody, 'EventList')

    AggregationEvent = ET.SubElement(EventList, 'AggregationEvent')
    ET.SubElement(AggregationEvent, 'eventTime').text = eventtime.now()
    ET.SubElement(AggregationEvent, 'parentID').text = 'urn:epc:id:sgtin:'+sgtin

    ET.SubElement(AggregationEvent, 'action').text = 'ADD'

    bizLocation = ET.SubElement(AggregationEvent, 'bizLocation')
    ET.SubElement(bizLocation, 'id').text = 'urn:epc:id:sgln:'+sgln

    extension = ET.SubElement(AggregationEvent, 'extension')
    childQuantityList = ET.SubElement(extension, 'childQuantityList')
    quantityElement = ET.SubElement(childQuantityList, 'quantityElement')
    ET.SubElement(quantityElement, 'epcClass').text = 'urn:epc:idpat:sgtin:'+sgtin[:-1]+'*'
    ET.SubElement(quantityElement, 'quantity').text = quantity
    ET.SubElement(quantityElement, 'uom').text = uom

    return ET.tostring(root, encoding='utf8', method='xml')
