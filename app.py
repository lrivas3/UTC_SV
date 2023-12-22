from flask import Flask
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/')
def hello_world():
    hora_utc = datetime.now(timezone.utc)

    # El Salvador
    huso_horario_el_salvador = timezone(timedelta(hours=-6))
    hora_el_salvador = hora_utc.astimezone(huso_horario_el_salvador)

    hora_sv_formateada = hora_el_salvador.strftime('%Y-%m-%d %H:%M:%S')

    # UTC
    hora_utc_formateada = hora_utc.strftime('%Y-%m-%d %H:%M:%S')

    return {'hora_el_salvador': hora_sv_formateada, 'hora_utc': hora_utc_formateada}

if __name__ == '__main__':
    app.run(debug=True)
