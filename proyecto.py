from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    datos = None
    if request.method == 'POST':
        try:
            v = int(request.form.get('v', 0))
            # Cálculo directo: $0.05 por cada 1k vistas
            pago_directo = (v / 1000) * 0.05
            datos = {
                "vistas": f"{v:,}",
                "pago": round(pago_directo, 2),
                "marcas": round(pago_directo * 12, 2)
            }
        except:
            datos = "error"

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VELOX MONEY</title>
        <style>
            body { background:#000; color:#fff; font-family:sans-serif; text-align:center; padding:10px; }
            .card { background:#111; border:2px solid #00ff7f; padding:25px; border-radius:15px; max-width:380px; margin:20px auto; }
            input { width:100%; padding:15px; background:#000; border:1px solid #333; color:#00ff7f; font-size:1.5rem; border-radius:10px; margin-bottom:10px; box-sizing:border-box; }
            button { width:100%; padding:15px; background:#00ff7f; color:#000; border:none; font-weight:bold; border-radius:10px; cursor:pointer; font-size:1.1rem; }
            .res { margin-top:20px; background:#1a1a1a; padding:15px; border-radius:10px; text-align:left; border-left:4px solid #00ff7f; }
            .ad { margin-top:30px; min-height:250px; background:#050505; border:1px dashed #444; padding:10px; }
        </style>
    </head>
    <body>
        <h1 style="letter-spacing:5px; margin-bottom:0;">VELOX <span style="color:#00ff7f;">$</span></h1>
        <p style="font-size:0.8rem; color:#666;">CALCULADORA DE INGRESOS REALES</p>

        <div class="card">
            <form method="POST">
                <input type="number" name="v" placeholder="Vistas del video" required>
                <button type="submit">CALCULAR GANANCIA</button>
            </form>

            {% if datos and datos != "error" %}
            <div class="res">
                <small style="color:#888;">PARA {{ datos.vistas }} VISTAS:</small><br>
                <p><strong>PAGO TIKTOK:</strong> <span style="color:#00ff7f;">${{ datos.pago }} USD</span></p>
                <p><strong>CON MARCAS:</strong> <span style="color:#00ff7f;">${{ datos.marcas }} USD</span></p>
            </div>
            {% endif %}
        </div>

        <div class="ad">
            <p style="font-size:10px; color:#444;">PUBLICIDAD (GANA DINERO AQUÍ)</p>
            <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
            <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
        </div>
    </body>
    </html>
    ''', datos=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
