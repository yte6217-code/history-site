import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("📜 흥미진진 역사 밸런스 게임")
window.geometry("600x450")
window.resizable(False, False)

questions = [
    {
                "id": 1,
                "question": "당신은 임진왜란 당시 선조 임금입니다.\n나라의 운명이 걸린 상황, 당신의 선택은?",
                "choice_A": "목숨을 걸고 바다을 지키겠다\n[이순신 장군 전폭 지원]",
                "choice_B": "수도를 버리고 피난을 가겠다\n[명나라에 군사 요청 및 망명 시도]",
                "fact_A": "[역사 사실]\n이순신 장군은 단 13척의 배로 133척의 왜선을 격파하는 '명량대첩'의 기적을 이뤄냈습니다.",
                "fact_B": "[역사 사실]\n선조는 의주로 피난을갔고, 명나라에 지속적으로 군사 요청을 했습니다."
            },
            {
                "id": 2,
                "question": "19세기 말, 서양 선진국들이 통상을 요구하며\n조선의 물을 두드립니다. 당신의 선택은?",
                "choice_A": "서양의 제안을 단호히 거부하고 \n나라의 문을 꽉 잠궈 \n통상 수교를 거부한다.",
                "choice_B": "위험하더라도 항구를 개방하여 \n서양의 근대 기술과 문물을 적극적으로 받아들이는 \n'개항 정책'을 펼친다",
                "fact_A": "[역사 사실]\n흥선대원군은 병인양요, 신미양요를 거치며 전국에 척화비를 세우고 서양과의 교류를 거부했습니다. \n이는 외세의 침략을 일시적으로 막았으나 대외 교류와 근대화를 늦추는 결과를 낳았습니다 .",
                "fact_B": "[역사 사실]\n조선은 1876년 강화도 조약을 시작으로 개항했습니다. \n이후 근대 문물을 받아들이고 개혁을 추진했으나, 준비가 부족한 상태에서 불평등 조약을 맺어 외세에 이권을 많이 빼앗기는 아픔을 겪었습니다."
            },
            {
                "id": 3,
                "question": "일제강점기 독립운동 단체 '의열단'의 단원인 당신,\n일본 순사에게 붙잡혀 고문받기 직전의 선택은?",
                "choice_A": "동료들의 아지트를 밀고하고\n나 혼자 살아남아 \n평생 부자로 산다",
                "choice_B": "혀를 깨물고 비밀을 지키며\n모진 고문을 견디다 \n감옥에서 순국한다",
                "fact_A": "💡 [역사 사실]\n당시 일제의 가혹한 고문을 이기지 못하고 변절하여 스파이가 된 이들은 독립운동에 큰 피해를 주었습니다.",
                "fact_B": "💡 [역사 사실]\n당시 수많은 단원들은 상상을 초월하는 고문 속에서도 끝까지 비밀을 지키며 순국하셨습니다."
            }
        ]


current_index = 0
user_choices = []

def 다음문제로():
    global current_index
    
    if current_index < len(questions):
        q = questions[current_index]
        q_label.config(text=f"Q{q['id']}. {q['question']}")
        btn_A.config(text=q['choice_A'])
        btn_B.config(text=q['choice_B'])
        status_label.config(text=f"진행도: {current_index + 1} / {len(questions)}")
    else:
        result_msg = "🎉 게임이 모두 종료되었습니다! 🎉\n\n 당신의 역사적 선택 요약:\n"
        for choice in user_choices:
            result_msg += f" - {choice}\n"
        messagebox.showinfo("게임 종료", result_msg)
        window.quit()

def 버튼클릭(choice):
    global current_index
    q = questions[current_index]
    
    user_choices.append(f"Q{q['id']}: {choice}")
    fact_text = q['fact_A'] if choice == 'A' else q['fact_B']
    messagebox.showinfo("🧐 선택 분석 및 역사 사실", fact_text)
    
    current_index += 1
    다음문제로()

title_label = tk.Label(window, text="📜 역사 밸런스 게임", font=("맑은 고딕", 18, "bold"), fg="#333333")
title_label.pack(pady=15)

q_label = tk.Label(window, text="", font=("맑은 고딕", 13, "bold"), justify="center", height=4, fg="#555555")
q_label.pack(pady=10, fill="x")

btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)

btn_A = tk.Button(btn_frame, text="", font=("맑은 고딕", 11), width=24, height=4, 
                  bg="#ffdddd", activebackground="#ffcccc", command=lambda: 버튼클릭('A'))
btn_A.grid(row=0, column=0, padx=15)

btn_B = tk.Button(btn_frame, text="", font=("맑은 고딕", 11), width=24, height=4, 
                  bg="#ddeeff", activebackground="#ccddff", command=lambda: 버튼클릭('B'))
btn_B.grid(row=0, column=1, padx=15)

status_label = tk.Label(window, text="", font=("맑은 고딕", 10), fg="#888888")
status_label.pack(side="bottom", pady=15)

다음문제로()

window.mainloop()
