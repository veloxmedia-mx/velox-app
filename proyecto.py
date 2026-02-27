from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    reporte = None
    if request.method == 'POST':
        try:
            url = request.form.get('url', '')
            vistas = int(request.form.get('v', 0))
            region = request.form.get('region', 'latam')
            plat = request.form.get('p', 'yt')

            # --- LÓGICA DE AUDITORÍA AVANZADA ---
            # CPM base por región
            cpm_map = {
                'usa': {'yt': 12.50, 'fb': 3.20, 'tt': 0.80},
                'eur': {'yt': 8.20, 'fb': 2.10, 'tt': 0.50},
                'latam': {'yt': 2.10, 'fb': 0.80, 'tt': 0.05}
            }
            
            cpm_aplicado = cpm_map[region][plat]
            ingresos_ads = (vistas / 1000) * cpm_aplicado
            
            # Simulación de retención y calidad
            retencion = random.randint(35, 75)
            calidad_audiencia = "ALTA" if region != 'latam' else "MEDIA"
            
            reporte = {
                "url": url if url else "MANUAL_ENTRY",
                "plataforma": plat.upper(),
                "vistas": f"{vistas:,}",
                "region": region.upper(),
                "cpm": cpm_aplicado,
                "ingresos_ads": round(ingresos_ads, 2),
                "marcas": round(ingresos_ads * 15, 2),
                "total": round(ingresos_ads + (ingresos_ads * 15), 2),
                "retencion": retencion,
                "calidad": calidad_audiencia
            }
        except: reporte = "error"

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VELOX | Intelligence System</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            :root { --neon: #00ff7f; --dark: #020202; --panel: #0a0a0a; }
            body { background: var(--dark); color: #e0e0e0; font-family: 'Courier New', monospace; margin: 0; padding: 10px; }
            .terminal { max-width: 700px; margin: auto; border: 1px solid #1a1a1a; background: var(--panel); border-radius: 10px; overflow: hidden; box-shadow: 0 0 30px rgba(0,255,127,0.1); }
            .header { background: #111; padding: 15px; border-bottom: 1px solid #222; text-align: center; }
            .content { padding: 20px; }
            input, select { width: 100%; padding: 12px; margin: 5px 0 15px 0; background: #000; border: 1px solid #333; color: var(--neon); font-size: 0.9rem; border-radius: 5px; box-sizing: border-box; }
            button { width: 100%; padding: 15px; background: var(--neon); color: #000; border: none; font-weight: bold; cursor: pointer; letter-spacing: 2px; }
            
            .report-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 25px; }
            .data-card { border: 1px solid #222; padding: 15px; border-radius: 5px; position: relative; }
            .data-card label { font-size: 0.6rem; color: #555; text-transform: uppercase; display: block; }
            .data-card span { font-size: 1.2rem; font-weight: bold; color: var(--neon); }
            
            .progress-bar { height: 5px; background: #111; margin-top: 10px; border-radius: 10px; overflow: hidden; }
            .progress-fill { height: 100%; background: var(--neon); transition: 1s; }
            
            .ad-zone { margin-top: 30px; background: #000; border: 1px dashed #333; padding: 15px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="terminal">
            <div class="header">
                <h1 style="margin:0; font-size:1.5rem; letter-spacing:10px;">VELOX <span style="color:var(--neon)">AI</span></h1>
                <small style="color:#444;">OS v4.0 - DATA SCRAPER & REVENUE AUDIT</small>
            </div>
            
            <div class="content">
                <form method="POST">
                    <label style="font-size:0.7rem;">LINK DEL VIDEO / CANAL:</label>
                    <input type="text" name="url" placeholder="https://www.youtube.com/watch?v=...">
                    
                    <div style="display:flex; gap:10px;">
                        <select name="p">
                            <option value="yt">YOUTUBE</option>
                            <option value="fb">FACEBOOK</option>
                            <option value="tt">TIKTOK</option>
                        </select>
                        <select name="region">
                            <option value="latam">LATAM (CPM Bajo)</option>
                            <option value="usa">USA (CPM Premium)</option>
                            <option value="eur">EUROPA (CPM Alto)</option>
                        </select>
                    </div>

                    <label style="font-size:0.7rem;">VISTAS TOTALES:</label>
                    <input type="number" name="v" placeholder="Ej: 500000" required>
                    <button type="submit">INICIAR ESCANEO ESTRUCTURAL</button>
                </form>

                {% if reporte and reporte != "error" %}
                <div id="results">
                    <div class="report-grid">
                        <div class="data-card">
                            <label>Ingresos AdSense</label>
                            <span>${{ reporte.ingresos_ads }} USD</span>
                        </div>
                        <div class="data-card">
                            <label>Sponsorships (Marcas)</label>
                            <span>${{ reporte.marcas }} USD</span>
                        </div>
                        <div class="data-card">
                            <label>CPM Aplicado</label>
                            <span>${{ reporte.cpm }}</span>
                        </div>
                        <div class="data-card">
                            <label>Calidad Audiencia</label>
                            <span>{{ reporte.calidad }}</span>
                        </div>
                    </div>

                    <div style="margin-top:20px;">
                        <label style="font-size:0.7rem;">RETENCIÓN ESTIMADA: {{ reporte.retencion }}%</label>
                        <div class="progress-bar"><div class="progress-fill" style="width: {{ reporte.retencion }}%;"></div></div>
                    </div>

                    <div style="margin-top:25px; background:var(--neon); color:#000; padding:15px; border-radius:5px; text-align:center;">
                        <small>POTENCIAL TOTAL GENERADO</small><br>
                        <span style="font-size:2rem; font-weight:900;">${{ reporte.total }} USD</span>
                    </div>
                </div>
                {% endif %}
            </div>

            <div class="ad-zone">
                <p style="font-size:10px; color:#444; margin-bottom:15px;">PUBLICIDAD DE ALTA CONVERSIÓN</p>
                <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
                <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
            </div>
        </div>
    </body>
    </html>
    ''', reporte=reporte)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
