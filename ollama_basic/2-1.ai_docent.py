# 실습 : image to text
from ollama import chat

IMAGE_PATH = "imgs/img01.jpg"
MODEL_NAME = "gemma4:e2b"

# MODEL_NAME = "qwen3.5:9b"


response = chat(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": """
이 이미지를 한국어로 설명해줘.

다음 형식으로 답변해줘.
1. 전체 장면
2. 주요 객체
3. 배경
4. 이미지에서 추론 가능한 상황
""",
            "images": [IMAGE_PATH],
        }
    ],
    think=False, # 추론기능 꺼놓기 
    stream=False, # 답변을 스트리밍하지 않고 한 번에 받기
)

print(response.message.content)

