from enum import Enum


class VPSStatus(Enum):
    '''Класс для статусов серверов.'''

    STARTED = 'started'
    BLOCKED = 'blocked'
    STOPPED = 'stopped'

    @classmethod
    def choices(cls):
        '''Формирует соответствие для выбора статуса в модели.'''
        return tuple((status.value, status.value) for status in cls)
