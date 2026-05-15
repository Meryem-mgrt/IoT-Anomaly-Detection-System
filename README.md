## TECHNOLOGY STACK

### Backend
FastAPI
Uvicorn
SQLAlchemy

### Database
PostgreSQL

### Messaging
Mosquitto MQTT

### ML
scikit-learn

### Dashboard
Streamlit

### Streaming
WebSockets

### Security
JWT
bcrypt
role-based access

### Alerts
Telegram Bot API
SMTP email

### Containers
Docker Compose


## INDUSTRIAL IoT AI SECURITY SYSTEM
ESP32
   ↓ MQTT
Mosquitto
   ↓
Backend MQTT listener
   ↓
DB storage
   ↓
ML model prediction
   ↓
WebSocket broadcast
   ↓
Dashboard live graph
   ↓
Alerts (Telegram + Email)




PFA/
│
├── backend/                     # FASTAPI CORE (Brain)
│   ├── api/
│   │   ├── auth.py             # login/register/JWT
│   │   ├── routes.py           # sensor + history APIs
│   │   ├── websocket.py       # realtime streaming
│   │
│   ├── database/
│   │   ├── models.py          # SQLAlchemy models
│   │   ├── db.py              # PostgreSQL connection
│   │
│   ├── services/
│   │   ├── mqtt_service.py    # MQTT consumer
│   │   ├── alert_service.py   # telegram/email
│   │   ├── ml_client.py       # calls ML service
│   │
│   ├── security/
│   │   ├── jwt.py             # token creation/verify
│   │   ├── password.py        # bcrypt hashing
│   │
│   ├── main.py
│
├── ml_service/                # ISOLATED AI SERVICE
│   ├── model.pkl             # your RandomForest
│   ├── predict.py            # inference API
│   ├── app.py                # FastAPI ML service
│
├── dashboard/                # REACT ONLY (NO STREAMLIT)
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   │   ├── websocket.js
│   │   │   ├── api.js
│   │
│   ├── package.json
│
├── mqtt/
├── docker-compose.yml