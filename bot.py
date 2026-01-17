import time
import requests
from datetime import datetime

TOKEN = "8329803682:AAEDqmNKn2h2NDZT59OJulFYG1mD05xA7P8"
CHAT_ID = "7529392560"

def enviar(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": texto
    })

enviar("🚀 Bot iniciado correctamente")

while True:
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    enviar(f"📊 Reporte diario\n⏰ {ahora}")
    time.sleep(86400)  # 24 horas

