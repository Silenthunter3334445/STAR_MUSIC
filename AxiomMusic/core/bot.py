# -----------------------------------------------
# 🔸 AxiomMusic Project
# 🔹 Developed & Maintained by: Axiom Bots
# 📅 Copyright © 2026 – All Rights Reserved
# -----------------------------------------------

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Axiomm(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Axiom's MusicBot...")

        super().__init__(
            name="AxiomMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<blockquote>"
                    f"<b><u>» ᴛʜє ᴧxɪσϻ ϻυsɪᴄ ʙσᴛ sᴛᴧʀᴛєᴅ :</u></b>"
                    f"</blockquote>"
                    f"<u>\n\n"
                    f"<blockquote expandable>"
                    f"<b>"
                    f"✧ ηᴧϻє : {self.mention}\n"
                    f"✧ υsєʀηᴧϻє : @{self.username}\n"
                    f"✧ ɪᴅ : <code>{self.id}</code>"
                    f"</b>"
                    f"</blockquote>"
                ),
            )

        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. "
                "Make sure that you have added your bot to your log group/channel."
            )
            return

        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n"
                f"Reason : {type(ex).__name__}: {ex}"
            )
            return

        try:
            a = await self.get_chat_member(config.LOGGER_ID, self.id)

            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "Please promote your bot as an admin in your log group/channel."
                )
                return

        except Exception as ex:
            LOGGER(__name__).error(
                f"Failed to check logger admin status.\n"
                f"Reason : {type(ex).__name__}: {ex}"
            )
            return

        LOGGER(__name__).info(
            f"Axiom's Music Bot Started as {self.name}"
        )

    async def stop(self):
        await super().stop()
