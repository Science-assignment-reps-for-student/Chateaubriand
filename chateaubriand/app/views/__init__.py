from abc import ABCMeta, abstractmethod


class BaseView(metaclass=ABCMeta):
    @abstractmethod
    def get_data():
        pass
    
    @abstractmethod
    def get_view():
        pass
    