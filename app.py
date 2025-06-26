import streamlit as st
import matplotlib.pyplot as plt

# اللغة الافتراضية
اللغة = "ar"

# النصوص حسب اللغة
النصوص = {
    "ar": {
        "title": "تحليل ذكاء توزيع الوقت",
        "sleep": "كم ساعة نمت؟",
        "phone": "كم ساعة قضيتها على الهاتف؟",
        "study": "كم ساعة درست أو عملت؟",
        "waste": "كم ساعة ضاعت دون فائدة؟",
        "analyze": "تحليل الآن",
        "results": "نتائج التحليل",
        "error": "يرجى إدخال أرقام صحيحة فقط.",
        "analysis": "🔍 تقييم وتحليل:",
        "sleep_low": "✉ نوم غير كافٍ: يفضل النوم من 7 إلى 8 ساعات.",
        "sleep_ok": "✔ نوم جيد: ممتاز، استمر في ذلك.",
        "phone_high": "⚠ وقت الهاتف مرتفع: حاول تقليله إلى أقل من 3 ساعات.",
        "phone_ok": "✔ وقت الهاتف مقبول.",
        "study_low": "⚠ وقت الدراسة قليل: حاول زيادته تدريجيًا.",
        "study_ok": "✔ ممتاز، وقت الدراسة مناسب.",
        "waste_high": "⚠ وقت ضائع كبير: حاول استغلاله في نشاط مفيد.",
        "waste_ok": "✔ إدارة الوقت جيدة.",
        "tips": "\n📌 نصائح لإدارة وقتك بشكل أفضل:\n- خصص وقتًا ثابتًا للنوم والاستيقاظ.\n- قلل من تصفح الهاتف بدون هدف.\n- استخدم تقنيات مثل بومودورو في الدراسة.\n- خطط يومك في بداية كل صباح أو قبل النوم."
    },
    "en": {
        "title": "Smart Time Distribution Analyzer",
        "sleep": "How many hours did you sleep?",
        "phone": "How many hours on phone?",
        "study": "How many hours did you study/work?",
        "waste": "How many hours were wasted?",
        "analyze": "Analyze Now",
        "results": "Analysis Results",
        "error": "Please enter valid numbers only.",
        "analysis": "🔍 Analysis Summary:",
        "sleep_low": "✉ Not enough sleep: Aim for 7–8 hours.",
        "sleep_ok": "✔ Good sleep: Well done.",
        "phone_high": "⚠ Too much phone time: Reduce to < 3 hrs.",
        "phone_ok": "✔ Phone time is fine.",
        "study_low": "⚠ Not enough study/work: Try to increase it.",
        "study_ok": "✔ Good study/work time.",
        "waste_high": "⚠ Too much wasted time: Use it productively.",
        "waste_ok": "✔ Good time management.",
        "tips": "\n📌 Time Management Tips:\n- Set a fixed sleep schedule.\n- Avoid endless phone scrolling.\n- Use Pomodoro technique for work.\n- Plan your day each morning or night."
    }
}

st.set_page_config(page_title=النصوص[اللغة]["title"], layout="centered")
st.title(النصوص[اللغة]["title"])

نوم = st.number_input(النصوص[اللغة]["sleep"], min_value=0.0, step=0.5)
هاتف = st.number_input(النصوص[اللغة]["phone"], min_value=0.0, step=0.5)
دراسة = st.number_input(النصوص[اللغة]["study"], min_value=0.0, step=0.5)
ضائع = st.number_input(النصوص[اللغة]["waste"], min_value=0.0, step=0.5)

if st.button(النصوص[اللغة]["analyze"]):
    try:
        مجموع = نوم + هاتف + دراسة + ضائع
        if مجموع == 0:
            st.warning(النصوص[اللغة]["error"])
        else:
            نسب = [(نوم / مجموع) * 100, (هاتف / مجموع) * 100, (دراسة / مجموع) * 100, (ضائع / مجموع) * 100]
            التصنيفات = [نصوص[اللغة]["sleep"], نصوص[اللغة]["phone"], نصوص[اللغة]["study"], نصوص[اللغة]["waste"]]
            ألوان = ["#4CAF50", "#FF9800", "#2196F3", "#F44336"]

            fig, ax = plt.subplots()
            ax.pie(نسب, labels=التصنيفات, autopct="%.1f%%", startangle=90, colors=ألوان)
            ax.axis("equal")
            st.pyplot(fig)

            توصيات = نصوص[اللغة]["analysis"]
            توصيات += "\n" + (نصوص[اللغة]["sleep_low"] if نوم < 6 else نصوص[اللغة]["sleep_ok"])
            توصيات += "\n" + (نصوص[اللغة]["phone_high"] if هاتف > 3 else نصوص[اللغة]["phone_ok"])
            توصيات += "\n" + (نصوص[اللغة]["study_low"] if دراسة < 4 else نصوص[اللغة]["study_ok"])
            توصيات += "\n" + (نصوص[اللغة]["waste_high"] if ضائع > 3 else نصوص[اللغة]["waste_ok"])
            توصيات += "\n" + نصوص[اللغة]["tips"]

            st.markdown(f"""
            <div style='background-color:#f9f9f9; padding:15px; border-radius:10px;'>
                <pre>{توصيات}</pre>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"{النصوص[اللغة]['error']}: {str(e)}")
