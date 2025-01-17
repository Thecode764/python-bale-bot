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
from typing import Optional
from bale import BaleObject
from bale.utils.types import MissingValue

__all__ = (
    "Contact",
)

class Contact(BaleObject):
    """This object shows a Contact.

    Attributes
    ----------
        phone_number: int
            Contact’s phone number.
        first_name: str
            Contact’s first name.
        last_name: :obj:`str`, optional
            Contact’s last name.
        user_id: :obj:`int`, optional
            Contact’s user identifier in Bale.
    """
    __slots__ = (
        "phone_number",
        "first_name",
        "last_name",
        "user_id"
    )

    def __init__(self, phone_number: int, first_name: str, last_name: Optional[str] = MissingValue, user_id: Optional[int] = MissingValue) -> None:
        super().__init__()
        self._id = user_id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

        self._lock()
