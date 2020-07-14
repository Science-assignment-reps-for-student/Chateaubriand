from abc import ABCMeta, abstractmethod


class BaseView(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self):
        pass
    
    @abstractmethod
    def get_view(self):
        pass
    