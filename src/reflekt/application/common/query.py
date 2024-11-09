from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

QRes = TypeVar("QRes")
Q = TypeVar("Q", bound="Query")


@dataclass(frozen=True)
class Query(ABC): ...


class QueryHandler(ABC, Generic[Q, QRes]):
    @abstractmethod
    async def __call__(self, query: Q) -> QRes: ...
