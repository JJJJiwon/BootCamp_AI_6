from openai import OpenAI
import os
import dotenv

# env 설정
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
# print(os.environ["OPENAI_API_KEY"])
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


# Whisper
renamed_file = "C:/Users/scvts/Desktop/jiwon/prompt/audio/하슬라한의원.mp3"

audio_file = open(renamed_file, "rb")
transcript = client.audio.transcriptions.create(
    file = audio_file,
    model="whisper-1",
    language="ko",
    response_format="text",
    temperature=0.0,
)

print(transcript)



