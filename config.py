# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

    if not getenv("BOT_TOKEN") or not getenv("BOT_TOKEN").count(":") == 1:
        print("Error: BOT_TOKEN must be in format '123456:abcdefghijklmnopqrstuvwxyz'")
        exit(1)

    if (
        not getenv("SESSION_STRING")
        or getenv("SESSION_STRING") == "xxxxxxxxxxxxxxxxxxxxxxx"
    ):
        print("Error: SESSION_STRING must be set with a valid string")
        exit(1)


# Pyrogram setup
class PyroConf(object):
    API_ID = int(getenv("API_ID", "21840825"))
    API_HASH = getenv("API_HASH", "83398eab5af8c8392bc3034f2974299e")
    BOT_TOKEN = getenv("BOT_TOKEN", "7944120107:AAE71kJhUiXr4PwNIfdOVI_XZwFF5kYXnUs")
    SESSION_STRING = getenv("SESSION_STRING", "BQFNQ7kAmWo2l0lNwdPzfzDtuq2VcCRXin3jDIQKSeGIxVgehJU4fmbsQibi6E_llqREasr7Q_CoxsQLlug2d2RoIDVU5yaNoYG_lgPJV-F3PK-RV8Q6hzEKZvvvEdLD_rKu5GYDmIVikusJk4hCP1AXjk_qWuH4hG4sIGVql_CfMDOrykIjy1I87zpAtIDDDnhkCXw4HWPy4zw1Qp5QvoLupzo-CNu4UxFbX4Qu4_nD08LufMt3iVk73PxUWGEW3WFgwsu0NmtfjR0EKZl-3XhlXl0cWCKTL9EHmEfjE1P2SbG1r8fWBk2oOaJZrFfupgC0amFnTUUvtPDerzQMxcj8ol6RdAAAAAGtMapdAA")
    BOT_START_TIME = time()
