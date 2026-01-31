import sqlite3


def init_db():

    conn = sqlite3.connect('bmi_history.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS history
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       bmi
                       REAL,
                       status
                       TEXT,
                       date
                       TIMESTAMP
                       DEFAULT
                       CURRENT_TIMESTAMP
                   )
                   ''')

    conn.commit()
    conn.close()


def add_entry(bmi, status):
    conn = sqlite3.connect('bmi_history.db')
    cursor = conn.cursor()

    # (?, ?) işaretleri güvenlik içindir, değerleri oraya yerleştirir.
    cursor.execute('INSERT INTO history (bmi, status) VALUES (?, ?)', (bmi, status))

    conn.commit()
    conn.close()


def fetch_history():
    conn = sqlite3.connect('bmi_history.db')
    cursor = conn.cursor()

    # Verileri al (Tarihe göre tersten sırala, sadece son 5 tanesini getir)
    cursor.execute('SELECT * FROM history ORDER BY date DESC LIMIT 5')
    data = cursor.fetchall()

    conn.close()
    return data