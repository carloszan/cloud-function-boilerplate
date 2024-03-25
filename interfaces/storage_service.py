from abc import ABC, abstractmethod


class StorageService(ABC):
    @abstractmethod
    def download_file(self, folder: str, file: str) -> str:
        pass

    @abstractmethod
    def upload_file(self, folder: str, file: str) -> None:
        pass
