import streamlit as st
from datetime import datetime, timedelta
import time

st.set_page_config(page_title="siddy countdown", page_icon=":smiley:")

# Set the target date for the countdown
target_date = datetime(2024, 7, 25, 22, 30)

def get_time_remaining(target_date):
    now = datetime.now()
    time_remaining = target_date - now
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
        text-align: center;
        margin-top: 60px;
    }
    .countdown-box {
        font-size:30px !important;
        text-align: center;
        background-color: #f0f8ff;
        border: 2px solid #87ceeb;
        padding: 20px;
        border-radius: 10px;
        color: black;
        width: 45vh;
        margin: auto;
    }
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .image-container {
        padding: 20px;
    }
    .image {
        max-width: 500px;
        height: auto;
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #87ceeb;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 style="text-align: center;">days until i see siddy again 🔥</h1>', unsafe_allow_html=True)

placeholder = st.empty()

with st.container() as main_container:

    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image("photo.png", width=800, use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

while True:
    days, hours, minutes, seconds = get_time_remaining(target_date)
    with placeholder.container():
        st.markdown('<p class="big-font">time until august 26</p>', unsafe_allow_html=True)
        st.markdown(f"<div class='countdown-box'>{days} days, {hours}h, {minutes}m, {seconds}s</div>", unsafe_allow_html=True)
    time.sleep(1)

st.title("bye sid.")
