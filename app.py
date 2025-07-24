import streamlit as st
import random
import matplotlib.pyplot as plt

# 질문 목록 (카테고리는 계산에만 사용되고 사용자에게는 보이지 않음)
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

images = {
    "테토남": "https://images.unsplash.com/photo-1610563166154-9b7be0b11a06?auto=format&fit=crop&w=1200&q=80",
    "에겐남": "https://images.unsplash.com/photo-1594824476967-48c8b9642731?auto=format&fit=crop&w=1200&q=80",
    "테토녀": "https://images.unsplash.com/photo-1586281380381-52c3ea5484d2?auto=format&fit=crop&w=1200&q=80",
    "에겐녀": "https://images.unsplash.com/photo-1617038491894-5b18d376ef1b?auto=format&fit=crop&w=1200&q=80",
    "혼합형": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1200&q=80"
}

def calculate_result(gender, teto_score, egen_score):
    total_score = teto_score + egen_score
    if total_score == 0:
        teto_percent = egen_percent = 50
    else:
        teto_percent = (teto_score / total_score) * 100
        egen_percent = (egen_score / total_score) * 100

    if teto_percent > 50:
        if gender == "남성":
            return "테토남", teto_percent, egen_percent
        else:
            return "테토녀", teto_percent, egen_percent
    elif egen_percent > 50:
        if gender == "남성":
            return "에겐남", teto_percent, egen_percent
        else:
            return "에겐녀", teto_percent, egen_percent
    else:
        return "혼합형", teto_percent, egen_percent

# ✅ 성향별 설명
descriptions = {
    "테토남": "🧠 논리적이고 목표 지향적인 리더형 남성",
    "에겐남": "💓 따뜻하고 공감력이 뛰어난 감성형 남성",
    "테토녀": "📐 이성적이고 주도적인 전략가형 여성",
    "에겐녀": "🌷 감성적이고 따뜻한 공감형 여성",
    "혼합형": "⚖️ 이성과 감성의 균형을 갖춘 유연형"
}

images = {
    "테토남": "https://images.unsplash.com/photo-1610563166154-9b7be0b11a06?auto=format&fit=crop&w=1200&q=80",
    "에겐남": "https://images.unsplash.com/photo-1594824476967-48c8b9642731?auto=format&fit=crop&w=1200&q=80",
    "테토녀": "https://images.unsplash.com/photo-1586281380381-52c3ea5484d2?auto=format&fit=crop&w=1200&q=80",
    "에겐녀": "https://images.unsplash.com/photo-1617038491894-5b18d376ef1b?auto=format&fit=crop&w=1200&q=80",
    "혼합형": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1200&q=80"
}

# 스타일 삽입
st.markdown("""
    <style>
        .card {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 0px;
            background-color: #f2f2f2;
        }
        .question-text {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 0px;
        }
        .stRadio > div {
            margin-top: -10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 테토/에겐 성향 테스트")

with st.container():
    with st.expander("", expanded=True):
        st.markdown("""
            <div class='card'>
                <div class='question-text'>당신의 성별은?</div>
            """, unsafe_allow_html=True)
        gender = st.radio(" ", ["남성", "여성"], index=None)
        st.markdown("</div>", unsafe_allow_html=True)

st.subheader("📝 아래 문항에 응답해주세요")
teto_score = 0
egen_score = 0

for i, (q, category) in enumerate(questions):
    with st.container():
        with st.expander("", expanded=True):
            st.markdown(f"<div class='card'><div class='question-text'>{q}</div>", unsafe_allow_html=True)
            answer = st.radio(" ", options, key=f"q_{i}", index=None)
            st.markdown("</div>", unsafe_allow_html=True)

            if answer:
                score = score_map[answer]
                if category == "teto":
                    teto_score += score
                else:
                    egen_score += score

# 성향별 설명 추가
descriptions = {
    "테토남": (
        "🧠 **테토남** ｜ 논리적이고 목표 지향적인 리더형 남성\n\n"
        "당신은 논리적 사고와 명확한 목표 지향성을 바탕으로 스스로를 이끄는 **테토남** 유형입니다. "
        "📊 문제 해결을 위한 분석과 전략 수립에 능하며, 감정보다는 이성을 우선시하려는 경향이 있습니다. "
        "🏁 자신만의 기준과 방향이 분명하고, 경쟁 상황에서도 자신감을 가지고 적극적으로 임합니다. "
        "🏗️ 조직 내에서 역할과 구조가 명확할 때 안정감을 느끼며, 리더십을 발휘하는 데에도 거리낌이 없습니다."
    ),
    "에겐남": (
        "💓 **에겐남** ｜ 따뜻하고 공감력이 뛰어난 감성형 남성\n\n"
        "당신은 감정의 흐름을 잘 읽고 타인의 감정에 깊이 공감하는 따뜻한 **에겐남** 유형입니다. "
        "🌈 관계와 조화를 중요하게 여기며, 분위기와 표정 같은 신호에도 민감하게 반응합니다. "
        "🤝 힘든 사람에게 공감과 위로를 전하며, 감정 표현을 통해 관계를 깊게 만들어갑니다."
    ),
    "테토녀": (
        "📐 **테토녀** ｜ 이성적이고 주도적인 전략가형 여성\n\n"
        "당신은 이성적이고 체계적인 사고를 바탕으로 능동적으로 삶을 이끄는 **테토녀** 유형입니다. "
        "🗂️ 계획을 세우고 효율을 중시하며, 감정보다 구조와 논리에 따라 움직입니다. "
        "👑 리더십을 발휘하고 책임감 있게 행동하며, 독립적인 성향이 강합니다."
    ),
    "에겐녀": (
        "🌷 **에겐녀** ｜ 감성적이고 따뜻한 공감형 여성\n\n"
        "당신은 따뜻한 감성과 깊은 공감 능력을 바탕으로 관계를 중시하는 **에겐녀** 유형입니다. "
        "💞 감정 중심의 소통을 선호하고, 갈등을 피하기보다는 화해와 이해를 시도합니다. "
        "🌟 배려심 깊고 섬세한 감성 리더십을 가지고 있습니다."
    ),
    "혼합형": (
        "⚖️ **혼합형** ｜ 이성과 감성의 균형을 갖춘 유연형\n\n"
        "당신은 상황에 따라 논리와 감정을 균형 있게 활용하는 **혼합형** 성향입니다. "
        "🔀 분석과 공감을 모두 중요하게 생각하며, 유연하고 조화로운 성향을 지녔습니다. "
        "🤲 다양한 상황에서 조율자나 중재자로서의 역량을 발휘합니다."
    )
}

# ✅ [추가된 부분 2] 성별 선택 안 했을 경우 경고
if st.button("결과 보기"):
    if gender is None:
        st.warning("성별을 선택해주세요.")
    else:
        result_type, teto_percent, egen_percent = calculate_result(gender, teto_score, egen_score)

        st.markdown("---")
        st.header(f"✅ 당신은 '{result_type}'입니다.")
        st.image(images[result_type], use_container_width=True)
        st.write(f"테토 성향 비율: {teto_percent:.1f}%")
        st.write(f"에겐 성향 비율: {egen_percent:.1f}%")

        fig, ax = plt.subplots()
        labels = ['Teto', 'Egen']
        sizes = [teto_percent, egen_percent]
        colors = ['#66b3ff', '#ff9999']
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')
        st.pyplot(fig)

        st.markdown(descriptions[result_type])
