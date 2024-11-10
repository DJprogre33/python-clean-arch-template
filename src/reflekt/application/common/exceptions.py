from abc import ABC


class ApplicationLayerError(Exception, ABC):
    @property
    def title(self) -> str:
        return "An application layer error occured"
