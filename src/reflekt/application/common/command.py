from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

CRes = TypeVar("CRes")
C = TypeVar("C", bound="Command")


@dataclass
class Command(ABC): ...


class CommandHandler(ABC, Generic[C, CRes]):
    @abstractmethod
    async def __call__(self, query: C) -> CRes: ...
