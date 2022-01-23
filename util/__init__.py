"""Package containing utility modules that perform specific tasks."""

# Standard library imports
import traceback


def format_exception_info(exception: Exception):
    """Returns the exception stack trace in the form of a string as it is displayed in the shell.

    Arguments:
        exception -- the exception to format.
    """
    info = type(exception), exception, exception.__traceback__
    fmt_info = traceback.format_exception(*info)
    return ''.join(fmt_info)
