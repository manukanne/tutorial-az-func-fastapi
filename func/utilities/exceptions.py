class ApiException(Exception):
    """
    Generic API Exception
    """
    def __init__(self, *, status_code: int, code: str, description: str) -> None:
        """
        API exception constructor
        Args:
            status_code (int): HTTP status code
            code (str): Error code
            description (str): Error description
        """
        self.status_code = status_code
        self.code = code
        self.description = description


class EntityNotFoundException(ApiException):
    """
    Entity not found exception
    """
    def __init__(self, *, code: str, description: str) -> None:
        """_summary_

        Args:
            code (str): Entity name
            description (str): Error description
        """
        super().__init__(status_code=404, code=code, description=description)
