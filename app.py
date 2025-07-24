import streamlit as st
import random
import matplotlib.pyplot as plt

# 전역 스타일
st.markdown("""
    <style>
    .card-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9;
        padding: 20px;
        margin-bottom: 18px;
    }
    .card-box .question {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# 질문 목록 (카테고리는 계산용)
questions = [
    ("나는 감정을 드러내기보다 속으로 처리하는 편이다.", "teto"),
    ("논쟁에서는 상대를 이기고 싶다는 생각이 든다.", "teto"),
    ("일을 할 때 누가 더 잘하나 경쟁심이 생긴다.", "teto"),
    ("나는 위로보다는 해결책을 주는 쪽이다.", "teto"),
    ("리더가 되는 자리를 부담스럽게 느끼지 않는다.", "teto"),
    ("감정에 휘둘리는 사람을 보면 불편하다.", "teto"),
    ("조직 내에서 서열과 룰이 명확해야 편하다.", "teto"),
    ("관계보다 나 자신을 먼저 챙겨야 한다고 생각한다.", "teto"),
    ("상대의 말보다 표정이나 분위기를 먼저 읽는다.", "egen"),
    ("친구가 울면 나도 눈물이 핑 돈 적이 있다.", "egen"),
    ("누군가 다쳤을 때 먼저 감정적으로 반응한다.", "egen"),
    ("감정적으로 힘든 사람에게 오래 공감해줄 수 있다.", "egen"),
    ("내 기분은 주변 사람의 분위기에 따라 잘 변한다.", "egen"),
    ("주변 사람과 갈등이 생기면 먼저 화해를 시도한다.", "egen"),
    ("감정 표현을 솔직하게 하는 게 오히려 관계를 좋게 만든다.", "egen")
]

random.seed(42)
random.shuffle(questions)

options = ["매우 그렇다", "그렇다", "아니다", "전혀 아니다"]
score_map = {"매우 그렇다": 3, "그렇다": 2, "아니다": 1, "전혀 아니다": 0}

def calculate_result(gender, teto_score, egen_score):
    total = teto_score + egen_score
    if total == 0:
        return "혼합형", 50, 50
    teto_p = (teto_score / total) * 100
    egen_p = 100 - teto_p
    if teto_p > 50:
        return ("테토남" if gender == "남성" else "테토녀"), teto_p, egen_p
    elif egen_p > 50:
        return ("에겐남" if gender == "남성" else "에겐녀"), teto_p, egen_p
    return "혼합형", teto_p, egen_p

descriptions = {
    "테토남": """🧠 **테토남** ｜ 논리적이고 목표 지향적인 리더형 남성\n\n논리적 사고와 명확한 목표로 스스로를 이끄는 유형입니다. 📊 분석, 전략, 구조에 강하며 리더십이 자연스럽습니다.""",
    "에겐남": """💓 **에겐남** ｜ 따뜻하고 공감력이 뛰어난 감성형 남성\n\n감정 흐름을 잘 읽고 타인의 감정에 공감하는 따뜻한 유형입니다. 🤝 관계와 조화를 중시하며 감정 표현이 자연스럽습니다.""",
    "테토녀": """📐 **테토녀** ｜ 이성적이고 주도적인 전략가형 여성\n\n이성적이고 체계적인 사고로 능동적인 삶을 이끄는 유형입니다. 🗂️ 계획과 효율을 중시하며 독립성과 리더십이 돋보입니다.""",
    "에겐녀": """🌷 **에겐녀** ｜ 감성적이고 따뜻한 공감형 여성\n\n배려심과 공감 능력을 바탕으로 관계를 중시하는 유형입니다. 💞 갈등보다는 이해와 조화를 추구합니다.""",
    "혼합형": """⚖️ **혼합형** ｜ 이성과 감성의 균형을 갖춘 유연형\n\n논리와 감정을 균형 있게 활용하며 유연하게 반응하는 유형입니다. 🔀 조율자 역할을 잘 수행합니다."""
}

images = {
    "테토남": "https://images.unsplash.com/photo-1610563166154-9b7be0b11a06?auto=format&fit=crop&w=1200&q=80",
    "에겐남": "https://images.unsplash.com/photo-1594824476967-48c8b9642731?auto=format&fit=crop&w=1200&q=80",
    "테토녀": "https://images.unsplash.com/photo-1586281380381-52c3ea5484d2?auto=format&fit=crop&w=1200&q=80",
    "에겐녀": "https://images.unsplash.com/photo-1617038491894-5b18d376ef1b?auto=format&fit=crop&w=1200&q=80",
    "혼합형": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1200&q=80"
}

st.title("🧠 테토/에겐 성향 테스트")
gender = st.radio("당신의 성별은?", ["남성", "여성"])

st.subheader("📝 아래 문항에 응답해주세요")
teto_score = 0
egen_score = 0

for i, (q, cat) in enumerate(questions):
    with st.container():
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='question'>{q}</div>", unsafe_allow_html=True)
        answer = st.radio(" ", options, key=f"q_{i}", label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        score = score_map[answer]
        if cat == "teto": teto_score += score
        else: egen_score += score

if st.button("결과 보기"):
    result_type, teto_percent, egen_percent = calculate_result(gender, teto_score, egen_score)

    st.markdown("---")
    st.header(f"✅ 당신은 '{result_type}'입니다.")
    st.image(images[result_type], use_container_width=True)
    st.write(f"테토 성향 비율: {teto_percent:.1f}%")
    st.write(f"에겐 성향 비율: {egen_percent:.1f}%")

    fig, ax = plt.subplots()
    ax.pie([teto_percent, egen_percent], labels=['테토', '에겐'], autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff9999'])
    ax.axis('equal')
    st.pyplot(fig)

    st.markdown(descriptions[result_type])
