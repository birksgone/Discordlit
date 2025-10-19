# pages/3_Timestamp_Generator.py
import streamlit as st
from datetime import datetime, time # timeをインポート
import pytz

st.title("🕒 Discord Timestamp Generator")
st.write("Generate dynamic timestamps that display correctly for everyone in their own time zone.")
st.caption("Perfect for scheduling international events!")

# --- 利用可能なタイムゾーンのリスト ---
all_timezones = pytz.all_timezones
common_timezones = [
    "UTC", "Asia/Tokyo", "US/Pacific", "US/Mountain", "US/Central", "US/Eastern",
    "Europe/London", "Europe/Berlin", "Europe/Moscow", "Australia/Sydney"
]
# 重複をなくしつつ、common_timezonesを先頭にしたリストを作成
sorted_timezones = sorted(list(set(common_timezones + all_timezones)))
# デフォルトのタイムゾーンをUTCに固定
default_timezone_index = sorted_timezones.index("UTC")


# --- UI ---
st.header("1. Input Date and Time")
col1, col2 = st.columns(2)
with col1:
    # 日付のデフォルトは現在の日付
    d = st.date_input("Date", help="Select the date of your event.")
with col2:
    # ★★★ 時刻のデフォルトを午前7時に設定 ★★★
    t = st.time_input("Time", value=time(7, 0), help="Select the time of your event.")

st.header("2. Select The Event's Time Zone")
st.write("Select the time zone where the date and time above are based.")
user_timezone_str = st.selectbox(
    "Event Time Zone",
    sorted_timezones,
    index=default_timezone_index, # ★★★ デフォルトをUTCに固定 ★★★
    help="Type to search for your city or time zone."
)

st.divider()

# --- 実行ボタン ---
if st.button("Generate Timestamps", type="primary"):
    try:
        user_timezone = pytz.timezone(user_timezone_str)
        # ユーザーが入力した日付と時刻を組み合わせる
        dt_local = datetime.combine(d, t)
        # タイムゾーン情報を付加する
        dt_aware = user_timezone.localize(dt_local)
        
        unix_timestamp = int(dt_aware.timestamp())

        # --- 結果表示 ---
        st.header("3. Copy Your Timestamps")
        st.info(f"The time below corresponds to **{dt_aware.strftime('%Y-%m-%d %H:%M')}** in **{user_timezone_str}**. Actual display is based on each user's local time zone.")

        formats = {
            "Short Time":      ("t", "%I:%M %p"),
            "Long Time":       ("T", "%I:%M:%S %p"),
            "Short Date":      ("d", "%m/%d/%Y"),
            "Long Date":       ("D", "%B %d, %Y"),
            "Short Date/Time": ("f", "%B %d, %Y %I:%M %p"),
            "Long Date/Time":  ("F", "%A, %B %d, %Y %I:%M %p"),
            "Relative Time":   ("R", None)
        }

        for style, (code_char, strftime_format) in formats.items():
            st.subheader(style)
            
            col1, col2 = st.columns([2, 3])
            
            with col1:
                st.write("**Preview:**")
                if strftime_format:
                    st.success(f"{dt_aware.strftime(strftime_format)}")
                else:
                    st.info("e.g., in 2 hours")

            with col2:
                st.write("**Discord Code:**")
                st.code(f"<t:{unix_timestamp}:{code_char}>", language="")

    except Exception as e:
        st.error(f"An error occurred: {e}")