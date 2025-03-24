import socket
import threading
import uuid
from typing import Any

from prometheus_client import CollectorRegistry, push_to_gateway


class PrometheusPusher:
    def __init__(
        self,
        gateway_url: str = "http://localhost:9091",
        job_name: str = "python_app",
        push_interval: int = 60,
        registry: CollectorRegistry = None,
        grouping_labels: dict[str, Any] = None,
    ):
        self.gateway_url = gateway_url
        self.job_name = job_name
        self.push_interval = push_interval
        self.registry = registry or CollectorRegistry()
        self.worker_id = str(uuid.uuid4())
        self.grouping_labels = {
            "instance": socket.gethostname(),
            "worker_id": self.worker_id,
            **(grouping_labels or {}),
        }
        self._stop_event = threading.Event()
        self._thread = None

    def push_loop(self) -> None:
        while not self._stop_event.is_set():
            push_to_gateway(
                self.gateway_url,
                job=self.job_name,
                registry=self.registry,
                grouping_key=self.grouping_labels,
            )
            self._stop_event.wait(self.push_interval)

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return

        self._thread = threading.Thread(target=self.push_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if self._thread and self._thread.is_alive():
            self._stop_event.set()
            self._thread.join()
