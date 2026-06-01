import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("역사 퀴즈 서바이벌")
window.geometry("800x800")

# 문제와 정답
quiz = [
    ["조선을 건국한 인물은?", "이성계"],
    ["세종대왕의 본명은?", "이도"],
    ["임진왜란이 일어난 연도는?", "1592"],
    ["후백제를 세운 인물은?", "견훤"]
]

current = 0
score = 0

# 제목
label1 = tk.Label(window, text="==역사 퀴즈 서바이벌==")
label1.pack(pady=10)

# 문제 표시
question_label = tk.Label(window, text=quiz[current][0])
question_label.pack(pady=10)

# 답 입력창
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

def check_answer():
    global current, score

    answer = entry.get()

    if answer == quiz[current][1]:
        score += 1
        messagebox.showinfo("결과", "정답!")
    else:
        messagebox.showinfo(
            "결과",
            f"오답!\n정답은 {quiz[current][1]} 입니다."
        )

    current += 1

    if current < len(quiz):
        question_label.config(text=quiz[current][0])
        entry.delete(0, tk.END)
    else:
        question_label.config(
            text=f"게임 종료!\n점수 : {score}/{len(quiz)}"
        )
        entry.pack_forget()
        submit_button.pack_forget()

# 제출 버튼
submit_button = tk.Button(window, text="정답 제출", command=check_answer)
submit_button.pack(pady=10)

window.mainloop()
