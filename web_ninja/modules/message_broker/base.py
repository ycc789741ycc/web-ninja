from abc import ABC, abstractmethod
from typing import Dict, Callable


class BaseEventBroker(ABC):
    """Base class for event brokers"""

    def __init__(self, topic_name: str, *args, **kwargs) -> None:
        self.topic_name = topic_name

    @abstractmethod
    def publish(
        self,
        event_name: str,
        payload: Dict,
    ) -> None:
        """Publishes an event to the broker"""

        raise NotImplementedError

    @classmethod
    @abstractmethod
    def set_consumer_subscription(
        cls,
        event_name: str,
        event_handler: Callable,
        *args,
        retries: int = 3,
        retry_delay_in_seconds: float = 5,
        task_time_limit_in_seconds: int = 300,
        **kwargs
    ) -> None:
        """Subscribes to an event
        Args:
            event_name (str): The name of the event
            event_handler (Callable): The event handler
        """

        raise NotImplementedError
