# Агент оценки телефонных звонков

Минимальное приложение для анализа тона телефонных разговоров и генерации рекомендаций по улучшению коммуникации.

## Функционал

- Анализирует текст телефонного разговора
- Определяет общий тон (позитивный/нейтральный/негативный)
- Формирует 1-2 конкретные рекомендации по улучшению
- Поддерживает два интерфейса: консольный и Telegram-бота

## Технологии

- Mistral AI (API) - языковая модель для анализа
- Pydantic - валидация и структурирование данных
- Instructor - структурированный вывод LLM
- aiogram - Telegram-бот (опционально)

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Andrei1Pavlov/teleAgent.git
cd teleAgent