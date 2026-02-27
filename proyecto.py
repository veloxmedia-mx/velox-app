from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    datos = None
    if request.method == 'POST':
        try:
            vistas = int(request.form.get('vistas', 0))
            pais = request.form.get('pais', 'latam')
            # Factor de pago según región
            multiplicador = 1.0 if pais == 'latam' else 4.5
            
            ganancia_min = (vistas * 0.02 / 1000) * multiplicador
            ganancia_max = (vistas * 0.05 / 1000) * multiplicador
            
            datos = {
                "vistas": f"{vistas:,}",
                "min": round(ganancia_min, 2),
                "max": round(ganancia_max, 2),
                "marca": round(ganancia_min * 8, 2),
                "pais": "Estados Unidos / Europa" if pais == 'usa' else "Latinoamérica"
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
            :root { --money: #00ff7f; --bg: #050505; }
            body { background: var(--bg); color: #fff; font-family: 'Inter', sans-serif; margin: 0; padding: 20px; text-align: center; }
            .container { max-width: 450px; margin: auto; }
            .calc-card { background: #111; padding: 30px; border-radius: 25px; border: 1px solid #222; margin-top: 20px; }
            input, select { width: 100%; padding: 15px; background: #000; border: 1px solid #333; border-radius: 12px; color: var(--money); font-size: 1.2rem; text-align: center; margin-bottom: 15px; box-sizing: border-box; }
            button { width: 100%; padding: 18px; background: var(--money); color: #000; border: none; border-radius: 12px; font-weight: 900; cursor: pointer; text-transform: uppercase; }
            .res-card { background: #1a1a1a; padding: 20px; border-radius: 15px; margin-top: 15px; border-left: 4px solid var(--money); text-align: left; }
            .ad-box { margin-top: 40px; border: 1px dashed #333; padding: 15px; border-radius: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 style="letter-spacing:10px;">VELOX<span style="color:var(--money);">$</span></h1>
            <p style="font-size:0.7rem; color:#555; letter-spacing:3px;">CALCULADORA DE INGRESOS PRO</p>

            <div class="calc-card">
                <form method="POST">
                    <input type="number" name="vistas" placeholder="Número de vistas" required>
                    <select name="pais">
                        <option value="latam">Audiencia: Latinoamérica</option>
                        <option value="usa">Audiencia: USA / Europa (Paga más)</option>
                    </select>
                    <button type="submit">CALCULAR MI DINERO</button>
                </form>

                {% if datos and datos != "error" %}
                <div class="result">
                    <div class="res-card">
                        <small style="color:#888;">REGIÓN: {{ datos.pais }}</small><br>
                        <strong>PAGO TIKTOK:</strong><br>
                        <span style="font-size:1.5rem;">${{ datos.min }} - ${{ datos.max }} USD</span>
                    </div>
                    <div class="res-card" style="border-left-color:#00d4ff;">
                        <strong>VALOR CON MARCAS:</strong><br>
                        <span style="font-size:1.5rem; color:#00d4ff;">${{ datos.marca }} USD</span>
                    </div>
                </div>
                {% endif %}
            </div>

            <div class="ad-box">
                <p style="font-size:10px; color:#444;">ANUNCIO PATROCINADO</p>
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
