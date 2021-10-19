#!/usr/bin/python37all
import cgi
import json

import cgitb
cgitb.enable()

#green blue red
leds = [0, 0, 0]

data = cgi.FieldStorage()
s1 = data.getvalue('slider1')
button = data.getvalue('button')

leds[button] = s1

ledjson = {"green":leds[0], "blue":leds[1], "red":leds[2]}


with open('lab4.txt', 'w') as f:  
  json.dump(ledjson, f)

"""
print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/led-pwm-multiple.py" method="POST">')
print('<input type="range" name="slider" min="0" max="100" value="%s"><br>' % brightness)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('Brightness = %s' % brightness)
print('</html>')
"""