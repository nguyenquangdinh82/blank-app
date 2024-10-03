import streamlit as st
import json
import os

# File để lưu trữ dữ liệu
DATA_FILE = 'saved_data.json'

# Hàm lưu và tải dữ liệu
def save_data(data): 
    with open(DATA_FILE, 'w') as f: json.dump(data, f)
def load_data(): 
    return json.load(open(DATA_FILE)) if os.path.exists(DATA_FILE) else {}

# Tải dữ liệu đã lưu
loaded_data = load_data()

# Khởi tạo session state từ dữ liệu đã lưu nếu có
row_count = loaded_data.get('row_count', 1)
for i in range(row_count):
    st.session_state.setdefault(f'text_input1_{i}', loaded_data.get(f'text_input1_{i}', ''))
    st.session_state.setdefault(f'text_input2_{i}', loaded_data.get(f'text_input2_{i}', ''))

# Hàm thêm hàng mới
def add_row():
    st.session_state[f'text_input1_{row_count}'] = ''
    st.session_state[f'text_input2_{row_count}'] = ''
    st.session_state['row_count'] += 1

# Hiển thị các hàng
for row in range(row_count):
    cols = st.columns([2, 0.5, 2])
    with cols[0]:
        st.text_input(f"input ({row+1})", key=f"text_input1_{row}")
    with cols[1]:
        if st.button(f"Test ({row+1})", key=f"test_button_{row}"):
            st.session_state[f'text_input2_{row}'] = st.session_state[f'text_input1_{row}']
    with cols[2]:
        st.text_input(f"reply ({row+1})", key=f"text_input2_{row}")

# Thêm nút để thêm hàng mới
if st.button("+++"): add_row()

# Lưu dữ liệu vào file
save_data({f'text_input1_{i}': st.session_state[f'text_input1_{i}'] for i in range(row_count)} | 
          {f'text_input2_{i}': st.session_state[f'text_input2_{i}'] for i in range(row_count)} |
          {'row_count': row_count})
