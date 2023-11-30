# Music Cards

## Requires
### software:
Use python venv:
```bash
python -m venv ./venv
source venv/bin/activate
```

- python evdev and python mpd-2. To install:
```bash
pip install evdev python-mpd2
```

### hardware:
- [Raspberry Pi Zero (Don't forget micro sd card and power supply)](http://www.microcenter.com/product/486575/Zero_W)
- [USB OTG Hub](https://www.amazon.com/gp/product/B01HYJLZH6/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1)
- [RFID 125Khz Reader](https://www.amazon.com/gp/product/B018C8C162/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)
- [125Khz Cards](https://www.amazon.com/gp/product/B01MQY5Y7U/ref=ox_sc_act_title_1?smid=A1GYMVIZIMSYWM&psc=1)
- [RFID Card Inkjet Tray to print in your printer (Note this is the model needed for my Canon MX922 Printer)](https://www.amazon.com/gp/product/B00P25H0BA/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)

Please note that Raspberry Pi Zero is insufficient to run both the Home Assistant and Music Cards concurrently. I recommend you use a Raspberry Pi 3 if you intend to run both at the same time.

## Steps to Configure and/or Run once if you dont want Music Cards to AutoStart

1. Run `python config.py` to select the reader from the inputs
2. Run `python add_card.py` to scan cards and enter your Google Play Music Playlist Name
3. Run `python box.py` to start the application and verify that it is reading your cards and csv list properly

## Install Service to AutoStart

- Change directory to music-cards/
```bash
cd music-cards/
```
- Link the musiccards.service file to systemd
```bash
sudo ln musiccards.service /etc/systemd/system/musiccards.service
```
- Reload the Daemon
```bash
sudo systemctl daemon-reload
```
- Start the musiccards.service
```bash
sudo systemctl start musiccards.service
```
- Check if musiccards.service is running
```bash
sudo systemctl status musiccards.service
```
