# Hackathon Challenge 2

By Eric Foy, William, and Karim Unisa

## What does it do
Running the application will ask you to scan our barcodes.

[lettuce.btw](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/lettuce.btw)
![lettuce image](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/lettuce.png | width=80)

[tomatos.btw](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/tomatos.btw)
![tomatos image](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/tomatos.png)

[containers.btw](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/containers.btw)
![containers image](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/containers.png)

[item.btw](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/item.btw)
![item image](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/item.png)

[Case.btw](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/Case.btw)
![case image](https://github.com/eric-foy/HackathonChallenge2/blob/main/Barcodes/case.png)


Scanning these will capture the GTIN and lot code of the item. These KDE's, key data element, along with its other KDE's will be sent to our EPCIS database. The other KDE's we store in our database are the traceablility lot code, the unit of measure, and the quantity. These are required by the FDA Food traceability list. We also store other data such as the cature time and GLN.

This is part 1 of our application. Part two will demonstrate that we have support for all CTE's, critical tracking events, required by the challenge.

The first events are observation events when we receive an item at the processing line. There are 3 items we recieve to produce our salad: lettuce, tomatos, and containers. These events are triggered as in part one when we scan a barcode.

The next event is a transformation event. This is where we transform the ingredients into finished salad assigning the new traceablility lot code. This event will be triggered when we print a barcode for the finished salad.

The last event is an aggregation event. This is where we pack the salads into cases. This event will be triggered when we print a barcode for the case of salads.

That was part two of our application. Part three will demonstrate the usefulness of having this database.

What is shown on the screen is a graph of the time it takes from when the  ingredients arrive at the processing line till when they leave in cases by the day.
This is one of the many statistical observations you can make with this data. We plan to offer many different ways to view and sort this data.

Some examples would be:
 - An employee is using too much lettuce. Using the unit of measure and expected quantity we can visualise this.
 - A box of tomoatos has gotten lost in the facility. We can automatically flag this and alert someone to find and dispoce of them using the arrival time.
 - Wrong ingredients arrive at the facility. The GTIN is not on our appoved list and we flag these at entry.

The source code in [main.py](https://github.com/eric-foy/HackathonChallenge2/blob/main/src/epcis_service/main.py) is broken down into the 3 parts so you can see what were talking about under the hood.

## How to run
```console
$ python src/epcis_service/main.py
```

## Dependencies
```console
$ pip install requests
$ pip install matplotlib
```
