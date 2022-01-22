# About
Corny Commons is a Python package containing modules for use by MagicalCornFlake. They are used projects such as Dzwonnik 2 and other private work-in-progress projects.

# Packages
There is currently one package inside Corny Commons; the `util` package. 

## 1. util.py
As you can guess, this package contains utility-oriented modules.

### a) web.py
The `web` module implements functionality for creating web requests. It is used in various web APIs that must retrieve information from an external source. In essence, this module is a wrapper around the built-in `requests` module.

`make_request` -- takes a URL and creates a web request to that address. If the function has been called before the maximum request cooldown has passed, `web.TooManyRequestsException` is raised. Otherwise, the request is made. If the response is not retrieved within 10 seconds, or if it returns a response with a HTTP code that is not between 200-299, raises `web.InvalidResponseException`. If all checks pass, returns the response object.

`get_html` -- makes a request using the `make_request()` function, then decodes the binary content and returns it as a string.