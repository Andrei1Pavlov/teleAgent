import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from call_analyzer import CallAnalyzer

TOKEN = '7589904927:AAFqiqu8eqhGMD9w5rJj55-r2n39inafAqY'
MISTRAL_API_KEY = "1uIQjVsBbqhY4FogxSBklVXIeAnnnzpG"

bot = Bot(TOKEN)
dp = Dispatcher()
analyzer = CallAnalyzer(MISTRAL_API_KEY)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Пришлите мне текст телефонного разговора, и я проанализирую его тон и дам рекомендации.")

@dp.message()
async def analyze_call(message: types.Message):
    try:
        analysis = analyzer.analyze(message.text)
        response = (
            f"📊 Тон разговора: {analysis.tone}\n\n"
            "🔍 Рекомендации:\n" +
            "\n".join(f"• {rec}" for rec in analysis.recommendations)
        )
        await message.answer(response)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())