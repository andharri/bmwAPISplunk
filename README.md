# bmwAPISplunk

There are lots of examples floating around regarding scripts to run API calls to the BMW Connected Drive app. But I wanted to make my own anyway!

You will need to provide the following:

- BMW Username
- BMW Password
- BMW VIN number

This will make a general API call to get current car data such as lat/long, mileage, fuel remaining etc.

Optionally you can dump this data into Splunk, if you don't want to this comment out the last 3 lines