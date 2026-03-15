class NotFoundError(Exception):
    def __init__(self, detail: str = "Resource not found"):
        self.detail = detail


class ForbiddenError(Exception):
    def __init__(self, detail: str = "Access forbidden"):
        self.detail = detail
