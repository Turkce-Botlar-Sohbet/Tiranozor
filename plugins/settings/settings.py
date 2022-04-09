import asyncio
from pyrogram import types, errors
from config import LOGGER
from database.database import db


async def Settings(m: "types.Message"):
    usr_id = m.chat.id
    is_command = m.entities[0]['type']

    if is_command == "bot_command":
        message = m.reply_text
    else:
        message = m.edit

    user_data = await db.get_user_data(usr_id)

    if not user_data:
        await message("Verileriniz veritabanından alınamadı!")
        return

    upload_as_doc = user_data.get("upload_as_doc", False)
    thumbnail = user_data.get("thumbnail", None)
    # generate_sample_video = user_data.get("generate_sample_video", False)
    generate_ss = user_data.get("generate_ss", False)
    get_notif = user_data.get("notif", False)
    get_caption = user_data.get("caption", False)

    buttons_markup = [
        [types.InlineKeyboardButton(f"{'🔔' if get_notif else '🔕'} Bildirimler",
                                    callback_data="notifon")],
        [types.InlineKeyboardButton(f"{'🎥 Video' if upload_as_doc else '🗃️ Dosya'} Olarak Yükle",
                                    callback_data="triggerUploadMode")],
        # [types.InlineKeyboardButton(f"🎞 Kısa Video Oluştur {'✅' if generate_sample_video else '❎'}",
        # callback_data="triggerGenSample")],
        [types.InlineKeyboardButton(f"📜 Açıklama {'✅' if get_caption else '❎'}",
                                    callback_data="setCaption")],
        [types.InlineKeyboardButton(f"📸 Ekran Görüntüsü Al {'✅' if generate_ss else '❎'}",
                                    callback_data="triggerGenSS")],
        [types.InlineKeyboardButton(f"🌃 Thumbnail {'Değiştir' if thumbnail else 'Ayarla'}",
                                    callback_data="setThumbnail")]
    ]
    if thumbnail:
        buttons_markup.append([types.InlineKeyboardButton("🌆 Thumbnail Göster",
                                                          callback_data="showThumbnail")])

    buttons_markup.append([types.InlineKeyboardButton(f"🔙 Geri",
                                                      callback_data="home"),
                           ])

    try:
        await message(
            text="**⚙ Bot Ayarları**",
            reply_markup=types.InlineKeyboardMarkup(buttons_markup),
            disable_web_page_preview=True,
            parse_mode="Markdown"
        )
    except errors.MessageNotModified:
        pass
    except errors.FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as err:
        LOGGER.error(err)
