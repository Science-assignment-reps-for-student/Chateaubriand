from abc import ABCMeta, abstractmethod


class BaseView(metaclass=ABCMeta):
    @abstractmethod
    def query_to_db(self):
        pass

    @abstractmethod
    def get_view(self):
        pass
