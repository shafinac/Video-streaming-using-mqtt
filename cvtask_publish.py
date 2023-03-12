# Importing Libraries
import cv2 as cv
import paho.mqtt.client as mqtt
import base64
import time
broker_mqtt = "broker.emqx.io"
mq_topic = "cvtask"
# Object to capture the frames
cap = cv.VideoCapture(0)
# Phao-MQTT Clinet
client = mqtt.Client()
client.connect(broker_mqtt)
try:
 while True:
  start = time.time()
  _, frame = cap.read()
  # Encoding the Frame
  _, buffer = cv.imencode('.jpg', frame)
  # Converting into encoded bytes
  jpg_as_text = base64.b64encode(buffer)
  client.publish(mq_topic, jpg_as_text)
  end = time.time()
  t = end - start
  fps = 1/t
  print(fps)
except:
 cap.release()
 client.disconnect()
 print("\nrestart new feed")