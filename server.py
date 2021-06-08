from flask import Flask
import RPi.GPIO as GPIO
import logging

BUTTON_PIN = 26
LED_PIN_LIST = [17, 27, 2]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
app = Flask(__name__)

for pin in LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)

@app.route("/")
def index():
   
    return '''
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=0.5">
    <title>Home Control</title>
  </head>
  <body>
  <div style="font-size:50px">
  <hr>
<div class="col-sm-4">
    <h1> <a href="/led/2/state/1">Lights On</a></h1>
</div>
<hr>
<div class="col-sm-4">
 <h1 > <a href="/led/2/state/0"> Lights Off</a> </h1>
</div>
<hr>
<div class="col-sm-4">
    <h1> <a href="/led/27/state/1">Fan On</a></h1>
</div>
<hr>
<div class="col-sm-4">
    <h1 class=""> <a href="/led/27/state/0"> Fan Off</a> </h1>
</div>
</div>
 </body>
</html>





'''
@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Button is pressed"
    return "Button is not pressed"

@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    if not led_pin in LED_PIN_LIST:
        return "Wrong GPIO number: " + str(led_pin)
    if led_state == 0:
        GPIO.output(led_pin, GPIO.LOW)
    elif led_state == 1:
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        return "State must be 0 or 1"
    return "OK"

app.run(host="0.0.0.0", port=80)
#while True:
 #   GPIO.cleanup()  


