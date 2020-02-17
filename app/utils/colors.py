# -*- coding: utf-8 -*-

"""
Created on 03.01.2020
:author: goodmice
Содержит класс для работы с цветами в консоли
"""

from typing import NoReturn


class TerminalColors:
    """ Содержит константы и функции для работы с цветами в консоли """

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self) -> NoReturn:
        """ Выключает цвета """

        self.HEADER = self.OKBLUE = \
            self.OKGREEN = self.WARNING = self.FAIL = self.ENDC = ''

    def ob(self, text: str) -> str:
        """
        Выводит синий текст

        :param str text: входящий текст

        :return: цветной текст
        :rtype: str
        """

        return self.OKBLUE + text + self.ENDC

    def og(self, text: str) -> str:
        """
        Выводит зелёный текст

        :param str text: входящий текст

        :return: цветной текст
        :rtype: str
        """

        return self.OKGREEN + text + self.ENDC

    def h(self, text: str) -> str:
        """
        Выводит текст-заголовок

        :param str text: входящий текст

        :return: цветной текст
        :rtype: str
        """

        return self.HEADER + text + self.ENDC

    def w(self, text: str) -> str:
        """
        Выводит текст-предупреждение

        :param str text: входящий текст

        :return: цветной текст
        :rtype: str
        """

        return self.WARNING + text + self.ENDC

    def f(self, text: str) -> str:
        """
        Выводит текст-ошибку

        :param str text: входящий текст

        :return: цветной текст
        :rtype: str
        """

        return self.FAIL + text + self.ENDC
