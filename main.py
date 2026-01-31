import customtkinter
import database


app = customtkinter.CTk()
app.title("BMI Calculator")
app.geometry("300x600")

my_label = customtkinter.CTkLabel(master=app, text="BMI Calculator",)
my_label.configure(text_color="yellow",font=("Arial", 24, "bold"))
my_label.pack(padx=5, pady=15)


#List Update Func
def update_history_ui():
    for widget in history_frame.winfo_children():
        widget.destroy()

    data = database.fetch_history()

    for row in data:
        bmi_val = "{:.2f}".format(row[1])
        status_val = row[2]
        date_val = row[3].split(" ")[0]

        record_text = f"{date_val} | BMI: {bmi_val} | {status_val}"

        record_label = customtkinter.CTkLabel(history_frame, text=record_text, font=("Arial", 12))
        record_label.pack(anchor="w", padx=5, pady=2)

def my_button_clicked():
    try:
        height_input = my_entry_height.get()
        weight_input = my_entry_weight.get()

        user_height = float(height_input)
        user_weight = float(weight_input)

        if user_height > 3:
            user_height = user_height / 100

        if user_height <= 0 or user_height > 2.50:
            result_text = "Height Error!"
            my_result_entry.configure(text_color="red")
            status_label.configure(text="")

        elif user_weight <= 0 or user_weight > 600:
            result_text = "Weight Error!"
            my_result_entry.configure(text_color="red")
            status_label.configure(text="")

        else:
            bmi = user_weight / (user_height * user_height)
            result_text = "{:.2f}".format(bmi)

            if bmi < 18.5:
                status_text = "Thin"
                status_color = "#FFCC00"  # Yellow/Orange
            elif 18.5 <= bmi <= 24.9:
                status_text = "Normal"
                status_color = "#32CD32"  # Lime Green
            elif 25 <= bmi <= 29.9:
                status_text = "Overweight"
                status_color = "#FFCC00"  # Yellow/Orange
            else:
                status_text = "Obese"
                status_color = "#FF4500"  # Orange Red

            my_result_entry.configure(text_color=status_color)
            status_label.configure(text=status_text, text_color=status_color)

            database.add_entry(bmi, status_text)

            update_history_ui()

        my_result_entry.delete(0, "end")
        my_result_entry.insert(0, result_text)

    except ValueError:
        my_result_entry.configure(text_color="red")
        my_result_entry.delete(0, "end")
        my_result_entry.insert(0, "Sayı Giriniz!")
        status_label.configure(text="")


my_entry_weight = customtkinter.CTkEntry(app, placeholder_text="your weight")
my_entry_weight.pack(padx=5, pady=5)

my_entry_height = customtkinter.CTkEntry(app, placeholder_text="your height")
my_entry_height.pack(padx=5, pady=5)

my_button = customtkinter.CTkButton(master=app,text="Calculate", command=my_button_clicked)
my_button.pack(padx=5, pady=10)

result_label = customtkinter.CTkLabel(app, text="Result:", font=("Arial", 16))
result_label.pack(pady=(10, 0))

my_result_entry = customtkinter.CTkEntry(app, font=("Arial", 18, "bold"),text_color="green", fg_color="#333333", justify="center")
my_result_entry.pack(padx=5, pady=5)

status_label = customtkinter.CTkLabel(app, text="", font=("Arial", 16, "bold"))
status_label.pack(pady=10)

# History
history_title = customtkinter.CTkLabel(app, text="Last 5 Record", font=("Arial", 14, "bold"))
history_title.pack(pady=(10, 0))

# Scrollable Frame
history_frame = customtkinter.CTkScrollableFrame(app, width=200, height=100)
history_frame.pack(pady=5)


database.init_db()
app.mainloop()
