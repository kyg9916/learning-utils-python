import re


input_text = """

[2. 🐶💸 악동 도지쉑 - 다 잃었소 (song by 나 일론 머스크)](https://www.notion.so/2-song******643d81a3bf7ddc57dcd93d20?pvs=21)

[3. 😠 X발 내가 잡는다](https://www.notion.so/3-X-23816bf4643d819b92dadd1b5bc******)

"""

titles = re.findall(r"\[\d+\. (.+?)\]\(", input_text)

for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")
