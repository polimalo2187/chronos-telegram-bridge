import asyncio
import httpx
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.config import settings

dp = Dispatcher()

def extract_code(text: str):
    if not text:
        return None
    parts = text.split(maxsplit=1)
    if len(parts) < 2:
        return None
    payload = parts[1]
    if payload.startswith("link_"):
        return payload.replace("link_", "", 1)
    return None

@dp.message(CommandStart())
async def start(message: Message):
    code = extract_code(message.text)

    if not code:
        await message.answer("Abre el enlace desde la web para vincular tu cuenta.")
        return

    telegram_id = message.from_user.id
    telegram_username = message.from_user.username

    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{settings.API_BASE_URL}/telegram/link",
            headers={"X-TG-SECRET": settings.TELEGRAM_LINK_SECRET},
            json={
                "code": code,
                "telegram_id": telegram_id,
                "telegram_username": telegram_username,
            },
        )

    if r.status_code == 200:
        await message.answer("✅ Cuenta vinculada correctamente.")
    else:
        await message.answer("❌ No pude vincular la cuenta. Genera un nuevo enlace en la web.")

async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
