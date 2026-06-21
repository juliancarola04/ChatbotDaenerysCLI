from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME")

client = genai.Client()

chat = client.chats.create(
    model= MODEL_NAME,
    config= types.GenerateContentConfig(
        system_instruction = "Sos Daenerys Targaryen de la serie Juego de Tronos. Contesta en español.",
        temperature = 0.8)
)
print("||||||||||||||||||")
print("||Chat de Gemini||")
print("||||||||||||||||||")

while True:
    print()
    try:
        entrada_user = input("Vos: ").strip()

        if (entrada_user.lower() == "salir"):
            print("---------------------")
            print("Saliendo del chatbot")
            print("Tokens consumidos: " + str(response.usage_metadata.total_token_count))
            print("---------------------")
            break

        response = chat.send_message(entrada_user)

        print("Gemini: " + response.text)

    except Exception:
        print("Ocurrió un error")