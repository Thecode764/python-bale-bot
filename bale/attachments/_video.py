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
from ._basefile import BaseFile
from bale.utils.types import MissingValue

__all__ = (
    "Video",
)

class Video(BaseFile):
    """This object shows a Video.

    Attributes
    ----------
        file_id: :obj:`str`
            Identifier for this file, which can be used to download or reuse the file.
        file_unique_id: :obj:`str`
            Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.
        width: int
            Video width as defined by sender.
        height: str
            Video height as defined by sender.
        duration: int
            Duration of the video in seconds as defined by sender.
        file_name: :obj:`str`, optional
            Original video filename as defined by sender.
        mime_type: :obj:`str`, optional
            MIME type of file as defined by sender.
        file_size: :obj:`int`, optional
            File size in bytes, if known.
    """
    __slots__ = (
        "width",
        "height",
        "duration",
        "file_name",
        "mime_type"
    )

    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, duration: int, file_name: Optional[str] = MissingValue,
                 mime_type: Optional[str] = MissingValue, file_size: Optional[int] = MissingValue):
        super().__init__(file_id, file_unique_id, file_size)

        self.width = width
        self.height = height
        self.duration = duration
        self.file_name = file_name
        self.mime_type = mime_type

        self._lock()