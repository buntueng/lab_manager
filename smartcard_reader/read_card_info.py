#!/usr/bin/env python
# Kawin Viriyaprasopsook<kawin.v@kkumail.com>
# 2023-10-19
# sudo apt-get -y install pcscd python-pyscard python-pil

import binascii
import os
import sys
from PIL import Image
from smartcard.System import readers
from smartcard.util import toHexString, HexListToBinString

# Thailand ID Smartcard

# tis-620 to utf-8
def thai2unicode(data):
    if isinstance(data, list):
        return bytes(data).decode('tis-620').replace('#', ' ').strip()
    else:
        return data

def get_data(cmd, req=[0x00, 0xc0, 0x00, 0x00]):
    data, sw1, sw2 = connection.transmit(cmd)
    data, sw1, sw2 = connection.transmit(req + [cmd[-1]])
    return [data, sw1, sw2]

# Define the APDUs used in this script
# https://github.com/chakphanu/ThaiNationalIDCard/blob/master/APDU.md

# Check card
SELECT = [0x00, 0xA4, 0x04, 0x00, 0x08]
THAI_CARD = [0xA0, 0x00, 0x00, 0x00, 0x54, 0x48, 0x00, 0x01]

# CID
CMD_CID = [0x80, 0xb0, 0x00, 0x04, 0x02, 0x00, 0x0d]

# TH Fullname
CMD_THFULLNAME = [0x80, 0xb0, 0x00, 0x11, 0x02, 0x00, 0x64]

# EN Fullname
CMD_ENFULLNAME = [0x80, 0xb0, 0x00, 0x75, 0x02, 0x00, 0x64]

# Date of birth
CMD_BIRTH = [0x80, 0xb0, 0x00, 0xD9, 0x02, 0x00, 0x08]

# Gender
CMD_GENDER = [0x80, 0xb0, 0x00, 0xE1, 0x02, 0x00, 0x01]

# Card Issuer
CMD_ISSUER = [0x80, 0xb0, 0x00, 0xF6, 0x02, 0x00, 0x64]

# Issue Date
CMD_ISSUE = [0x80, 0xb0, 0x01, 0x67, 0x02, 0x00, 0x08]

# Expire Date
CMD_EXPIRE = [0x80, 0xb0, 0x01, 0x6F, 0x02, 0x00, 0x08]

# Address
CMD_ADDRESS = [0x80, 0xb0, 0x15, 0x79, 0x02, 0x00, 0x64]

# Define photo commands
CMD_PHOTO = [0x80, 0xb0, 0x00, 0x78, 0x02, 0x00, 0xFF]

# Get all the available readers
readerList = readers()
print("Available readers:")
for readerIndex, readerItem in enumerate(readerList):
    print(readerIndex, readerItem)

# Select reader
readerSelectIndex = 0

reader = readerList[readerSelectIndex]
print("Using:", reader)

connection = reader.createConnection()
connection.connect()
atr = connection.getATR()
print("ATR:", toHexString(atr))
req = [0x00, 0xc0, 0x00, 0x01] if atr[0] == 0x3B and atr[1] == 0x67 else [0x00, 0xc0, 0x00, 0x00]

# Check card
data, sw1, sw2 = connection.transmit(SELECT + THAI_CARD)
print(f"Select Applet: {sw1:02X} {sw2:02X}")

# CID
data = get_data(CMD_CID, req)
cid = thai2unicode(data[0])
print("CID:", cid)

# TH Fullname
data = get_data(CMD_THFULLNAME, req)
print("TH Fullname:", thai2unicode(data[0]))

# EN Fullname
data = get_data(CMD_ENFULLNAME, req)
print("EN Fullname:", thai2unicode(data[0]))

# Date of birth
data = get_data(CMD_BIRTH, req)
print("Date of birth:", thai2unicode(data[0]))

# Gender
data = get_data(CMD_GENDER, req)
print("Gender:", thai2unicode(data[0]))

# Card Issuer
data = get_data(CMD_ISSUER, req)
print("Card Issuer:", thai2unicode(data[0]))

# Issue Date
data = get_data(CMD_ISSUE, req)
print("Issue Date:", thai2unicode(data[0]))

# Expire Date
data = get_data(CMD_EXPIRE, req)
print("Expire Date:", thai2unicode(data[0]))

# Address
data = get_data(CMD_ADDRESS, req)
print("Address:", thai2unicode(data[0]))

# PHOTO
photo_data = b''
for i in range(1, 21):
    cmd_photo = CMD_PHOTO[:]
    cmd_photo[4] = i
    # photo_data += get_data(cmd_photo, req)[0]
    temp_data = get_data(cmd_photo, req)[0]

with open(f"{cid}.jpg", "wb") as f:
    f.write(photo_data)

# Exit program
sys.exit()