"""

Calculator

สร้างเครื่องคิดเลขด้วย Tkinter
ต้องมีปุ่มตัวเลข 0-9 และตัวดำเนินการร (+ - * /)
ต้องมีปุ่ม = และ Clear
แสดงผลลัพธ์ในช่อง input
และเครื่องคิดเลขสามารถใช้งานการคำนวนได้จริง

Bonus :
- เพิ่มปุ่ม %

"""

import tkinter as tk

# หน้าโปรแกรมเครื่องคิดเลข
calculator = tk.Tk()
calculator.title("Calculator (เครื่องคิดเลข)")
calculator.geometry("330x500")

# ฟังก์ชันจัดการตัวเลขและเครื่องหมาย
def button_click(value):
    current = label_num.cget("text")

    if current == "0" or current == "Error":
        label_num.config(text=str(value))
    else:
        label_num.config(text=current + str(value))

# ฟังก์ชันล้างหน้าจอ
def clear_screen():
    label_num.config(text="0")

# ฟังก์ชันคำนวณผลลัพธ์
def calculate():
    try:
        expression = label_num.cget("text")
        expression = expression.replace("%", "/100")
        result = eval(expression)
        label_num.config(text=str(result))
    except:
        label_num.config(text="Error")

# ใช้ Label เป็นหน้าจอหลัก
label_num = tk.Label(
    calculator,
    text="0",
    font=("Arial", 24),
    bg="white",
    width=16,
    height=2,
    anchor="e",
    padx=10
)

label_num.grid(row=0, column=0, columnspan=4, pady=20)

# -------------------------
# สร้างปุ่มตัวเลข

btn_7 = tk.Button(calculator, text="7", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(7))

btn_8 = tk.Button(calculator, text="8", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(8))

btn_9 = tk.Button(calculator, text="9", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(9))

btn_4 = tk.Button(calculator, text="4", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(4))

btn_5 = tk.Button(calculator, text="5", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(5))

btn_6 = tk.Button(calculator, text="6", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(6))

btn_1 = tk.Button(calculator, text="1", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(1))

btn_2 = tk.Button(calculator, text="2", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(2))

btn_3 = tk.Button(calculator, text="3", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(3))

btn_0 = tk.Button(calculator, text="0", font=("Arial", 18),
                  width=5, height=2,
                  command=lambda: button_click(0))

# -------------------------
# ปุ่มเครื่องหมาย

btn_add = tk.Button(calculator, text="+", font=("Arial", 18),
                    width=5, height=2,
                    command=lambda: button_click("+"))

btn_subtract = tk.Button(calculator, text="-", font=("Arial", 18),
                         width=5, height=2,
                         command=lambda: button_click("-"))

btn_multiply = tk.Button(calculator, text="*", font=("Arial", 18),
                         width=5, height=2,
                         command=lambda: button_click("*"))

btn_divide = tk.Button(calculator, text="/", font=("Arial", 18),
                       width=5, height=2,
                       command=lambda: button_click("/"))

# ปุ่ม %
btn_percent = tk.Button(calculator, text="%", font=("Arial", 18),
                        width=5, height=2,
                        command=lambda: button_click("%"))


# ปุ่ม =
btn_equal = tk.Button(calculator, text="=", font=("Arial", 18),
                      width=5, height=2,
                      command=calculate)

# ปุ่ม Clear
btn_clear = tk.Button(calculator, text="C", font=("Arial", 18),
                      width=5, height=2,
                      command=clear_screen)

# -------------------------
# จัดวางปุ่ม

btn_clear.grid(row=1, column=0)
btn_percent.grid(row=1, column=1)
btn_divide.grid(row=1, column=2)
btn_multiply.grid(row=1, column=3)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_subtract.grid(row=2, column=3)

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_add.grid(row=3, column=3)

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_0.grid(row=4, column=3)

btn_equal.grid(row=5, column=0, columnspan=4, sticky="nsew")



# ใช้งานโปรแกรม
calculator.mainloop()