# Kevin's Time Tracker: 0.5 hour

import abc

class Potion(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def action(self):
        pass

    @abc.abstractmethod
    def __potion_effect(self):
        pass

    @abc.abstractproperty
    def name(self):
        pass
