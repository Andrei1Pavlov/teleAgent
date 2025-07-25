from call_analyzer import CallAnalyzer


def main():
    # Инициализация анализатора
    analyzer = CallAnalyzer(api_key="1uIQjVsBbqhY4FogxSBklVXIeAnnnzpG")

    # Ввод текста звонка
    call_text = input("Введите текст телефонного разговора:\n")

    # Анализ
    result = analyzer.analyze(call_text)

    # Вывод результатов
    print("\nРезультат анализа:")
    print(f"Тон разговора: {result.tone}")
    print("Рекомендации:")
    for i, rec in enumerate(result.recommendations, 1):
        print(f"{i}. {rec}")


if __name__ == "__main__":
    main()
