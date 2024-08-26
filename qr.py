import asyncio
import qrcode
import os
from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart
bot = Bot(token="6896983459:AAFJO077XXLxKu8UTdTGR5tPBSxAvnoABPc")

dp = Dispatcher()

@dp.message(CommandStart())
async def get_message(message: types.Message):
    await message.answer("Assalomu alaykum botimizga xush kelibsiz! Xohlagan matningizni tashlang men sizga uni QR Code'ga aylantirib beraman")
    
@dp.message()
async def qr_send(message: types.Message):
    img = qrcode.make(message.text)
    img.save(f"{message.chat.id}.png")
    
    file = types.input_file.FSInputFile(path=f"{message.chat.id}.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=file)
    
    try:
        os.remove(f"{message.chat.id}.png")
    except:
        pass
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())