[![RFID Jukebox with Google Home](https://img.youtube.com/vi/AvCseOQidSw/0.jpg)](https://www.youtube.com/watch?v=AvCseOQidSw)

Requires:
- python evdev. To install:

wget http://dl.piwall.co.uk/python-evdev_0.4.1-1_armhf.deb

dpkg -i python-evdev_0.4.1-1_armhf.deb

- python mpd-2. To install

pip install python-mpd2

First run 'python config.py' to select the reader from the inputs.




EDIT:


Place the files under homeassistant_files in the config directory of your Homeassistant machine.

https://www.home-assistant.io/

You will need to create custom_components/switch directory in your config directory and place this file in there.

https://github.com/mf-social/Home-Assistant/blob/master/custom_components/switch/gmusic.py


I followed this forum post to figure out how to find my device id, and set up the component.

https://community.home-assistant.io/t/google-music-in-ha/10976


Links to items needed:


Raspberry Pi Zero (Don't forget micro sd card and power supply)

http://www.microcenter.com/product/486575/Zero_W


USB OTG Hub

https://www.amazon.com/gp/product/B01HYJLZH6/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1


RFID 125Khz Reader

https://www.amazon.com/gp/product/B018C8C162/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1


125Khz Cards

https://www.amazon.com/gp/product/B01MQY5Y7U/ref=ox_sc_act_title_1?smid=A1GYMVIZIMSYWM&psc=1


RFID Card Inkjet Tray to print in your printer (Note this is the model needed for my Canon MX922 Printer)

https://www.amazon.com/gp/product/B00P25H0BA/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1


Please note that I have Home Assistant running in a Virtual Machine on another computer. If you want to run Home Assistant and the music cards on the same machine I'd recommend a Raspberry Pi 3 as opposed to the Raspberry Pi Zero
