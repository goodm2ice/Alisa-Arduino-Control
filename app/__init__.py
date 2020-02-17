# -*- coding: utf-8 -*-

"""
Created on 16.02.2020
:author: goodmice
Главный файл сервера для тестового навыка алисы
"""

from __future__ import unicode_literals
from flask import Flask, request
from app.utils.log import GM_Logger
from app.utils.alice_sdk import AliceRequest, AliceResponse
from app.handlers import handle_dialog

app = Flask(__name__)
log = GM_Logger(__name__, True)

@app.route("/", methods=["POST"])
def main():    
    alice_req = AliceRequest(request.json)
    alice_res = AliceResponse(alice_req)

    alice_res = handle_dialog(alice_req, alice_res)

    log.info(alice_res)

    return alice_res.dumps()
