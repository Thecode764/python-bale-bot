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
from bale import BaleObject, User, ChatPhoto, Document, PhotoSize, Video, Animation, Audio
from bale.utils.types import FileInput, MediaInput, MissingValue, OptionalParam
from typing import TYPE_CHECKING, Optional, List, Union, ClassVar, Dict

if TYPE_CHECKING:
    from bale import Message, InlineKeyboardMarkup, MenuKeyboardMarkup, LabeledPrice, Location, Contact, Sticker


__all__ = (
    "Chat",
)

class Chat(BaleObject):
    """This object indicates a chat.

    Attributes
    ----------
        id: :obj:`str`
            Unique identifier for this chat.
        type: :obj:`str`
            Type of chat.
        title: :obj:`str`, optional
            Title, for channels and group chats.
        username: :obj:`str`, optional
            Username, for private chats, supergroups and channels if available.
        first_name: :obj:`str`, optional
            First name of the other party in a private chat.
        last_name: :obj:`str`, optional
            Last name of the other party in a private chat.
        photo: :class:`bale.ChatPhoto`, optional
            Chat photo.
        invite_link: :obj:`str`, optional
            Primary invite link, for groups and channel. Returned only in :meth:`bale.Bot.get_chat()`.
    """
    PRIVATE: ClassVar[str] = "private"
    GROUP: ClassVar[str] = "group"
    CHANNEL: ClassVar[str] = "channel"
    __slots__ = (
        "__weakref__",
        "id",
        "type",
        "title",
        "username",
        "first_name",
        "last_name",
        "photo",
        "pinned_message",
        "all_members_are_administrators",
        "invite_link",
        "bot"
    )

    def __init__(self, chat_id: int, chat_type: str, title: OptionalParam[str] = MissingValue, username: OptionalParam[str] = MissingValue,
                 first_name: OptionalParam[str] = MissingValue, last_name: OptionalParam[str] = MissingValue, photo: OptionalParam["ChatPhoto"] = MissingValue,
                 invite_link: OptionalParam[str] = MissingValue) -> None:
        super().__init__()
        self._id = chat_id
        self.id = chat_id
        self.type = chat_type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.photo = photo
        self.invite_link = invite_link

        self._lock()
        
    @property
    def is_private_chat(self) -> bool:
        return self.type == self.PRIVATE
    
    @property
    def is_group_chat(self) -> bool:
        return self.type == self.GROUP

    @property
    def is_channel_chat(self) -> bool:
        return self.type == self.CHANNEL

    async def send(self, text: str, components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue, delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_message(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_message`.

        .. hint::
            .. code:: python

                await chat.send("hi, python-bale-bot!", components = None)
        """
        return await self.get_bot().send_message(self.id, text, components=components, delete_after=delete_after)

    async def send_document(self, document: Union["Document", FileInput], *, caption: OptionalParam[str] = MissingValue,
                            components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                            delete_after: Optional[Union[float, int]] = None, file_name: OptionalParam[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_document(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_document`.

        .. hint::
            .. code:: python

                await chat.send_document(bale.InputFile("FILE_ID"), caption = "this is caption", ...)
        """
        return await self.get_bot().send_document(self.id, document, caption=caption, components=components, delete_after=delete_after, file_name=file_name)

    async def send_photo(self, photo: Union["PhotoSize", FileInput], *, caption: OptionalParam[str] = MissingValue,
                         components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                         delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_photo(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_photo`.

        .. hint::
            .. code:: python

                await chat.send_photo(bale.InputFile("FILE_ID"), caption = "this is caption", ...)
        """
        return await self.get_bot().send_photo(self.id, photo, caption=caption, components=components, delete_after=delete_after, file_name=file_name)

    async def send_video(self, video: Union["Video", FileInput], *, caption: OptionalParam[str] = MissingValue,
                         components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                         delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_video(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_video`.

        .. hint::
            .. code:: python

                await chat.send_video(bale.InputFile("FILE_ID"), caption = "this is caption", ...)
        """
        return await self.get_bot().send_video(self.id, video, caption=caption, components=components, delete_after=delete_after, file_name=file_name)

    async def send_animation(self, animation: Union["Animation", FileInput], *, duration: OptionalParam[int] = MissingValue, width: OptionalParam[int] = MissingValue,
                             height: OptionalParam[int] = MissingValue, caption: OptionalParam[str] = MissingValue,
                             components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                             delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_animation(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_animation`.

        .. hint::
            .. code:: python

                await chat.send_animation(bale.InputFile("FILE_ID"), caption = "this is caption", ...)
        """
        return await self.get_bot().send_animation(self.id, animation, duration=duration, width=width, height=height, caption=caption, components=components,
                                                   delete_after=delete_after, file_name=file_name)

    async def send_audio(self, audio: Union["Audio", FileInput], *, caption: OptionalParam[str] = MissingValue,
                         components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                         delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_audio(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_audio`.

        .. hint::
            .. code:: python

                await chat.send_audio(bale.InputFile("FILE_ID"), caption = "this is caption", ...)
        """
        return await self.get_bot().send_audio(self.id, audio, caption=caption, components=components, delete_after=delete_after, file_name=file_name)

    async def send_location(self, location: "Location", delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_location(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_location`.

        .. hint::
            .. code:: python

                await chat.send_location(bale.Location(35.71470468031143, 51.8568519168293))
        """
        return await self.get_bot().send_location(self.id, location, delete_after=delete_after)

    async def send_contact(self, contact: "Contact", delete_after: Optional[Union[float, int]] = None) -> "Message":
        """
        Shortcut method for:

        .. code:: python

            await bot.send_contact(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_contact`.

        .. hint::
            .. code:: python

                await chat.send_contact(Contact('09****', 'first name', 'last name))
        """
        return await self.get_bot().send_contact(self.id, contact, delete_after=delete_after)

    async def send_invoice(self, title: str, description: str, provider_token: str, prices: List["LabeledPrice"], *,
                   payload: OptionalParam[str] = MissingValue, photo_url: OptionalParam[str] = MissingValue, need_name: OptionalParam[bool] = MissingValue,
                   need_phone_number: OptionalParam[bool] = MissingValue, need_email: OptionalParam[bool] = MissingValue,
                   need_shipping_address: OptionalParam[bool] = MissingValue, is_flexible: OptionalParam[bool] = MissingValue,
                   delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_invoice(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_invoice`.

        .. hint::
            .. code:: python

                await chat.send_invoice(
                    "invoice title", "invoice description", "6037************", [bale.LabeledPrice("label", 2000)],
                    payload = "unique invoice payload", ...
                )
        """
        return await self.get_bot().send_invoice(self.id, title, description, provider_token, prices,
                                        invoice_payload=payload, photo_url=photo_url, need_name=need_name, need_email=need_email,
                                        need_phone_number=need_phone_number, need_shipping_address=need_shipping_address, is_flexible=is_flexible,
                                        delete_after=delete_after)

    async def copy_message(self, chat_id: Union[int, str], message_id: Union[int, str], reply_to_message_id: OptionalParam[str, int] = MissingValue,
                           delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.copy_message(
                from_chat_id=chat.id, message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.copy_message`.

        .. hint::
            .. code:: python

                await chat.copy_message(
                    1234, 1234
                )
        """
        return await self.get_bot().copy_message(chat_id, self.id, message_id, reply_to_message_id=reply_to_message_id, delete_after=delete_after)

    async def send_sticker(self, sticker: Union["Sticker", FileInput], *, delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_sticker(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_sticker`.

        .. hint::
            .. code:: python

                await chat.send_sticker("FILE_ID", ...)
        """
        return await self.get_bot().send_sticker(self.id, sticker, delete_after=delete_after)

    async def send_media_group(self, media: List[MediaInput], *,
                    components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_media_group(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_media_group`.

        .. hint::
            .. code:: python

                await chat.send_media_group([
                    InputMediaPhoto("File ID", caption="example caption"),
                    InputMediaPhoto("File ID"),
                    InputMediaPhoto("File ID")
                ], ...)
        """
        return await self.get_bot().send_media_group(self.id, media, components=components)

    async def leave(self):
        """
        Shortcut method for:

        .. code:: python

            await bot.leave_chat(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the method, please see :meth:`bale.Bot.leave_chat`.

        .. hint::
            .. code:: python

                chat = await bot.get_chat(1234)
                await chat.leave()
        """
        await self.get_bot().leave_chat(self.id)

    async def add_user(self, user: Union["User", str, int]):
        """
        Shortcut method for:

        .. code:: python

            await bot.invite_user(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.invite_user`.

        .. hint::
            .. code:: python

                user = await bot.get_user(1234)
                await chat.add_user(user)
        """
        if isinstance(user, User):
            user = user.user_id

        await self.get_bot().invite_user(self.id, user)

    async def get_member(self, user: Union["User", str, int]):
        """
        Shortcut method for:

        .. code:: python

            await bot.get_chat_member(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.get_chat_member`.

        .. hint::
            .. code:: python

                user = await bot.get_user(1234)
                await chat.get_member(user)
                ...
                await chat.get_member(1234)
        """
        if isinstance(user, User):
            user = user.user_id

        return await self.get_bot().get_chat_member(self.id, user_id=user)

    async def ban_member(self, user: Union["User", str, int]):
        """
        Shortcut method for:

        .. code:: python

            await bot.ban_chat_member(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.ban_chat_member`.

        .. hint::
            .. code:: python

                user = await bot.get_user(1234)
                await chat.ban_member(user)
                ...
                await chat.ban_member(1234)
        """
        if isinstance(user, User):
            user = user.user_id

        return await self.get_bot().ban_chat_member(self.id, user)

    async def unban_member(self, user: Union["User", str, int], *, only_if_banned: OptionalParam[bool] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.unban_chat_member(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.unban_chat_member`.

        .. hint::
            .. code:: python

                user = await bot.get_user(1234)
                await chat.unban_member(user)
                ...
                await chat.unban_member(1234)
        """
        if isinstance(user, User):
            user = user.user_id

        return await self.get_bot().unban_chat_member(self.id, user, only_if_banned=only_if_banned)

    async def set_photo(self, photo: Union[PhotoSize, FileInput]):
        """
        Shortcut method for:

        .. code:: python

            await bot.set_chat_photo(
                chat_id=chat.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.set_chat_photo`.

        .. hint::
            .. code:: python

                await chat.set_photo(bale.InputFile("FILE_ID"))
        """
        return await self.get_bot().set_chat_photo(self.id, photo)

    async def get_members_count(self):
        """
        Shortcut method for:

        .. code:: python

            await bot.get_chat_members_count(
                chat_id=chat.id
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.get_chat_members_count`.

        .. hint::
            .. code:: python

                await chat.get_members_count()
        """
        return await self.get_bot().get_chat_members_count(self.id)

    async def get_administrators(self):
        """
        Shortcut method for:

        .. code:: python

            await bot.get_chat_administrators(
                chat_id=chat.id
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.get_chat_administrators`.

        .. hint::
            .. code:: python

                await chat.get_administrators()
        """
        return await self.get_bot().get_chat_administrators(self.id)

    @classmethod
    def from_dict(cls, data: Optional[Dict], bot):
        data = BaleObject.parse_data(data)
        if not data:
            return None

        data["chat_id"] = data.pop("id")
        data["chat_type"] = data.pop("type")
        data["photo"] = ChatPhoto.from_dict(data.get('photo'), bot)

        return super().from_dict(data, bot)
