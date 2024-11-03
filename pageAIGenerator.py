import streamlit as st
import json
import os
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyBHb1kxosSIwj0F-cujdrVZAWKoCtuxB84"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# File để lưu trữ dữ liệu
DATA_FILE = 'saved_data.json'

# Hàm lưu và tải dữ liệu
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        else:
            return {}
    except json.JSONDecodeError:  # Xử lý lỗi nếu file JSON bị hỏng
        return {}


# Khởi tạo row_count trong session_state. Đảm bảo nó luôn được khởi tạo.
if 'row_count' not in st.session_state:
    st.session_state['row_count'] = 1

# Tải dữ liệu đã lưu.  Sử dụng try-except để bắt lỗi nếu file JSON bị hỏng.
loaded_data = load_data()

# Cập nhật row_count từ dữ liệu đã lưu (nếu có).
if 'row_count' in loaded_data:
    st.session_state['row_count'] = loaded_data['row_count']

# Khởi tạo session state từ dữ liệu đã lưu nếu có.
for i in range(st.session_state['row_count']):
    st.session_state.setdefault(f'text_input1_{i}', loaded_data.get(f'text_input1_{i}', ''))
    st.session_state.setdefault(f'text_input2_{i}', loaded_data.get(f'text_input2_{i}', ''))

# Hàm thêm hàng mới
def add_row():
    st.session_state[f'text_input1_{st.session_state["row_count"]}'] = ''
    st.session_state[f'text_input2_{st.session_state["row_count"]}'] = ''
    st.session_state['row_count'] += 1

# Hiển thị các hàng
for row in range(st.session_state['row_count']):
    cols = st.columns([2, 0.5, 2])
    with cols[0]:
        st.text_area(f"Input_{row+1}:", key=f"text_input1_{row}")
    with cols[1]:
        if st.button(f"AI_{row+1}", key=f"test_button_{row}"):
            response = model.generate_content(st.session_state[f'text_input1_{row}'])
            st.session_state[f'text_input2_{row}'] = response.text
    with cols[2]:
        st.markdown(f"**Reply**_{row+1}: {st.session_state[f'text_input2_{row}']}")

# Thêm nút để thêm hàng mới
if st.button("+++"):
    add_row()

# Lưu dữ liệu vào file
save_data({f'text_input1_{i}': st.session_state[f'text_input1_{i}'] for i in range(st.session_state['row_count'])} |
          {f'text_input2_{i}': st.session_state[f'text_input2_{i}'] for i in range(st.session_state['row_count'])} |
          {'row_count': st.session_state['row_count']})