class UnauthorizedException(Exception):
  def __init__(self, message: str = "Unauthorized", status_code: int = 401):
    super().__init__(message)
    self.status_code = status_code
    self.message = message