import tkinter as tk
import os

# 현재 파일 위치 기준
base = os.path.dirname(__file__)

def img(name):
    return os.path.join(base, name)

window = tk.Tk()
window.title("대한독립만세")
window.geometry("700x700")

# 제목
tk.Label(window, text="독립운동가 업적 검색 프로그램",
         font=("맑은 고딕", 16, "bold")).pack(pady=10)

# 로고 이미지
try:
    logo = tk.PhotoImage(file=img("tae.png"))
    lbl_logo = tk.Label(window, image=logo)
    lbl_logo.image = logo
    lbl_logo.pack()
except:
    pass

# 안내문
tk.Label(window, text="이름을 입력하세요").pack()

# 입력창
textbox = tk.Text(window, height=1, width=30)
textbox.pack(pady=10)

# 데이터
fighters = {
    "유관순": ("yks.png", "- 3·1 운동 참여"),
    "홍범도": ("hbd.png", "- 봉오동 전투 승리"),
    "이육사": ("264.png", "- 대표 시 '절정'"),
    "신채호": ("sch.png", "- 역사학자"),
    "조만식": ("jms.png", "- 물산장려운동")
}

# 버튼 클릭 함수
def click():
    name = textbox.get("1.0", tk.END).strip()

    if name in fighters:
        img_file, desc = fighters[name]

        w = tk.Toplevel(window)
        w.title(name)

        tk.Label(w, text=name, font=("맑은 고딕", 18, "bold")).pack(pady=10)

        try:
            p = tk.PhotoImage(file=img(img_file))
            l = tk.Label(w, image=p)
            l.image = p
            l.pack()
        except:
            tk.Label(w, text="(이미지 없음)").pack()

        tk.Label(w, text=desc).pack(pady=10)

    else:
        tk.Label(window, text="해당 인물이 없습니다").pack()

# 버튼
tk.Button(window, text="확인", command=click).pack()

window.mainloop()
