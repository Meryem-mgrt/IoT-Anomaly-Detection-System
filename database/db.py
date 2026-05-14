import sqlite3

# =========================
# DATABASE CONNECTION
# =========================
conn = sqlite3.connect(
    "iot_data.db",
    check_same_thread=False
)

cursor = conn.cursor()

# =========================
# CREATE TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id TEXT NOT NULL,

    temperature REAL NOT NULL,

    vibration REAL NOT NULL,

    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

# =========================
# SAVE SENSOR DATA
# =========================
def save_data(data):

    try:

        cursor.execute("""
        INSERT INTO sensor_data (
            device_id,
            temperature,
            vibration
        )
        VALUES (?, ?, ?)
        """, (

            data["device_id"],
            data["temperature"],
            data["vibration"]

        ))

        conn.commit()

        print("✅ Data saved to database")

    except Exception as e:

        print("❌ Database Error:", e)

# =========================
# GET ALL DATA
# =========================
def get_data():

    try:

        cursor.execute("""
        SELECT
            id,
            device_id,
            temperature,
            vibration,
            timestamp
        FROM sensor_data
        ORDER BY id DESC
        """)

        return cursor.fetchall()

    except Exception as e:

        print("❌ Fetch Error:", e)

        return []

# =========================
# OPTIONAL: CLEAR DATABASE
# =========================
def clear_data():

    cursor.execute("DELETE FROM sensor_data")

    conn.commit()

    print("🗑️ Database cleared")



    from sqlalchemy import create_engine, Column, Float, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://user:pass@localhost/iot")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Sensor(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True)
    device_id = Column(String)
    temperature = Column(Float)
    vibration = Column(Float)