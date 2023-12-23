import aiogram
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, executor, types
import re

bot = Bot(token='6547129006:AAE83sI_akx1rBDyc6SnyCmucjPV2ht64Ak')
dp = Dispatcher(bot)

@dp.message_handler(commands=['dns'])
async def dns_command_handler(message: types.Message):
    mention = message.from_user.mention
    
    if not mention:
        mention = message.from_user.first_name

    await message.reply(f"""› PS4 & PS5 DNS 🌐

• OLD DNS ❌ Offline 
Primary: 165.227.83.145
Secondary: 192.241.221.79

• NEW DNS ✅ Online
Primary: 62.210.38.117
Secondary: NONE

Req by: {mention}""")

@dp.message_handler(lambda message: re.search(r'\bdns\b', message.text, re.IGNORECASE))
async def dns_text_handler(message: types.Message):
    await dns_command_handler(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)