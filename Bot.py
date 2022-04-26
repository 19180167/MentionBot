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
async def start(event):
  await event.reply(
    "**ʜᴇʟʟᴏ sᴡᴇᴇᴛ ʜᴇᴀʀᴛ ɪ ᴀᴍ ᴀsᴀᴅ mh ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ** 👻\n**ᴄʟɪᴄᴋ ᴏɴ** /help **ғᴏʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏsᴇʟғ**\n\n**ɢɪᴠᴇ ᴍᴇ ʜᴇᴀʀᴛ** [ʟᴏᴠᴇ](https://t.me/mr_theherd) **ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ**",
    link_preview=False,
    buttons=(
      [
        Button.url('⚙️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⚙️', 'https://t.me/MHMentionBot?startgroup=true'),
        Button.url('👥 ɢʀᴏᴜᴘ 👥︎', 'https://t.me/wsbmusikgc'),
        ],
        [
        Button.url('📣 ᴄʜᴀɴɴᴇʟ 📣️', 'https://t.me/MH_Projects'),
        ]
    )
  )
                    
                    
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴀsᴀᴅ ᴀʟᴇxᴀ**\n\n**ᴄᴏᴍᴍᴀɴᴅ**: /mentionall\n**ᴄᴏᴍᴍᴀɴᴅ**: /cancel **ᴛᴏ ᴄᴀɴᴄᴇʟ ɢᴏɪɴɢ ᴏɴ ᴘʀᴏᴄᴇss**\n**__Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.__**\n`Example: /mentionall Good Morning!`\n**Yᴏᴜ ᴄᴀɴ ʏᴏᴜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ. Bᴏᴛ ᴡɪʟʟ ᴛᴀɢ ᴜsᴇʀs ᴛᴏ ᴛʜᴀᴛ ʀᴇᴘʟɪᴇᴅ ᴍᴇsssᴀɢᴇ__**."
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('❤️ ʜᴇᴀʀᴛ ❤️', 'https://t.me/mr_theherd'),
        Button.url('📽️ ʏᴏᴜᴛᴜʙᴇ 📽️', 'https://youtube.com/channel/UCs5naByLDF-XNWjOOLENTRg')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
  helptext = "**ᴏᴡɴᴇʀ ᴍᴇɴᴜ ᴏғ mh mention**\n\n**ᴍʏ ᴏᴡɴᴇʀ ɪs [MBUL](https://t.me/mr_theherd)**\n**__ᴏғғɪᴄɪᴀʟ ᴍᴇᴍʙᴇʀ ᴏғ MH__**\n**ʏᴏᴜᴛᴜʙᴇ** [ᴄʜᴀɴɴᴇʟ](https://youtube.com/channel/UCs5naByLDF-XNWjOOLENTRg)\n**ғᴜᴛᴜʀᴇ ᴀɴᴇsᴛʜᴇᴛɪᴄ**."
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('❤️ ʜᴇᴀʀᴛ ❤️', 'https://t.me/mr_theherd'),
        Button.url('📽️ ʏᴏᴜᴛᴜʙᴇ 📽️', 'https://youtube.com/channel/UCs5naByLDF-XNWjOOLENTRg')
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
