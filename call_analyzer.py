from pydantic import BaseModel
from mistralai import Mistral
from instructor import from_mistral, Mode


# Класс для структурированного вывода
class CallAnalysis(BaseModel):
    tone: str  # "положительный", "нейтральный", "негативный"
    recommendations: list[str]  # 1-2 рекомендации


class CallAnalyzer:
    def __init__(self, api_key: str):
        self.client = Mistral(api_key=api_key)
        self.instructor_client = from_mistral(client=self.client, mode=Mode.MISTRAL_TOOLS)

    def analyze(self, call_text: str) -> CallAnalysis:
        """Анализирует текст звонка и возвращает оценку тона и рекомендации"""
        prompt = f"""
        Ты - эксперт по анализу телефонных переговоров. Проанализируй следующий разговор:

        {call_text}

        Сначала определи общий тон разговора (строго один из вариантов: положительный, нейтральный, негативный).
        Затем дай 1-2 конкретные рекомендации, как можно улучшить коммуникацию.
        """

        analysis = self.instructor_client.chat.completions.create(
            response_model=CallAnalysis,
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        return analysis