class BingException(Exception):
    """A generic exception for all bing-related exceptions. You can catch all exceptions with this."""
    pass

class BadAuth(BingException):
    """An invalid authorization was passed in"""
    pass

class NotEnoughResults(BingException):
    """There weren't enough results."""
    pass
