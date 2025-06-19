import tkinter as tk
from gtts import gTTS
import os
import playsound
import threading

# Hàm xử lý chuyển đổi và phát âm thanh
def convert_and_play():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        status_label.config(text="Vui lòng nhập văn bản!")
        return

    status_label.config(text="Đang chuyển đổi...")
    language = 'vi'  # Ngôn ngữ mặc định là tiếng Việt

    def process():
        try:
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save("output.mp3")
            playsound.playsound("output.mp3", True)
            os.remove("output.mp3")
            status_label.config(text="Hoàn tất!")
        except Exception as e:
            status_label.config(text=f"Lỗi: {str(e)}")

    # Chạy trong luồng riêng để giao diện không bị treo
    threading.Thread(target=process).start()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi văn bản thành giọng nói")
root.geometry("400x300")
root.configure(bg="#f0f0f0")  # Màu nền nhẹ nhàng

# Tiêu đề
title_label = tk.Label(root, text="Chuyển đổi văn bản thành giọng nói", 
                       font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=10)

# Hộp văn bản
text_box = tk.Text(root, height=10, width=40, font=("Arial", 12), 
                   borderwidth=2, relief="groove")
text_box.pack(pady=10)

# Nút chuyển đổi
convert_button = tk.Button(root, text="Chuyển đổi và phát", 
                           font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", 
                           command=convert_and_play, borderwidth=0, padx=10, pady=5)
convert_button.pack(pady=10)

# Nhãn trạng thái
status_label = tk.Label(root, text="", font=("Arial", 12, "italic"), 
                        bg="#f0f0f0", fg="#666666")
status_label.pack(pady=10)

# Chạy ứng dụng
root.mainloop()