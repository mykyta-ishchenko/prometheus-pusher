class BasePusherException(Exception):
    message: str = "An error occurred in the Prometheus Pusher library."

    def __init__(self, message: str = None):
        super().__init__(message or self.message)
