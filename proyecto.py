from flask import Flask, render_template_string, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    datos = None
    if request.method == 'POST':
        try:
            vistas = int(request.form.get('vistas', 0))
            # Lógica de cálculo (Estimados reales de RPM)
            ganancia_min = vistas * 0.02 / 1000  # $0.02 por cada 1k vistas
            ganancia_max = vistas * 0.05 / 1000  # $0.05 por cada 1k vistas
            
            datos = {
                "vistas": f"{vistas:,}",
                "min": round(ganancia_min, 2),
                "max": round(ganancia_max, 2),
                "marca": round(ganancia_min * 5, 2) # Estimado por trato con marca
            }
        except:
            datos = "error"

    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VELOX | Money Calc</title>
        <style>
            :root { --money: #00ff7f; --bg: #050505; --card: #111; }
            body { background: var(--bg); color: #fff; font-family: 'Lexend', sans-serif; margin: 0; padding: 20px; text-align: center; }
            .container { max-width: 450px; margin: auto; }
            .logo { font-size: 2.5rem; font-weight: 800; letter-spacing: -1px; margin-top: 40px; }
            .logo span { color: var(--money); }
            .subtitle { font-size: 0.7rem; color: #555; letter-spacing: 3px; margin-bottom: 40px; }
            
            .calc-card { background: var(--card); padding: 30px; border-radius: 25px; border: 1px solid #222; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
            input { width: 100%; padding: 15px; background: #000; border: 1px solid #333; border-radius: 12px; color: var(--money); font-size: 1.5rem; text-align: center; margin-bottom: 15px; box-sizing: border-box; font-weight: bold; }
            button { width: 100%; padding: 18px; background: var(--money); color: #000; border: none; border-radius: 12px; font-weight: 900; cursor: pointer; font-size: 1rem; text-transform: uppercase; }
            
            .result { margin-top: 30px; animation: fadeIn 0.5s; }
            .res-card { background: #1a1a1a; padding: 20px; border-radius: 15px; margin-bottom: 10px; border-left: 4px solid var(--money); text-align: left; }
            .res-label { font-size: 0.7rem; color: #888; text-transform: uppercase; }
            .res-value { font-size: 1.4rem; font-weight: bold; color: #fff; }
            
            .ad-slot { margin-top: 40px; padding: 15px; border: 1px dashed #333; border-radius: 15px; }
            @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="logo">VELOX<span>$</span></h1>
            <p class="subtitle">CALCULADORA DE INGRESOS</p>

            <div class="calc-card">
                <form method="POST">
                    <p style="font-size: 0.8rem; color: #888;">Introduce tus vistas totales:</p>
                    <input type="number" name="vistas" placeholder="0" required>
                    <button type="submit">CALCULAR GANANCIAS</button>
                </form>

                {% if datos and datos != "error" %}
                <div class="result">
                    <div class="res-card">
                        <div class="res-label">Pago Estimado TikTok (Fondo Creadores):</div>
                        <div class="res-value">${{ datos.min }} - ${{ datos.max }} USD</div>
                    </div>
                    <div class="res-card" style="border-left-color: #00d4ff;">
                        <div class="res-label">Valor estimado para Marcas:</div>
                        <div class="res-value" style="color: #00d4ff;">${{ datos.marca }} USD</div>
                    </div>
                    <p style="font-size: 0.6rem; color: #444;">*Cálculo basado en RPM promedio de 2026.</p>
                </div>
                {% endif %}
            </div>

            <div class="ad-slot">
                <p style="font-size: 10px; color: #444; margin-bottom: 10px;">ANUNCIO PATROCINADO</p>
                <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
                <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, datos=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
