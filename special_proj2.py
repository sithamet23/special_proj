'''
จงเขียนโปรแกรมแปลงหน่วยน้ำหนักด้วย Python และ Tkinter

คำอธิบาย : 

1. สร้าง GUI สำหรับรับค่าน้ำหนักหน่วย Kilogram (Kg) จากผู้ใช้

2. โปรแกรมต้องมีองค์ประกอบดังนี้:

Label แสดงข้อความ "Enter weight in Kg"
Entry สำหรับรับค่าน้ำหนัก
Button ชื่อ "Convert" -> แปลงค่า
Button ชื่อ "Clear" -> เคลียร์ค่า

3. เมื่อผู้ใช้กดปุ่ม Convertให้โปรแกรมแปลงค่า Kg เป็น:

Gram
Pound
Ounce

ซึ่งหาได้จากความสัมพันธ์

Pound = Kg * 2.2
Ounce = Kg * 35.27
Gram = Kg * 1000

4. แสดงผลลัพธ์ในช่อง output จำนวน 3 ช่อง คือ Gram, Pound, Ounce

5. สามารถแปลงค่าและใช้งานได้จริง

'''

# เขียนโค้ดที่นี่...


import tkinter as tk

# สร้างหน้าต่างหลัก
Converter = tk.Tk()
Converter.title("Weight Converter (แปลงหน่วยน้ำหนัก)")
Converter.geometry("400x300")

# สร้างป้ายและช่องกรอกข้อมูล
weight_label = tk.Label(Converter, text="ใส่น้ำหนัก (Kg)", font=("Arial", 14))
weight_label.pack(pady=10)
weight_entry = tk.Entry(Converter, font=("Arial", 14), width=20)
weight_entry.pack(pady=5)

# ฟังก์ชันแปลงค่า
def convert_weight():
    try:
        kg = float(weight_entry.get())
        pound = kg * 2.2
        ounce = kg * 35.27
        gram = kg * 1000

        pound_label.config(text=f"Pound: {pound:.2f}")
        ounce_label.config(text=f"Ounce: {ounce:.2f}")
        gram_label.config(text=f"Gram: {gram:.2f}")
    except ValueError:
        pound_label.config(text="Pound: Error")
        ounce_label.config(text="Ounce: Error")
        gram_label.config(text="Gram: Error")

# ฟังก์ชันเคลียร์ค่า
def clear_fields():
    weight_entry.delete(0, tk.END)
    pound_label.config(text="Pound: ")
    ounce_label.config(text="Ounce: ")
    gram_label.config(text="Gram: ")

# ปุ่มแปลงค่าและเคลียร์
convert_button = tk.Button(Converter, text="แปลงค่า", font=("Arial", 12), command=convert_weight)
clear_button = tk.Button(Converter, text="เคลียร์", font=("Arial", 12), command=clear_fields)
convert_button.pack(pady=10)
clear_button.pack(pady=5)

# กรอบแสดงผลลัพธ์
result_frame = tk.Frame(Converter)
result_frame.pack(pady=20)

pound_label = tk.Label(result_frame, text="Pound: ", font=("Arial", 12))
pound_label.grid(row=0, column=0, padx=10)

ounce_label = tk.Label(result_frame, text="Ounce: ", font=("Arial", 12))
ounce_label.grid(row=1, column=0, padx=10)

gram_label = tk.Label(result_frame, text="Gram: ", font=("Arial", 12))
gram_label.grid(row=2, column=0, padx=10)

# ใช้งานโปรแกรม
Converter.mainloop()