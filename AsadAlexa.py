import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cb76d7f5dae14ec1e11c7.jpg",
        caption=f"""**ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇɴᴛɪᴏɴ ʙᴏᴛ ᴛʜᴀᴛ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴜᴘᴛᴏ 10ᴋ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴍʙᴇʀs ᴇᴀsʟʏ ...
💞 ᴛʜᴀɴᴋꜱ ꜰᴏʀ  
ᴜꜱɪɴɢ ᴀɴᴅ ʏᴏᴜʀ ʟᴏᴠᴇ ❤️[ᴀsᴀᴅ ᴀʟᴇxᴀ](t.me/Alexa_MentionBot).\nᴍʏ [ᴅᴇᴠᴇʟᴏᴘᴇʀ](t.me/Dr_Asad_Ali) ᴍʏ [sᴜᴘᴘᴏʀᴛᴇʀ](t.me/HarshitSharma361)\n
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⚙️",
                        url=f"https://t.me/Alexa_MentionBot?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 ɢʀᴏᴜᴘ 👥︎", url=f"https://t.me/Shayri_Music_Lovers"
                    ),
                    InlineKeyboardButton(
                        "📣 ᴄʜᴀɴɴᴇʟ 📣", url=f"https://t.me/AsadSupport"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👸 ǫᴜᴇᴇɴ 👸︎", url=f"https://t.me/Sonali_rajputt_Queen_Of_ROCKS"
                    ),
                    InlineKeyboardButton(
                        "❤️ ʙʀᴏ ❤️", url=f"https://t.me/HarshitSharma361"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👑 ᴋɪɴɢ 👑", url="https://t.me/Dr_Asad_Ali"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴀsᴀᴅ ᴀʟᴇxᴀ**\n\n**ᴄᴏᴍᴍᴀɴᴅ**: /mentionall\n**__Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.__**\n`Example: /mentionall Good Morning!`\n**__You can you this command as a reply to any message. Bot will tag users to that replied messsage__**."
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('❤️ ʜᴇᴀʀᴛ ❤️', 'https://t.me/Give_Me_Heart'),
        Button.url('📽️ ʏᴏᴜᴛᴜʙᴇ 📽️', 'https://www.youtube.com/c/JankariKiDuniya')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
  helptext = "**ᴏᴡɴᴇʀ ᴍᴇɴᴜ ᴏғ ᴀsᴀᴅ ᴀʟᴇxᴀ**\n\n**ᴍʏ ᴏᴡɴᴇʀ ɪs [ᴀsᴀᴅ ᴀʟɪ](https://t.me/Dr_Asad_Ali)**\n**__ᴏғғɪᴄɪᴀʟ ᴍᴇᴍʙᴇʀ ᴏғ ʀᴏᴄᴋs__**\n**ʏᴏᴜᴛᴜʙᴇ [ᴄʜᴀɴɴᴇʟ](https://www.youtube.com/c/JankariKiDuniya)**\n**ғᴜᴛᴜʀᴇ ᴀɴᴇsᴛʜᴇᴛɪᴄ**."
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('❤️ ʜᴇᴀʀᴛ ❤️', 'https://t.me/Give_Me_Heart'),
        Button.url('📽️ ʏᴏᴜᴛᴜʙᴇ 📽️', 'https://www.youtube.com/c/JankariKiDuniya')
      ]
    )
  )

  
@client.on(events.NewMessage(pattern="^/mentionall ?(.*)"))
async def mentionall(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("__This command can be use in groups and channels!__")
  
  is_admin = False
  try:
    partici_ = await client(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("__Only admins can mention all!__")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("__Give me one argument!__")
  elif event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("__I can't mention members for older messages! (messages which are sent before I'm added to group)__")
  else:
    return await event.respond("__Reply to a message or give me some text to mention others!__")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
      if mode == "text_on_cmd":
        txt = f"{usrtxt}\n\n{msg}"
        await client.send_message(chat_id, txt)
      elif mode == "text_on_reply":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__There is no proccess on going...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('__Stopped.__')

print(">> ASAD ALEXA WORKING <<")
client.run_until_disconnected()
