import tkinter as tk
from tkinter import messagebox

KING_DATA = {
    "ISTJ": {
        "왕": "태종",
        "업적": "• 6조 직계제 실시\n• 호패법 시행을 통해 왕권을 강화하고 국가 기틀을 마련했습니다."
    },
    "ISFJ": {
        "왕": "정조",
        "업적": "• 탕평책 추진, 규장각 설립\n• 화성 축조를 통해 조선의 부흥기를 이끌었습니다."
    },
    "INFJ": {
        "왕": "세종대왕",
        "업적": "• 훈민정음 창제\n• 측우기와 자격루 제작 등 과학·문화·국방 전반에 찬란한 업적을 남겼습니다."
    },
    "INTJ": {
        "왕": "영조",
        "업적": "• 탕평책을 통해 당쟁을 완화했습니다.\n• 균역법을 실시하여 백성들의 군역 부담을 줄였습니다."
    },
    "ISTP": {
        "왕": "세조",
        "업적": "• 집현전을 폐지하고 직전법을 실시했습니다.\n• 재정을 확보하는 등 강력한 왕권을 행사했습니다."
    },
    "ISFP": {
        "왕": "인종",
        "업적": "• 성품이 어질고 효성이 지극했습니다.\n• 현량과를 부활시키는 등 도학 정치를 펴려 노력했습니다."
    },
    "INFP": {
        "왕": "단종",
        "업적": "• 어린 나이에 왕위에 올라 비극적인 삶을 살았습니다.\n• 그의 충신들의 절개는 후대에 큰 귀감이 되었습니다."
    },
    "INTP": {
        "왕": "광해군",
        "업적": "• 명나라와 후금 사이에서 실리적인 중립 외교를 펼쳤습니다.\n• 대동법을 경기도에 시범 실시했습니다."
    },
    "ESTP": {
        "왕": "연산군",
        "업적": "• 무오사화와 갑자사화를 일으켜 많은 선비들을 숙청했습니다.\n• 절대적인 왕권을 구축하려 했습니다."
    },
    "ESFP": {
        "왕": "숙종",
        "업적": "• 대동법을 전국적으로 확대 시행했습니다.\n• 상평통보를 주조하여 유통하는 등 경제 발전을 이끌었습니다."
    },
    "ENFP": {
        "왕": "중종",
        "업적": "• 조광조를 등용하여 도학 정치를 실현하려 했습니다.\n• 신진 사림을 대거 중용했습니다."
    },
    "ENTP": {
        "왕": "성종",
        "업적": "• 조선의 기본 법전인 '경국대전'을 완성했습니다.\n• 국가의 통치 체제를 확립했습니다."
    },
    "ESTJ": {
        "왕": "태조 이성계",
        "업적": "• 고려를 무너뜨리고 조선을 건국하였습니다.\n• 한양으로 천도하여 새로운 나라의 기틀을 다졌습니다."
    },
    "ESFJ": {
        "왕": "문종",
        "업적": "• 세종을 도와 측우기 제작에 기여하였습니다.\n• 고려사와 고려사절요 편찬을 주도했습니다."
    },
    "ENFJ": {
        "왕": "선조",
        "업적": "• 임진왜란이라는 국가적 위기를 겪었습니다.\n• 이순신, 권율 등 명장들을 등용하여 국난을 극복했습니다."
    },
    "ENTJ": {
        "왕": "고종",
        "업적": "• 대한제국을 선포하고 광무개혁을 추진했습니다.\n• 근대 국가로 나아가기 위한 노력을 기울였습니다."
    }
}

def show_result():

    mbti = entry.get().strip().upper()
    
    
    if mbti in KING_DATA:
        king_info = KING_DATA[mbti]
        
        
        result_text.delete("1.0", tk.END)
        
        result_text.insert(tk.END, f" 당신의 MBTI [{mbti}]와 매칭되는 왕은?\n\n")
        result_text.insert(tk.END, f"【 {king_info['왕']} 】 입니다!\n\n")
        result_text.insert(tk.END, f"주요 업적:\n{king_info['업적']}")
  
window = tk.Tk()
window.title("조선시대 왕 MBTI 추천기")
window.geometry("700x700")


title_label = tk.Label(window, text="내 MBTI와 닮은 조선의 왕은?")
title_label.pack(pady=15)


input_frame = tk.Frame(window)
input_frame.pack(pady=10)

label = tk.Label(input_frame, text="MBTI 입력 : ")
label.pack(side=tk.LEFT)

entry = tk.Entry(input_frame, width=10)
entry.pack(side=tk.LEFT, padx=5)


btn = tk.Button(window, text="결과 확인하기",command=show_result)
btn.pack(pady=10)


result_text = tk.Text(window,width=45, height=12)
result_text.pack(pady=10, padx=15)


window.mainloop()
