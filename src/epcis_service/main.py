import capture
import generateevent

#xml = '<?xml	version="1.0"	encoding="UTF-8"	standalone="yes"?>'
#xml = xml + generateevent.genSampleEvent().decode("utf-8") 
xml = generateevent.genSampleEvent()

#xml = xml + '<epcis:EPCISDocument xmlns:epcis="urn:epcglobal:epcis:xsd:1" xmlns:example="http://ns.example.com/epcis" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.2"><EPCISBody><EventList><ObjectEvent> <eventTime>2005-04-03T20:33:31.116-06:00</eventTime><eventTimeZoneOffset>-06:00</eventTimeZoneOffset><epcList><epc>urn:epc:id:sgtin:0614141.107346.2017</epc></epcList><action>OBSERVE</action><readPoint><id>urn:epc:id:sgln:0614141.07346.1234</id></readPoint></ObjectEvent></EventList></EPCISBody></epcis:EPCISDocument>'

#print(xml)
capture.capture(xml)
