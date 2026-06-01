import tkinter as tk
import os

# ✅ 현재 파일 위치 기준 경로 설정 (핵심🔥)
base_path = os.path.dirname(os.path.abspath(__file__))

def get_image_path(filename):
    return os.path.join(base_path, filename)

window = tk.Tk()
window.title("대한독립만세")
window.geometry("700x700")

label1 = tk.Label(
    window,
    text="독립운동가 업적 검색 프로그램",
    font=("맑은 고딕", 16, "bold")
)
label1.pack(pady=10)

# ✅ 로고 이미지 (경로 고정)
try:
    logo = tk.PhotoImage(file=get_image_path("tae.png"))
    image_label = tk.Label(window, image=logo)
    image_label.pack()
except:
    pass

label2 = tk.Label(
    window,
    text="업적을 알고 싶은 독립운동가의 이름을 입력해주세요."
)
label2.pack()

textbox = tk.Text(window, height=1, width=30)
textbox.pack(pady=10)

fighters = {
    "유관순": {
        "title": "유관순",
        "achievement": "- 3·1 운동 참여\n- 아우내 장터 만세 운동 주도",
        "cf": "3·1운동 - 1919년 3월 1일 정오를 기하여 일제의 압박에 항거, 전세계에 민족의 자주독립을 선언하고 온 민족이 총궐기하여 평화적 시위를 전개한 항일운동",
        "image": "yks.png"
    },
    "홍범도": {
        "title": "홍범도",
        "achievement": "- 대한독립군 총사령관\n- 봉오동전투, 청산리대첩을 대승으로 이끔",
        "cf": "봉오동 전투 - 1920년 만주 봉오동에서 독립군 부대가 일본 정규군을 대패시킨 전투\n청산리 대첩 - 1920년 10월에 김좌진의 북로 군정서와 홍범도의 대한 독립군이 청산리 일대에서 일본군과 싸워 대승한 전투",
        "image": "hbd.png"
    },
    "이육사": {
        "title": "이육사",
        "achievement": "- 「청포도」, 「절정」, 「광야」 저술",
        "cf": "대표 시 '절정'으로 민족정신을 표현",
        "image": "264.png"
    },
    "신채호": {
        "title": "신채호",
        "achievement": "- 항일 언론운동 및 역사 연구",
        "cf": "민족주의 사학자",
        "image": "sch.png"
    },
    "조만식": {
        "title": "조만식",
        "achievement": "- 물산장려운동 전개",
        "cf": "민족 경제 자립 운동가",
        "image": "jms.png"
    }
}

def click():
    name = textbox.get("1.0", tk.END).strip()

    if name in fighters:
        info = fighters[name]

        new_window = tk.Toplevel(window)
        new_window.title(info["title"])
        new_window.geometry("600x700")

        title_label = tk.Label(
            new_window,
            text=info["title"],
            font=("맑은 고딕", 20, "bold")
        )
        title_label.pack(pady=20)

        # ✅ 이미지 (절대 경로 사용)
        try:
            img_path = get_image_path(info["image"])
            photo = tk.PhotoImage(file=img_path)
            image_label = tk.Label(new_window, image=photo)
            image_label.image = photo
            image_label.pack(pady=10)
        except:
            pass

        achievement_label = tk.Label(
            new_window,
            text=info["achievement"],
            font=("맑은 고딕", 14),
            justify="left"
        )
        achievement_label.pack(pady=20)

        cf_label = tk.Label(
            new_window,
            text=info["cf"],
            font=("맑은 고딕", 10),
            wraplength=500
        )
        cf_label.pack(pady=20)

    else:
        error_window = tk.Toplevel(window)
        error_window.title("검색 결과")
        error_window.geometry("300x100")

        error_label = tk.Label(
            error_window,
            text="해당 정보를 찾을 수 없습니다.",
            font=("맑은 고딕", 12)
        )
        error_label.pack(pady=20)

button = tk.Button(
    window,
    text="확인",
    command=click
)
button.pack()

window.mainloop()
