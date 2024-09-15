import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# Khởi tạo danh sách công việc (nếu chưa có)
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Nhập danh sách công việc
input_text = st.text_area("Nhập danh sách công việc, mỗi công việc trên một dòng:", 
                          value="""Dọn phòng 101
Dọn phòng 203
Kiểm tra phòng 305""")

# Nút thêm công việc
if st.button("Thêm công việc"):
    new_tasks = input_text.split("\n")
    st.session_state.tasks.extend(new_tasks)

# Tạo DataFrame từ danh sách công việc
df = pd.DataFrame({"Công việc": st.session_state.tasks, "Hoàn thành": [False] * len(st.session_state.tasks)})

# Hiển thị danh sách công việc với checkbox
for index, row in df.iterrows():
    checked = st.checkbox(row['Công việc'], key=f'checkbox_{index}', value=row['Hoàn thành'])
    df.at[index, 'Hoàn thành'] = checked
    if checked:
        # Lấy thời gian hiện tại ở Việt Nam
        vn_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
        current_time_vn = datetime.now(vn_timezone)
        st.write(f"               - Xong lúc {current_time_vn.strftime('%d-%m-%Y %H:%M:%S')}")