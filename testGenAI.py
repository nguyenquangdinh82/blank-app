import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyBHb1kxosSIwj0F-cujdrVZAWKoCtuxB84"
genai.configure(api_key=GOOGLE_API_KEY)

""" instruction = (
    "You are a coding expert that specializes in front end interfaces. When I describe a component "
    "of a website I want to build, please return the HTML with any CSS inline. Do not give an "
    "explanation for this code but translate it to Vietnamese."
) """
instruction = ("Bạn là một trợ lý thông minh, luôn sẵn sàng giúp người dùng tạo và quản lý "
               "danh sách nhiệm vụ phải làm và không một lời giải thích.")

model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instruction)

prompt = "Tự xét là gì?"
response = model.generate_content(prompt)
print(response.text)
"""
import streamlit as st
import google.generativeai as genai

# Cấu hình API key (thay "abc" bằng API key thật của bạn)
GOOGLE_API_KEY = "AIzaSyBHb1kxosSIwj0F-cujdrVZAWKoCtuxB84"
genai.configure(api_key=GOOGLE_API_KEY)

# Khởi tạo mô hình Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

# Tiêu đề ứng dụng
st.title("Trò chuyện với Gemini")

# Lưu trữ lịch sử chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Hiển thị nội dung chat
        st.markdown(message["content"])

# Nhận input từ người dùng
if prompt := st.chat_input("Nhập tin nhắn của bạn"):
    # Thêm tin nhắn của người dùng vào lịch sử
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Hiển thị tin nhắn của người dùng
    with st.chat_message("user"):
        st.markdown(prompt)
        # Thêm nút sao chép (sử dụng JavaScript để sao chép)
        st.markdown(f'<button onclick="navigator.clipboard.writeText(\'{prompt}\')">Sao chép</button>', unsafe_allow_html=True)

    # Gọi API Gemini để tạo phản hồi
    try:
        response = model.generate_content(prompt)

        # Kiểm tra phản hồi từ API
        if response.text:
            # Thêm phản hồi của Gemini vào lịch sử
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            # Hiển thị phản hồi của Gemini
            with st.chat_message("assistant"):
                st.markdown(response.text)
                # Thêm nút sao chép (sử dụng JavaScript để sao chép)
                st.markdown(f'<button onclick="navigator.clipboard.writeText(\'{response.text}\')">Sao chép</button>', unsafe_allow_html=True)
        else:
            st.error("Gemini không thể tạo phản hồi. Vui lòng thử lại sau.")
    except Exception as e:
        st.error(f"Đã xảy ra lỗi khi gọi API Gemini: {e}")
"""