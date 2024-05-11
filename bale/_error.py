# An API wrapper for Bale written in Python
# Copyright (c) 2022-2024
# Kian Ahmadian <devs@python-bale-bot.ir>
# All rights reserved.
#
# This software is licensed under the GNU General Public License v2.0.
# See the accompanying LICENSE file for details.
#
# You should have received a copy of the GNU General Public License v2.0
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-2.0.html>.
from __future__ import annotations
from typing import Optional, Any, Tuple, Type, TYPE_CHECKING

from bale.utils.request import ResponseStatusCode
if TYPE_CHECKING:
    from bale.request.parser import ResponseParser

__all__ = (
    "HTTPClientError",
    "BaleError",
    "InvalidToken",
    "APIError",
    "NetworkError",
    "TimeOut",
    "NotFound",
    "Forbidden",
    "BadRequest",
    "RateLimited",
    "HTTPException",
    "__ERROR_CLASSES__"
)

class HTTPClientError:
    USER_OR_CHAT_NOT_FOUND = "no such group or user"
    TOKEN_NOT_FOUND = "Bad Request: Token not found"
    RATE_LIMIT = "bot limit exceed"
    LOCAL_RATE_LIMIT = "local_rate_limited"
    PERMISSION_DENIED = "permission_denied"

class BaleError(Exception):
    """
    Base exception class for python-bale-bot

    Attributes
    ------------
    message: :obj:`str`
        The text of the error. Could be an `None`.
    """
    __slots__ = ("message",)
    STATUS_CODE = None

    @staticmethod
    def check_response(response: Optional["ResponseParser"]) -> bool:
        return BaleError.check_description(response.description)

    @staticmethod
    def check_description(description: Optional[str]) -> bool:
        return False

    def __init__(self, message: Any) -> None:
        super().__init__()
        self.message = message

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.message}"

    def __reduce__(self):
        return self.__class__, (self.message,)


class InvalidToken(BaleError):
    """
    An exception where the server says the Token is Invalid
    """
    __slots__ = ("_message",)

    def __init__(self, message=None) -> None:
        super().__init__(message or "Invalid Token")

    @staticmethod
    def check_description(description: Optional[str]) -> bool:
        return description and "token not found" in description.lower()

class APIError(BaleError):
    """
    Exception that's raised for when status code 400 occurs and Error is Unknown.
    Subclass of :exc:`BaleError`
    """
    __slots__ = ()

    def __init__(self, error_code, message) -> None:
        super().__init__(f"{error_code}: {message}")


class NetworkError(BaleError):
    """
    Exception that's raised when the connection is
    closed for reasons that could not be handled internally.
    """
    __slots__ = ()


class TimeOut(BaleError):
    __slots__ = ()

    def __init__(self) -> None:
        super().__init__("Time Out")


class NotFound(BaleError):
    """
    Exception that's raised for when status code 404 occurs.
    Subclass of :exc:`BaleError`
    """
    __slots__ = ()
    STATUS_CODE = ResponseStatusCode.NOT_FOUND

    def __init__(self, message=None) -> None:
        super().__init__(message or "Not Found")

    @staticmethod
    def check_description(description: Optional[str]) -> bool:
        return description and HTTPClientError.USER_OR_CHAT_NOT_FOUND in description

class Forbidden(BaleError):
    """
    Exception that's raised for when status code 403 occurs.
    Subclass of :exc:`BaleError`
    """
    __slots__ = ()
    STATUS_CODE = ResponseStatusCode.PERMISSION_DENIED

    def __init__(self, err=None) -> None:
        super().__init__(err)

    @staticmethod
    def check_description(description: Optional[str]) -> bool:
        return description and description.startswith("Forbidden:")

class BadRequest(BaleError):
    """
    Exception that's raised for when Bale server say Bad Request.
    Subclass of :exc:`BaleError`
    """
    __slots__ = ()

    def __init__(self, err: Any) -> None:
        super().__init__(err)

    @staticmethod
    def check_description(description: Optional[str]) -> bool:
        return description and description.startswith("Bad Request:")

class RateLimited(BaleError):
    """
    Exception that's raised for when Rate Limits.
    Subclass of :exc:`BaleError`
    """
    __slots__ = ()
    STATUS_CODE = ResponseStatusCode.RATE_LIMIT

    def __init__(self) -> None:
        super().__init__("We are Rate Limited")

class HTTPException(BaleError):
    """
    Exception that's raised when an HTTP request operation fails.
    """
    __slots__ = ()

    def __init__(self, err: Any) -> None:
        super().__init__(err)


__ERROR_CLASSES__: Tuple[Type[BaleError], ...] = (
    BaleError,
    InvalidToken,
    APIError,
    NetworkError,
    TimeOut,
    NotFound,
    Forbidden,
    BadRequest,
    RateLimited,
    HTTPException
)