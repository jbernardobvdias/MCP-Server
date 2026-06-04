import openai

from settings import settings

client = openai.OpenAI(api_key=settings.openai_key)

def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding