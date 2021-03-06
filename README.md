# Gamma Rover
SpaceApps Challenge 2015 by Tim and Eric
## Abstract
Long term space exploration carries many risks including exposure to harmful ionizing radiation. This project uses SPHERES platform robots to improve mobile detection of health threats from gamma radiation in large spacecraft or space stations. Gamma ray sensors can detect damage to shielding from space debris impacts and provide pinpoint location information to target repair efforts.

A simulated gamma ray sensor will send readings to IBM Internet of Things Foundation running as a Bluemix service. Node-RED will be used to monitor sensor data and communicate with a Raspberry pi (registered to Internet of Things Foundation) providing light indicators for movement signal monitoring of the SPHERES device. When the sensor data exceeds a critical threshold, the monitor program will send a STOP signal to the SPHERES device and change the LED display color.

When stopped, Node-RED will simulate handling the http request to obtain location information from the SPHERES device and record the location to a database

## Background and additional project detail
The NASA [SPHERES](http://www.nasa.gov/spheres/mission.html) program provides a small autonomous vehicle capable of navigating within a large spacecraft of space station envrionment. These vehicles are able to use ultrasound beacons to identify position within the spacecraft and can have additional attachments through an expansion port.
[Gamma radiation](http://www.britannica.com/EBchecked/topic/225048/gamma-ray), discovered in the late 1800's is a high energy, short wavelength electromagnetic wave. Gamma rays is ionizing radiation that can cause damage to cells and organs in the body. The earth's atsmophere absorbs almost all non terrestrial gamma rays, however, a spacecraft orbiting earth or in transit for a long journey to mars does not have this type of protection. A recent project was announced to [incorporate a shield](http://www.engineering.com/Education/EducationArticles/ArticleID/7510/Orion-Spacecraft-will-carry-Radiation-Shield-designed-by-High-School-Students.aspx) for gamma rays into the Orion spacecraft. During an extended period of service, an autonomous system for locating defects and damage to the shield could be beneficial to occupants of the spacecraft. Small photo-diode based sensors have been described and developed in [other projects](http://hackaday.com/2013/06/03/a-very-tiny-gamma-ray-detector/) and we imagine attaching one of these sensors to the expansion port of the SPHERES satellite, or having it directly incorporated into future designs.

## Project design and assets in this Github
To explore how to create this type of solution using an internet of things framework, we are using a simulated gamma ray sensor on a mobile device and a monitoring display system on a raspberry pi. This simulated sensor creates a stream of regular data flowing into a processing system defined in Node-RED running on the IBM Bluemix platform. At most times, data from the sensor is in the nominal range and the processing system sends an all clear signal to a mobile device. The mobile device is a raspberry pi registered with the IBM Internet of Things Foundation service and is the endpoint for messages of the processing system in Node-RED. Both the simulated gamma ray sensor and mobile monitor use the [mqtt](https://docs.internetofthings.ibmcloud.com/messaging/mqtt.html) protocol to send and receive messages from the processing system.
![gamma-rover architecture](https://dl.dropboxusercontent.com/u/52328656/hackathons/gamma-rover-arch.png)

For the project, we have slightly modified the mqttPublisher.c file from the [iot-raspberrypi](https://github.com/ibm-messaging/iot-raspberrypi) project and added a small python program (led.py) that is called by the modifications in mqttPublisher.c. The Node-RED flow implementing the processing system is nodeRed-RPi-processing.json. A functional test Node-RED flow for the led color change (nodeRed-RPi-sine.json) using the sine wave inputs coming from the iot-raspberrypi sample application is also included.
## Use of IBM Bluemix
The Internet of Things boilerplate was used to support the Node-RED envrionment. To this a service instance of Internet of Things was added to create the organization used for registered device (raspberry pi) enrollment. View of the Bluemix dashboard:
![bluemix dashboard](https://dl.dropboxusercontent.com/u/52328656/hackathons/gamma-rover-Bluemix-dashboard.png)

Youtube Video demo: https://youtu.be/rnF_9mrPQyY
