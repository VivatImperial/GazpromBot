class CommandKey:

    @classmethod
    def key(cls):
        return 111

    @classmethod
    def __str__(cls):
        return 'информация о поиске по ключу'


class CommandFilter:

    @classmethod
    def filter(cls):
        return 222

    @classmethod
    def __str__(cls):
        return 'информация о поиске по фильтру'

