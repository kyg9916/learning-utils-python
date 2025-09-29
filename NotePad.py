from datetime import datetime, timedelta
from ics import Calendar, Event

# 일정 정보
schedule = [
    ("SQL 초급~중급 학습", "2025-10-07", "2025-10-12"),
    ("jQuery 1강. jQuery는 무엇인가? 설치부터 시작하기", "2025-10-14"),
    ("jQuery 2강. jQuery의 문법 구조 파헤치기", "2025-10-14"),
    ("jQuery 3강. jQuery 셀렉터 완전 정복", "2025-10-15"),
    ("jQuery 4강. HTML 내용 바꾸기 – jQuery로 DOM 다루기", "2025-10-15"),
    ("jQuery 5강. 스타일도 바꾼다! 클래스 조작하기", "2025-10-16"),
    ("jQuery 6강. 사용자와 소통하자! jQuery 이벤트 기초", "2025-10-16"),
    ("jQuery 7강. 시선을 사로잡는 jQuery 애니메이션", "2025-10-17"),
    ("jQuery 8강. 더 짧고 간결하게! jQuery 체이닝과 this", "2025-10-17"),
    ("jQuery 9강. 새로운 요소를 추가하고 지우기", "2025-10-18"),
    ("jQuery 10강. 입력값 받아오기 – 폼 요소 제어하기", "2025-10-18"),
    ("jQuery 11강. HTML 속성 변경으로 인터랙션 만들기", "2025-10-19"),
    ("jQuery 12강. 배열처럼 다루자! jQuery 반복 처리", "2025-10-19"),
    ("jQuery 13강. 서버와 통신하기 – jQuery Ajax 입문", "2025-10-20"),
    ("jQuery 14강. 서버에서 받은 데이터로 동적 페이지 만들기", "2025-10-20"),
    ("jQuery 15강. To-Do List 만들며 마무리하기!", "2025-10-20"),
    ("미니 프로젝트 (SQL + jQuery + JS + API 통합)", "2025-10-23", "2025-10-30"),
]

# 캘린더 생성
calendar = Calendar()

# 일정 추가
for item in schedule:
    if len(item) == 3:
        title, start_str, end_str = item
        start = datetime.strptime(start_str, "%Y-%m-%d")
        end = datetime.strptime(end_str, "%Y-%m-%d") + timedelta(days=1)
    else:
        title, date_str = item
        start = datetime.strptime(date_str, "%Y-%m-%d")
        end = start + timedelta(hours=1)

    event = Event()
    event.name = title
    event.begin = start
    event.end = end
    calendar.events.add(event)

# 파일 저장
with open("학습일정_2025_10.ics", "w", encoding="utf-8") as f:
    f.writelines(calendar.serialize_iter())

print("ICS 파일이 성공적으로 생성되었습니다!")
