from typing import Dict, Callable

from celery import Celery

from .base import BaseEventBroker


class CeleryEventBroker(BaseEventBroker):
    def __init__(self, topic_name: str, celery: Celery, *args, **kwargs) -> None:
        super().__init__(topic_name, *args, **kwargs)
        self.celery = celery

    def publish(self, event_name: str, payload: Dict) -> None:
        self.celery.send_task(event_name, kwargs=payload, queue=self.topic_name)

    @classmethod
    def set_consumer_subscription(
        cls,
        event_name: str,
        event_handler: Callable,
        celery: Celery,
        retries: int = 3,
        retry_delay_in_seconds: float = 5,
        task_time_limit_in_seconds: int = 300,
    ) -> None:
        celery.task(
            name=event_name,
            acks_late=True,
            reject_on_worker_lost=False,
            retry_kwargs={'max_retries': retries, 'countdown': retry_delay_in_seconds, 'time_limit': task_time_limit_in_seconds},
        )(event_handler)
