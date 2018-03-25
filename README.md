Requires:
- python evdev. To install:

wget http://dl.piwall.co.uk/python-evdev_0.4.1-1_armhf.deb

dpkg -i python-evdev_0.4.1-1_armhf.deb

- python mpd-2. To install

pip install python-mpd2

First run 'python config.py' to select the reader from the inputs.


EDIT:
Link to video of project in use:
https://youtu.be/AvCseOQidSw

Place the files under homeassistant_files in the config directory of your Homeassistant machine.
https://www.home-assistant.io/

You will need to create custom_components/switch directory in your config directory and place this file in there.
https://github.com/mf-social/Home-Assistant/blob/master/custom_components/switch/gmusic.py

I followed this forum post to figure out how to find my device id, and set up the component.
https://community.home-assistant.io/t/google-music-in-ha/10976
