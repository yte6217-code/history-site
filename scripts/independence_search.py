import tkinter as tk
import os

window = tk.Tk()
window.title("대한독립만세")
window.geometry("700x700")

base = os.path.dirname(os.path.abspath(__file__))

def safe_image(path):
    try:
        return tk.PhotoImage(file=path)
    except Exception as e:
        print("이미지 오류:", e)
        return None

tk.Label(window, text="독립운동가 업적 검색 프로그램",
         font=("맑은 고딕", 16, "bold")).pack(pady=10)

# 로고
logo_path = os.path.join(base, "tae.png")
logo = safe_image(logo_path)

if logo:
    lbl = tk.Label(window, image=logo)
    lbl.image = logo
    lbl.pack()
else:
    tk.Label(window, text="(로고 없음)").pack()

textbox = tk.Entry(window)
textbox.pack(pady=10)

fighters = {
    "유관순": ("yks.png", "3·1 운동 참여"),
    "홍범도": ("hbd.png", "봉오동 전투"),
    "이육사": ("264.png", "대표 시 절정"),
    "신채호": ("sch.png", "역사학자"),
    "조만식": ("jms.png", "물산장려운동")
}

def click():
    name = textbox.get().strip()

    if name in fighters:
        img_file, desc = fighters[name]

        w = tk.Toplevel(window)
        w.title(name)

        tk.Label(w, text=name, font=("맑은 고딕", 16, "bold")).pack()

        path = os.path.join(base, img_file)
        img = safe_image(path)

        if img:
            l = tk.Label(w, image=img)
            l.image = img
            l.pack()
        else:
            tk.Label(w, text="이미지 없음").pack()

        tk.Label(w, text=desc).pack()

    else:
        tk.Label(window, text="없음").pack()

tk.Button(window, text="확인", command=click).pack()

window.mainloop()
