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