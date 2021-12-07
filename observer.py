from abc import ABC, abstractmethod

class Observer(ABC):
    '''
    Define an updating interface for objects that should be notified of
    changes in a observable. This implementation automatically registers the observer(subscriber)
    to the observable(publisher). No exceptions raised
    '''

    @abstractmethod
    def __init__(self, observable):
        '''Automatically registers to the observable. Pass in observable to register'''
        observable.add_observer(self)

    @abstractmethod
    def notify(self, state_change):
        '''Alert the subject of interest, and pass in the state_change'''
