import capture
import generateevent

#xml = '<?xml	version="1.0"	encoding="UTF-8"	standalone="yes"?>'
#xml = xml + generateevent.genSampleEvent().decode("utf-8") 
#xml = generateevent.genSampleEvent()

serial = 0
prefix = '081005593'

#############################
# Recieve products
#############################

# lettuce
gtin = '10810055931016'
gtin = gtin[1:len(prefix)+1]+'.'+gtin[0]+gtin[len(prefix)+1:-1]
serial = serial + 1
sgtin = gtin+'.'+str(serial)
sgln = '0810055931231'
quantity = '20'
uom = 'each'
xml = generateevent.genObservationEvent(sgtin, sgln, quantity, uom)
capture.capture(xml)

# tomatos
gtin = '10810055931023'
gtin = gtin[1:len(prefix)+1]+'.'+gtin[0]+gtin[len(prefix)+1:-1]
serial = serial + 1
sgtin = gtin+'.'+str(serial)
sgln = '0810055931231'
quantity = '50'
uom = 'LB'
xml = generateevent.genObservationEvent(sgtin, sgln, quantity, uom)
capture.capture(xml)

# containers
gtin = '10810055931030'
gtin = gtin[1:len(prefix)+1]+'.'+gtin[0]+gtin[len(prefix)+1:-1]
serial = serial + 1
sgtin = gtin+'.'+str(serial)
sgln = '0810055931231'
quantity = '500'
uom = 'each'
xml = generateevent.genObservationEvent(sgtin, sgln, quantity, uom)
capture.capture(xml)

#############################
# Produce products
#############################
gtin1 = '10810055931016'
gtin1 = gtin1[1:len(prefix)+1]+'.'+gtin1[0]+gtin1[len(prefix)+1:-1]
serial = serial + 1
sgtinIn1 = gtin1+'.'+str(serial)
quantity1 = '0.4'
uom1 = 'each'

gtin2 = '10810055931023'
gtin2 = gtin2[1:len(prefix)+1]+'.'+gtin2[0]+gtin2[len(prefix)+1:-1]
serial = serial + 1
sgtinIn2 = gtin2+'.'+str(serial)
quantity2 = '0.5'
uom2 = 'LB'

gtin3 = '10810055931030'
gtin3 = gtin3[1:len(prefix)+1]+'.'+gtin3[0]+gtin3[len(prefix)+1:-1]
serial = serial + 1
sgtinIn3 = gtin3+'.'+str(serial)
quantity3 = '1'
uom3 = 'each'

gtinOut = '10810055939015'
gtinOut = gtinOut[1:len(prefix)+1]+'.'+gtinOut[0]+gtinOut[len(prefix)+1:-1]
serial = serial + 1
sgtinOut = gtinOut+'.'+str(serial)
sgln = '0810055931248'
quantityOut = '1'
uomOut = 'each'

xml = generateevent.genTransformationEvent(sgtinIn1, sgtinIn2, sgtinIn3, sgtinOut, sgln, quantity1, quantity2, quantity3, quantityOut, uom1, uom2, uom3, uomOut)
capture.capture(xml)


#xml = xml + '<epcis:EPCISDocument xmlns:epcis="urn:epcglobal:epcis:xsd:1" xmlns:example="http://ns.example.com/epcis" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.2"><EPCISBody><EventList><ObjectEvent> <eventTime>2005-04-03T20:33:31.116-06:00</eventTime><eventTimeZoneOffset>-06:00</eventTimeZoneOffset><epcList><epc>urn:epc:id:sgtin:0614141.107346.2017</epc></epcList><action>OBSERVE</action><readPoint><id>urn:epc:id:sgln:0614141.07346.1234</id></readPoint></ObjectEvent></EventList></EPCISBody></epcis:EPCISDocument>'

#print(xml)
