from abc import ABCMeta, abstractmethod


class BaseView(metaclass=ABCMeta):
    @abstractmethod
    def data_merge(self):
        pass

    @abstractmethod
    def get_view(self):
        pass
