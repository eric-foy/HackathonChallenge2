import capture
import generateevent
import simulation

serial = 0
prefix = '081005593'

########################################################
# Part 1 - Scan barcode and record transaction
########################################################

gtin = input('please scan...')
# containers
#gtin = '10810055931030'
gtin = gtin[2:]
gtin = gtin[1:len(prefix)+1]+'.'+gtin[0]+gtin[len(prefix)+1:-1]
serial = serial + 1
sgtin = gtin+'.'+str(serial)
sgln = '0810055931231'
quantity = '500'
uom = 'each'
xml = generateevent.genObservationEvent(sgtin, sgln, quantity, uom)
capture.capture(xml)

input("press enter for next part...")
########################################################
# Part 2 - Simulation of ESCIS transactions
# Simulate receiving:
#   pack of lettuce 20 ct
#   50 LB of tomatos
# Simulate transformation:
#   creating 1 salid
# Simulate aggregating:
#   25 salids into a case
########################################################

#############################
# Recieve products
#############################

# lettuce
gtin = '10810055931016'
gtin = gtin[1:len(prefix)+1]+'.'+gtin[0]+gtin[len(prefix)+1:-1]
serial = serial + 1
sgtin = gtin+'.'+str(serial)
sgln = '0810055931231'
lot = 'AB1234'
lgtin = gtin+'.'+lot
quantity = '20'
uom = 'each'
xml = generateevent.genObservationEvent(sgtin, sgln, quantity, uom, lgtin)
capture.capture(xml)

# tomatos
gtin = '10810055931023'
gtin = gtin[1:len(prefix)+1]+'.'+gtin[0]+gtin[len(prefix)+1:-1]
serial = serial + 1
sgtin = gtin+'.'+str(serial)
sgln = '0810055931231'
lot = '199X'
lgtin = gtin+'.'+lot
quantity = '50'
uom = 'LB'
xml = generateevent.genObservationEvent(sgtin, sgln, quantity, uom, lgtin)
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
lot1 = 'AB1234'
lgtinIn1 = gtin+'.'+lot1
quantity1 = '0.4'
uom1 = 'each'

gtin2 = '10810055931023'
gtin2 = gtin2[1:len(prefix)+1]+'.'+gtin2[0]+gtin2[len(prefix)+1:-1]
serial = serial + 1
sgtinIn2 = gtin2+'.'+str(serial)
lot2 = '199X'
lgtinIn2 = gtin2+'.'+lot2
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
lotOut = '1234WSU'
lgtinOut = gtinOut+'.'+lotOut
quantityOut = '1'
uomOut = 'each'

xml = generateevent.genTransformationEvent(sgtinIn1, sgtinIn2, sgtinIn3, sgtinOut, sgln, quantity1, quantity2, quantity3, quantityOut, uom1, uom2, uom3, uomOut, lgtinIn1, lgtinIn2, lgtinOut)
capture.capture(xml)

#############################
# Aggregate products
#############################

# case of 25 salids
gtin = '10810055939012'
gtin = gtin[1:len(prefix)+1]+'.'+gtin[0]+gtin[len(prefix)+1:-1]
serial = serial + 1
sgtin = gtin+'.'+str(serial)
sgln = '0810055931248'
lot = 'AB1234199X'
lgtin = gtin+'.'+lot
quantity = '25'
uom = 'each'
xml = generateevent.genAggregationEvent(sgtin, sgln, quantity, uom, lgtin)
capture.capture(xml)

input("press enter for next part...")
########################################################
# Part 3 - Simulation for processing thousands of salids
########################################################

# 20 cases of 20 packs of lettuce for 400 lettuce
# 10 cases of 50 pounds of tomatos for 500 tomatos
# 40 cases of 25 salids each for 1000 salids produced

simulation.simulate()
