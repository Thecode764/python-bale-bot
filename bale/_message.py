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

from datetime import datetime
from typing import List, Dict, Optional, Union

from bale import (
    BaleObject,
    Chat, User, Document, Contact, Location, PhotoSize, Invoice, InlineKeyboardMarkup,
    MenuKeyboardMarkup, Video, Voice, Audio, Sticker, SuccessfulPayment, Animation,
    InputFile
)
from bale.utils.types import FileInput, AttachmentType, MediaInput, MissingValue, OptionalParam
from .helpers import parse_time


class Message(BaleObject):
    """This object shows a message.

    Attributes
    ----------
        message_id: str
            Unique message identifier inside this chat.
        from_user: :class:`bale.User`, optional
            Sender of the message; empty for messages sent to channels. For backward compatibility, this will contain a
            fake sender user in non-channel chats, if the message was sent on behalf of a chat.

            .. note ::
                :attr:`from_user` is an Aliases for `from`. Because `from` is a reserved character in Python.

        chat: :class:`bale.Chat`
            Conversation the message belongs to.
        date: :class:`datetime.datetime`
            Date the message was sent in Unix time.
        text: :obj:`str`, optional
            Message Content
        caption: :obj:`str`, optional
            Caption for the animation, audio, document, photo, video or voice.
        forward_from: :class:`bale.User`, optional
            For forwarded messages, sender of the original message.
        forward_from_chat: :class:`bale.Chat`, optional
            For messages forwarded from channels or from anonymous administrators, information about the original sender chat.
        reply_to_message: :class:`bale.Message`, optional
            For replies, the original message. Note that the Message object in this field will not contain further
            reply_to_message fields even if it itself is a reply.
        edit_date: :class:`datetime.datetime`, optional
            Date the message was last edited.
        contact: :class:`bale.Contact`, optional
            Message is a shared contact, information about the contact.
        location: :class:`bale.Location`, optional
            Message is a shared location, information about the location.
        document: :class:`bale.Document`, optional
            Message is a general file, information about the file.
        video: :class:`bale.Video`, optional
            Message is a video, information about the video.
        animation: :class:`bale.Animation`, optional
            Message is an animation, information about the animation.
        audio: :class:`bale.Audio`, optional
            Message is an audio, information about the Audio.
        voice: :class:`bale.Voice`, optional
            Message is a voice, information about the Voice.
        sticker: :class:`bale.Sticker`, optional
            Message is a sticker, information about the sticker.
        new_chat_members: List[:class:`bale.User`], optional
            New members that were added to the group or supergroup and information about them (the bot itself may be
            one of these members). This list is empty if the message does not contain new chat members.
        left_chat_member: :class:`bale.User`, optional
            A member was removed from the group, information about them (this member may be the bot itself).
        invoice: :class:`bale.Invoice`, optional
            Message is an invoice for a payment, information about the invoice.
        successful_payment: :class:`bale.SuccessfulPayment`, optional
            Message is a service message about a successful payment, information about the payment.
    """
    __slots__ = (
        "text",
        "caption",
        "from_user",
        "contact",
        "location",
        "chat",
        "message_id",
        "forward_from",
        "forward_from_chat",
        "forward_from_message_id",
        "date",
        "edit_date",
        "audio",
        "voice",
        "document",
        "video",
        "animation",
        "photos",
        "location",
        "sticker",
        "invoice",
        "new_chat_members",
        "left_chat_member",
        "reply_to_message",
        "successful_payment"
    )

    def __init__(self, message_id: int, date: datetime, text: OptionalParam[str] = MissingValue, caption: OptionalParam[str] = MissingValue,
                 forward_from: OptionalParam["User"] = MissingValue, forward_from_chat: OptionalParam["Chat"] = MissingValue,
                 forward_from_message_id: OptionalParam[str] = MissingValue, from_user: OptionalParam["User"] = MissingValue,
                 document: OptionalParam["Document"] = MissingValue, contact: OptionalParam["Contact"] = MissingValue, edit_date: OptionalParam[datetime] = MissingValue,
                 location: OptionalParam["Location"] = MissingValue, chat: OptionalParam["Chat"] = MissingValue, video: OptionalParam["Video"] = MissingValue,
                 photos: OptionalParam[List["PhotoSize"]] = MissingValue, sticker: OptionalParam["Sticker"] = MissingValue,
                 reply_to_message: OptionalParam["Message"] = MissingValue, invoice: OptionalParam["Invoice"] = MissingValue,
                 audio: OptionalParam["Audio"] = MissingValue, voice: OptionalParam["Voice"] = MissingValue,
                 successful_payment: OptionalParam["SuccessfulPayment"] = MissingValue, animation: OptionalParam["Animation"] = MissingValue,
                 new_chat_members: OptionalParam[List["User"]] = MissingValue, left_chat_member: OptionalParam["User"] = MissingValue) -> None:
        super().__init__()
        self._id = message_id
        self.message_id = message_id
        self.date = date

        self.text = text
        self.chat = chat
        self.reply_to_message = reply_to_message
        self.from_user = from_user
        self.forward_from = forward_from
        self.forward_from_message_id = forward_from_message_id
        self.forward_from_chat = forward_from_chat
        self.edit_date = edit_date
        self.caption = caption
        self.document = document
        self.video= video
        self.animation = animation
        self.audio = audio
        self.voice = voice
        self.photos = photos
        self.contact = contact
        self.location = location
        self.sticker = sticker
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.invoice = invoice
        self.successful_payment = successful_payment

        self._lock()

    @property
    def id(self) -> int:
        """An alias for :attr:`message_id`"""
        return self.message_id

    @property
    def author(self) -> OptionalParam["User"]:
        """An alias for :attr:`from_user`"""
        return self.from_user

    @property
    def attachment(self) -> OptionalParam[AttachmentType, List[PhotoSize], None]:
        """Union[:class:`bale.Video`, List[:class:`bale.PhotoSize`], :class:`bale.Document`, :class:`bale.Animation`], optional: Represents the message attachment. ``None`` if the message don't have any attachments"""
        attachment = self.video or self.photos or self.audio or self.animation or self.voice or self.document
        if not attachment:
            return None

        return attachment

    @property
    def content(self) -> OptionalParam[str]:
        """:obj:`str`, optional: Represents the message content. ``None`` if the message don't have text or caption"""
        return self.caption or self.text

    @property
    def chat_id(self) -> OptionalParam[str, int]:
        """:obj:`str` | :obj:`int`: Represents the Unique identifier of Conversation the message belongs to."""
        if not self.chat:
            return None
        
        return self.chat.id

    @property
    def reply_to_message_id(self) -> OptionalParam[int, None]:
        """:obj:`str`, optional: Represents the Unique identifier of Original message, if the message has been replied. ``None`` If the message is not replied"""
        if not self.reply_to_message:
            return None

        return self.reply_to_message.message_id

    @classmethod
    def from_dict(cls, data: Optional[Dict], bot) -> Optional["Message"]:
        data = BaleObject.parse_data(data)
        if not data:
            return None
        
        data["date"] = parse_time(data.get('date'))
        data["from_user"] = User.from_dict(data.pop('from', None), bot)
        data["chat"] = Chat.from_dict(data.get('chat'), bot)
        data["forward_from"] = User.from_dict(data.get('forward_from'), bot)
        data["forward_from_chat"] = Chat.from_dict(data.get('forward_from_chat'), bot)
        data["reply_to_message"] = Message.from_dict(data.get('reply_to_message'), bot)
        data["edit_date"] = parse_time(data.pop('edit_date', None))
        data["photos"] = [PhotoSize.from_dict(photo_payload, bot) for photo_payload in data.pop("photo", [])]
        data["document"] = Document.from_dict(data.get('document'), bot)
        data["audio"] = Audio.from_dict(data.get('audio'), bot)
        data["voice"] = Voice.from_dict(data.get('voice'), bot)
        data["location"] = Location.from_dict(data.get('location'), bot)
        data["contact"] = Contact.from_dict(data.get('contact'), bot)
        data["animation"] = Animation.from_dict(data.get('animation'), bot)
        data["successful_payment"] = SuccessfulPayment.from_dict(data.get('successful_payment'), bot)
        data["sticker"] = Sticker.from_dict(data.get('sticker'), bot)
        data["invoice"] = Invoice.from_dict(data.get('invoice'), bot)
        data["new_chat_members"] = [User.from_dict(new_chat_member_payload, bot) for new_chat_member_payload in data.get('new_chat_members', [])] or None
        data["left_chat_member"] = User.from_dict(data.get('left_chat_member'), bot)

        return super().from_dict(data, bot)

    async def reply(self, text: str, *, components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                    delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_message(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_message`.

        .. hint::
            .. code:: python

                await message.reply("Hi, python-bale-bot!", components = None)
        """
        return await self.get_bot().send_message(self.chat_id, text, components=components,
                                           reply_to_message_id=self.message_id, delete_after=delete_after)

    async def forward(self, chat_id: Union[str, int]):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_message(
                message_id=message.chat_id, from_chat_id=message.from_chat_id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.forward_message`.

        .. hint::
            .. code:: python

                await message.forward(1234)
        """
        return await self.get_bot().forward_message(chat_id, self.chat_id, self.message_id)

    async def reply_document(self, document: Union["Document", FileInput], *, caption: OptionalParam[str] = MissingValue,
                             components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                             delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_document(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_document`.

        .. hint::
            .. code:: python

                await message.reply_document(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_document(self.chat_id, document, caption=caption, components=components, reply_to_message_id=self.message_id,
                                                  delete_after=delete_after, file_name=file_name)

    async def reply_photo(self, photo: Union["PhotoSize", FileInput], *, caption: OptionalParam[str] = MissingValue,
                          components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                          delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_photo(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_photo`.

        .. hint::
            .. code:: python

                await message.reply_photo(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_photo(self.chat_id, photo, caption=caption,
                                         components=components, reply_to_message_id=self.message_id,
                                         delete_after=delete_after, file_name=file_name)

    async def reply_sticker(self, sticker: Union["Sticker", FileInput], *, delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_sticker(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_sticker`.

        .. hint::
            .. code:: python

                await message.reply_sticker("File ID", *args, **kwargs)
        """
        return await self.get_bot().send_sticker(self.chat_id, sticker, reply_to_message_id=self.message_id,
                                         delete_after=delete_after)

    async def reply_video(self, video: Union["Video", InputFile], *, caption: OptionalParam[str] = MissingValue,
                          components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                          delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_video(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_video`.

        .. hint::
            .. code:: python

                await message.reply_video(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_video(self.chat_id, video, caption=caption,
                                         components=components, reply_to_message_id=self.message_id,
                                         delete_after=delete_after, file_name=file_name)

    async def reply_animation(self, animation: Union["Animation", FileInput], *, duration: OptionalParam[int] = MissingValue,
                              width: OptionalParam[int] = MissingValue, height: OptionalParam[int] = MissingValue, caption: OptionalParam[str] = MissingValue,
                              components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                              delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_animation(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_animation`.

        .. hint::
            .. code:: python

                await message.reply_animation(bale.InputFile("FILE_ID"), caption = "this is a caption", *args, **kwargs)
        """
        return await self.get_bot().send_animation(self.chat_id, animation, duration=duration, width=width, height=height, caption=caption,
                                                   components=components, reply_to_message_id=self.message_id, delete_after=delete_after, file_name=file_name)

    async def reply_audio(self, audio: Union["Audio", InputFile], *, caption: OptionalParam[str] = MissingValue,
                          components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                          delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_audio(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_audio`.

        .. hint::
            .. code:: python

                await message.reply_audio(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_audio(self.chat_id, audio, caption=caption,
                                         components=components, reply_to_message_id=self.message_id,
                                         delete_after=delete_after, file_name=file_name)

    async def reply_location(self, location: "Location", *, components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                             delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_location(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_audio`.

        .. hint::
            .. code:: python

                await message.reply_location(bale.Location(35.71470468031143, 51.8568519168293))
        """
        return await self.get_bot().send_location(self.chat_id, location,
                                               components=components,
                                               reply_to_message_id=self.message_id,
                                               delete_after=delete_after)

    async def reply_contact(self, contact: "Contact", *, components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                            delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_contact(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_contact`.

        .. hint::
            .. code:: python

                await message.reply_contact(bale.Contact('09****', 'first name', 'last name'))
        """
        return await self.get_bot().send_contact(self.chat_id, contact, components=components, reply_to_message_id=self.message_id, delete_after=delete_after)

    async def reply_media_group(self, media: List[MediaInput], *,
                    components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_media_group(
                chat_id=message.chat_id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_media_group`.

        .. hint::
            .. code:: python

                await message.reply_media_group([
                    InputMediaPhoto("File ID", caption="example caption"),
                    InputMediaPhoto("File ID"),
                    InputMediaPhoto("File ID")
                ], ...)
        """
        return await self.get_bot().send_media_group(self.id, media, components=components)

    async def copy(self, chat_id: Union[int, str], reply_to_message_id: OptionalParam[str, int] = MissingValue,
                   delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.copy_message(
                from_chat_id=message.chat_id, message_id=message.id, reply_to_message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.copy_message`.

        .. hint:;
            .. code:: python

                await message.copy(
                    1234, *args, **kwargs
                )
        """
        return await self.get_bot().copy_message(chat_id, self.chat_id, self.id, reply_to_message_id=reply_to_message_id, delete_after=delete_after)

    async def edit(self, text: str, *, components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue) -> Message:
        """
        Shortcut method for:

        .. code:: python

            await bot.edit_message(
                chat_id=message.chat_id, message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.edit_message`.

        .. hint::
            .. code:: python

                await message.edit("Bye!", components = None)
        """
        return await self.get_bot().edit_message(self.chat_id, self.message_id, text, components=components)

    async def edit_caption(self, caption: str, *, components: OptionalParam["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue) -> Message:
        """
        Shortcut method for:

        .. code:: python

            await bot.edit_message_caption(
                chat_id=message.chat_id, message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.edit_message_caption`.

        .. hint::
            .. code:: python

                await message.edit_caption("Edited!", components = None)
        """
        return await self.get_bot().edit_message_caption(self.chat_id, self.message_id, caption, components=components)

    async def delete(self, *, delay: Optional[Union[int, float]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.delete_message(
                chat_id=message.chat_id, message_id=message.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.delete_message`.

        .. hint::
            .. code:: python

                await message.delete(delay=5)
        """
        return await self.get_bot().delete_message(self.chat_id, self.message_id, delay=delay)
