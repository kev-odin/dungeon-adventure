class Observable:
    '''
    Observable class that will notify registered observers. Has EC methods for changing
    boolean flag when the state is different. No exceptions raised
    '''

    def __init__(self):
        '''
        Create observable object with empty list and
        boolean flag defaulted to False
        '''
        self._observers = []
        self._changed = False

    def add_observer(self, observer):
        '''Register observer to observable list, pass in observer'''
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        '''Unsubscribe observer from observable, pass in observer'''
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, state_change):
        '''
        Alert observer about state change, and clears flag after method call. State
        change is passed and provided to observers
        '''
        if self.has_changed():
            for observer in self._observers:
                observer.notify(state_change)

        self.clear_changed()

    def clear_changed(self):
        '''Clear change state flag to false'''
        self._changed = False

    def set_changed(self):
        '''Set changed state flag to true'''
        self._changed = True

    def has_changed(self):
        '''Getter for the changed flag'''
        return self._changed

    def count_observers(self):
        '''Return number of observers that are registered'''
        return len(self._observers)
