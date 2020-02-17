# -*- coding: utf-8 -*-

"""
Created on 16.02.2020
:author: goodmice
Главный файл сервера для тестового навыка алисы
"""

from __future__ import unicode_literals
import json
from re import findall, match
from typing import List
import Levenshtein as lsh
from app.utils.log import GM_Logger

log = GM_Logger(__name__)

config = {}
ALL_SYNONIMS = []
with open("config.json", encoding="utf8") as file:
    config = json.loads(file.read())
for syn in config["synonims"].values():
    ALL_SYNONIMS += syn

def hasOneOf(arr_base : List[str], arr_find : List[str]) -> bool:
    for elem1 in arr_find:
        for elem2 in arr_base:
            if lsh.ratio(elem1, elem2) > config["ratios"][elem2]:
                print(elem1, elem2, lsh.ratio(elem1, elem2))
                return True
    return False

def handle_dialog(request, response):
    req_text = request.command.lower().strip()

    if req_text.startswith('gm_0910 '):
        config['users'][request.user_id] = req_text.split()[1]
        with open("config.json", "w", encoding="utf8") as file:
            json.dump(config, fp=file)

        response.set_text(f'Добавлен пользователь дома {req_text.split()[1]}')
        return response

    if not request.user_id in config['users']:
        response.set_text('Неизвестный пользователь!')
        return response

    if request.is_new_session:
        response.set_text('Включён режим управления arduino!')
        return response

    house_id = config["users"][request.user_id]
    user_message = request.command.lower().strip().split()

    response.set_text(f"{request.command}\n\n")
    if hasOneOf(ALL_SYNONIMS, user_message):
        for room, elems in config["houses"][house_id].items():
            if hasOneOf(config["synonims"][room], user_message):
                for elem, states in elems.items():
                    if hasOneOf(config["synonims"][elem], user_message):
                        for state in states:
                            if hasOneOf(config["synonims"][state], user_message):
                                cmd = config["houses"][house_id]["command_template"].format(room=room, elem=elem, state=state)
                                response.set_text(f"{response}Будет выполнена команда: {cmd}\n")
                                break
        return response

    response.set_text("Команда не найдена!")
    return response