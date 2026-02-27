from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    datos = None
    if request.method == 'POST':
        try:
            v = int(request.form.get('v', 0))
            plataforma = request.form.get('p', 'tt')
            
            # Lógica de CPM por plataforma (Promedios 2026)
            if plataforma == 'yt':
                cpm = 4.50  # YouTube paga mejor
                label = "YouTube Adsense"
            elif plataforma == 'reels':
                cpm = 0.15
                label = "Meta Bonus"
            else:
                cpm = 0.05
                label = "TikTok Creator Rewards"
            
            ganancia = (v / 1000) * cpm
            datos = {
                "vistas": f"{v:,}",
                "plataforma": label,
                "pago": round(ganancia, 2),
                "marcas": round(ganancia * 10, 2),
                "rpm": cpm
            }
        except:
            datos = "error"

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VELOX | Analytics Spy</title>
        <style>
            body { background:#000; color:#fff; font-family:'Courier New', monospace; padding:15px; }
            .spy-box { background:#0a0a0a; border:1px solid #00ff7f; padding:25px; border-radius:5px; max-width:450px; margin:auto; box-shadow: 0 0 20px rgba(0,255,127,0.1); }
            select, input { width:100%; padding:15px; margin:10px 0; background:#000; border:1px solid #222; color:#00ff7f; font-size:1rem; box-sizing:border-box; }
            button { width:100%; padding:15px; background:#00ff7f; color:#000; border:none; font-weight:bold; cursor:pointer; text-transform:uppercase; }
            .panel { margin-top:20px; border:1px solid #333; padding:15px; text-align:left; background:#111; position:relative; }
            .status { font-size:0.7rem; color:#00ff7f; margin-bottom:10px; border-bottom:1px solid #222; padding-bottom:5px; }
            .val { font-size:1.5rem; font-weight:bold; color:#fff; }
            .ad-area { margin-top:30px; border:1px dashed #444; padding:10px; font-size:0.7rem; }
        </style>
    </head>
    <body>
        <div class="spy-box">
            <h2 style="letter-spacing:5px;">VELOX <span style="color:#00ff7f;">SPY</span></h2>
            <p style="font-size:0.7rem; color:#444;">ANALIZADOR DE INGRESOS MULTIPLATAFORMA</p>
            
            <form method="POST">
                <select name="p">
                    <option value="tt">TIKTOK</option>
                    <option value="yt">YOUTUBE (Largo)</option>
                    <option value="reels">INSTAGRAM REELS</option>
                </select>
                <input type="number" name="v" placeholder="Cantidad de vistas" required>
                <button type="submit">ESPECIALIZAR CÁLCULO</button>
            </form>

            {% if datos and datos != "error" %}
            <div class="panel">
                <div class="status">STATUS: ESCANEO COMPLETADO...</div>
                <small style="color:#666;">PLATAFORMA: {{ datos.plataforma }}</small><br>
                <div class="val">${{ datos.pago }} <small style="font-size:0.8rem;color:#444;">USD (CPM: ${{datos.rpm}})</small></div>
                <br>
                <small style="color:#666;">TRATOS CON MARCAS (ESTIMADO):</small><br>
                <div class="val" style="color:#00ff7f;">${{ datos.marcas }} USD</div>
            </div>
            {% endif %}
        </div>

        <div class="ad-area">
            <p>CONTENIDO PATROCINADO</p>
            <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
            <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
        </div>
    </body>
    </html>
    ''', datos=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
