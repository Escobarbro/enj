from pyrogram import Client, idle
from pyromod import listen

bot = Client(
    "mo",
    api_id=20977804,
    api_hash="7f34ed845703f6d40e856c367fb5dd7c",  # قم بإضافة القيمة الصحيحة لمتغير api_hash
    bot_token="5844249243:AAEY-mCqg4_TQj5sR9XzdDf8XRWUwpR92H4",  # قم بإضافة توكن المصنع
    plugins=dict(root="MHelal")
)

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "MohamedHelal_l"  # يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_helalbot())
