class InputError(Exception):
    """
    Creating class for custom errors inherited from Exception class
    """
    def __init__(self, message):
        """
        :parameter message: it is inherited from Exception class
        :param message:
        """
        super().__init__(message)
