from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseTemplate(ABC, Generic[T]):
    @abstractmethod
    def render(self, context: T) -> None:
        """Render the template with the given context."""
        raise NotImplementedError

    @abstractmethod
    def generate(self) -> None:
        """Generate the template."""
        raise NotImplementedError
