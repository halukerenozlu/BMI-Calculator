# 🏋️ BMI Calculator with History

Developed using Python, **CustomTkinter**, and **SQLite**; it is an advanced BMI application with a modern interface that stores historical records in a database.

## 🌟 Features

* **💾 Database Integration:** All calculations are automatically saved to a local `SQLite` database.
* **📜 History List:** The last 5 calculations (Date | BMI | Status) are displayed in a scrollable list within the application.
* **🧠 Smart Input:** Enter height in either cm (180) or meters (1.80); the app automatically detects and corrects it.
* **🎨 Color Feedback:** Dynamic color change based on the result (Green: Normal, Yellow: Underweight/Overweight, Red: Obese).
* **⚠️ Error Checking:** Prevents illogical height/weight entries.

## 📂 File Structure

The project is organized according to the **“Separation of Concerns”** principle:

* **`main.py`**: Application interface (Frontend) and user interactions.
* **`database.py`**: Database connection, record insertion, and data retrieval operations (Backend).
* **`bmi_history.db`**: Database file automatically created when the application is run for the first time.

## 🚀 Installation and Execution

1.  Install the required library (SQLite comes embedded with Python, no installation required):
    ```bash
    pip install customtkinter
    ```

2.  Run the application:
    ```bash
    python main.py
    ```

## 📷 Usage

1.  Enter your height and weight.
2.  Press the **Calculate** button.
3.  Your result is calculated instantly and added to the **“Last 5 Records”** list below.
4.  Your data won't be lost even if you close and reopen the application!
