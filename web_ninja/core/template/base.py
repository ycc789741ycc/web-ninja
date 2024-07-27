from abc import ABC, abstractmethod
from typing import Dict


class BaseTemplate(ABC):
    @abstractmethod
    def render(self, context: Dict[str, str]) -> None:
        """Render the template with the given context."""
        raise NotImplementedError

    @abstractmethod
    def generate(self) -> None:
        """Generate the template."""
        raise NotImplementedError
