from abc import ABC, abstractmethod


class ApiService(ABC):
    @abstractmethod
    def batch_insert_people(self, people):
        pass

    @abstractmethod
    def batch_update_people(self, people):
        pass
