# -*- coding: utf-8 -*-

"""
Created on 03.01.2020
:author: goodmice
Содержит класс логгера с настроенными цветами и выводом
"""

import datetime
import logging as lg
from typing import NoReturn
from app.utils.colors import TerminalColors


class GM_ConsoleFormatter(lg.Formatter):
    """ Форматирование для настройки логгера """

    def __init__(self, c: str):
        """
        Конструктор класса GM_ConsoleFormatter

        :param str c: Экземпляр класса цветного вывода

        :return:
        :rtype: GM_ConsoleFormatter
        """

        self.c = c
        lg.Formatter.__init__(self, self.fmt())

    def format(self, record: lg.LogRecord) -> str:
        """
        Изменённая функция format

        :param lg.LogRecord record: Запись для форматирования

        :return: Результат форматирования
        :rtype: str
        """

        self._style = lg.PercentStyle(self.fmt(record.levelno))
        result = lg.Formatter.format(self, record)
        self._style = lg.PercentStyle(self._fmt)
        return result

    def fmt(self, level: int = lg.DEBUG) -> str:
        """
        Форматирование шаблона для вывода записей лога

        :param int level: Слой логгирования

        :return: строковый шаблон форматирования
        :rtype: str
        """

        out = self.c.h(r"%(levelname)s")
        if level == lg.INFO:
            out = self.c.og(r"INFO ")
        elif level == lg.WARNING or level == lg.WARN:
            out = self.c.w(r"WARN ")
        elif level == lg.ERROR:
            out = self.c.f(r"ERROR")
        return f'[{out}] {self.c.ob(r"%(name)s")}: %(message)s'


class GM_Logger(lg.Logger):
    """ Настроенный под проект логгер """

    def __init__(self, name: str, withoutcolors: bool = False):
        """
        Конструктор класса CustomLogger

        :param str name: Название логгера
        :param bool withoutcolors: Не имеет ли лог цветов

        :return: Экземпляр настроенного логгера
        :rtype: CustomLogger
        """

        super().__init__(name)
        self.c = TerminalColors()
        if withoutcolors:
            self.c.disable()
        self.console_setup()
        self.file_setup()

    def console_setup(self) -> NoReturn:
        """ Настройка для вывода в консоль """

        handler = lg.StreamHandler()
        handler.setLevel(lg.DEBUG)
        hformat = GM_ConsoleFormatter(self.c)
        handler.setFormatter(hformat)
        self.addHandler(handler)

    def file_setup(self) -> NoReturn:
        """ Настройка для вывода в файл """

        now = datetime.datetime.now()
        handler = lg.FileHandler(now.strftime(r'./logs/%Y-%m-%d.log'), encoding='utf-8')
        handler.setLevel(lg.DEBUG)
        hformat = lg.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s: %(message)s')
        handler.setFormatter(hformat)
        self.addHandler(handler)
