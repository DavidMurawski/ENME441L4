#!/usr/bin/python27all
import cgi
import json

#green blue red
leds = [0, 0, 0]

data = cgi.FieldStorage()
s1 = data.getvalue('slider1')
button = data.getvalue('button')

leds[button-1] = s1

ledjson = {"green":leds[0], "blue":leds[1], "red":leds[2]}


with open('lab4.txt', 'w') as f:  
  json.dump(ledjson, f)
