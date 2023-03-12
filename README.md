# Video-streaming-using-mqtt
Segmentation on your live camera feed with good fps(using image processing only)
Using cv2, the publish task will capture the live feed from your pc camera
This is broken into frames and then encoded using base64.
For mqtt, mosquito broker is used and paho.mqtt library is the main library.

At subscribing end, the video is decoded and added to a numpy array.
It is then converted into a greyscale image so that Thresholding ( or Edge) based
segmentation can be performed on the output feed.
