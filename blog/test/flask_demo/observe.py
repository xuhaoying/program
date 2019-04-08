
class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        