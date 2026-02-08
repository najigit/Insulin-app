import streamlit as st
import math

st.set_page_config(page_title="Insulin Calculator", layout="centered")

# ===== استایل سفارشی =====
st.markdown("""
<style>
html, body, [class*="css"]  {
    direction: rtl;
    text-align: right;
    font-family: Tahoma !important;
    font-size: 18px !important;
}

h1 {
    text-align: center;
    font-family: Tahoma !important;
}

h2, h3 {
    font-family: Tahoma !important;
}

div.stButton > button {
    background-color: #98FB98;
    color: black;
    font-size: 20px;
    height: 60px;
    width: 100%;
    border-radius: 12px;
    border: none;
}

div.stButton > button:hover {
    background-color: #77dd77;
}
</style>
""", unsafe_allow_html=True)

st.title("💉 محاسبه‌گر دوز انسولین")

# -----------------------------
# مرحله ۱
# -----------------------------
#st.header("مرحله ۱")

b = st.number_input(
    "قند قبل غذا را وارد کنید:",
    min_value=0,
    step=1,
    format="%d",
    value=None,
    placeholder="مثلاً 180"
)

g = 130

# اگر خالی باشد صفر در نظر گرفته شود
b = b if b is not None else 0

# -----------------------------
# مرحله ۲
# -----------------------------
#st.header("مرحله ۲")

meal = st.radio(
    "وعده غذایی را انتخاب کنید:",
    ("صبحانه", "ناهار", "شام")
)

if meal == "صبحانه" or meal == "شام":
    z = 2
elif meal == "ناهار":
    z = 1

# -----------------------------
# مرحله ۳
# -----------------------------
#st.header("مرحله ۳")

textbox1 = st.number_input(
    "تعداد نان (سنگک کف دست با انگشت/ بربری فقط کف دست):",
    min_value=0,
    step=1,
    format="%d",
    value=None,
    placeholder="0"
)

bread = st.radio(
    "نوع برنج وارد کنید:",
    ("آبکش یا مخلوط", "کته")
)
if bread == "آبکش یا مخلوط":
    k = 3
elif bread == "کته":
    k = 2

textbox2 = st.number_input(
    "تعداد قاشق برنج:",
    min_value=0,
    step=1,
    format="%d",
    value=None,
    placeholder="0"
)

textbox3 = st.number_input(
    " ماست / دوغ:",
    min_value=0,
    step=1,
    format="%d",
    value=None,
    placeholder="0"
)
textbox4 = st.number_input(
    " کاسه کامل عدسی/ نخود/ لوبیا:",
    min_value=0,
    step=1,
    format="%d",
    value=None,
    placeholder="0"
)

textbox5 = st.number_input(
    "  یک کاسه سوپ یا حلیم",
    min_value=0,
    step=1,
    format="%d",
    value=None,
    placeholder="0"
)
# اگر خالی باشند صفر شوند
textbox1 = textbox1 if textbox1 is not None else 0
textbox2 = textbox2 if textbox2 is not None else 0
textbox3 = textbox3 if textbox3 is not None else 0
textbox4 = textbox3 if textbox3 is not None else 0
textbox5 = textbox3 if textbox3 is not None else 0


c = textbox1 + (textbox2 / k) + (textbox3 /2) + textbox4 + (textbox5 * 2.5)

# -----------------------------
# مرحله ۴
# -----------------------------
#st.header("مرحله ۴")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    calculate = st.button("محاسبه انسولین")

if calculate:

    insulin = ((b - g) / 40) + (c * z)

    if insulin < 0:
        insulin = 0

    # ===== گرد کردن سفارشی =====
    decimal_part = insulin - math.floor(insulin)

    if decimal_part > 0.5:
        insulin_final = math.ceil(insulin)
    else:
        insulin_final = math.floor(insulin)

    if insulin_final>6
        insulin_final=6

    st.markdown("---")
    st.markdown(
        f"<h1 style='text-align:center; color:red;'>💉 {insulin_final} واحد</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h3 style='text-align:center;'>شما باید {insulin_final} واحد انسولین تزریق کنید</h3>",
        unsafe_allow_html=True
    )






