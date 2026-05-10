import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        
        # แปลงเซนติเมตรเป็นเมตร และคำนวณ BMI
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        
        # กำหนดสีและข้อความตามเกณฑ์
        if bmi < 18.5:
            result = "ต่ำกว่าเกณฑ์ (ผอม)"
        elif 18.5 <= bmi < 23:
            result = "ปกติ สมส่วน"
        elif 23 <= bmi < 25:
            result = "น้ำหนักเกิน"
        elif 25 <= bmi < 30:
            result = "อ้วนระดับ 1"
        else:
            result = "อ้วนระดับ 2 (อันตราย)"

        # แสดงผลลัพธ์
        bmi_value_label.config(text=f"{bmi:.2f}")
        result_text_label.config(text=result)
        
    except ValueError:
        bmi_value_label.config(text="0.00")
        result_text_label.config(text="กรุณาใส่ตัวเลขที่ถูกต้อง")

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    bmi_value_label.config(text="0.00")
    result_text_label.config(text="รอผลคำนวณ ")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("BMI Calculator Pro")
root.geometry("350x450")
root.configure()

# ส่วนหัว
header = tk.Label(root, text="เครื่องคำนวณ BMI", font=("Arial", 18, "bold"))
header.pack(pady=20)

# ช่องกรอกน้ำหนัก
tk.Label(root, text="น้ำหนัก (กิโลกรัม)", font=("Arial", 10)).pack()
weight_entry = tk.Entry(root, font=("Arial", 14), justify='center')
weight_entry.pack(pady=5)

# ช่องกรอกส่วนสูง
tk.Label(root, text="ส่วนสูง (เซนติเมตร)", font=("Arial", 10)).pack()
height_entry = tk.Entry(root, font=("Arial", 14), justify='center')
height_entry.pack(pady=5)

# ปุ่มกด
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

calc_btn = tk.Button(btn_frame, text="คำนวณ",bg="#2ecc71", command=calculate_bmi, fg="white", width=10, font=("Arial", 10, "bold"))
calc_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(btn_frame, text="ล้างข้อมูล", bg="#95a5a6", command=clear_fields, fg="white", width=10, font=("Arial", 10, "bold"))
clear_btn.grid(row=0, column=1, padx=5)

# ส่วนแสดงผล
tk.Label(root, text="ค่า BMI ของคุณคือ:", font=("Arial", 10)).pack()
bmi_value_label = tk.Label(root, text="0.00", font=("Arial", 30, "bold"))
bmi_value_label.pack()

result_text_label = tk.Label(root, text="รอผลคำนวณ", font=("Arial", 14))
result_text_label.pack(pady=5)

root.mainloop()
