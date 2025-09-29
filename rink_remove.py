import re

# 입력 텍스트 (예시로 일부만 복사)
input_text = """
[1. 모바일 광고 제거하는 방법](https://www.notion.so/1-23716bf4643d805c8111d0******)
[2. 유튜브 광고 제거하는 방법](https://www.notion.so/2-23716bf4643d8027b223e97d58f6b******)
[3. 마우스 스크롤 속도 조정하는 방법](https://www.notion.so/3-23816bf4643d80529c41d25a******)
"""

# 정규표현식으로 링크 제거
output_text = re.sub(r'\[(.*?)\]\(https?://[^\)]+\)', r'\1', input_text)

print(output_text.strip())
