from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    d = None
    if request.method == 'POST':
        try:
            vists = int(request.form.get('v', 0))
            plat = request.form.get('p', 'yt')
            # CPM Promedio 2026: YT ($4.5), FB ($1.2), TT ($0.05)
            cpm = 4.5 if plat == 'yt' else (1.2 if plat == 'fb' else 0.05)
            ganancia = (vists / 1000) * cpm
            d = {
                "v": vists,
                "p": plat.upper(),
                "money": round(ganancia, 2),
                "brands": round(ganancia * 8, 2),
                "cpm": cpm
            }
        except: d = "error"

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VELOX ANALYTICS</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            :root { --accent: #00ff7f; --bg: #050505; }
            body { background: var(--bg); color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 15px; }
            .main { max-width: 600px; margin: auto; }
            .card { background: #111; border: 1px solid #222; padding: 20px; border-radius: 15px; margin-top: 15px; }
            input, select { width: 100%; padding: 12px; margin: 8px 0; background: #000; border: 1px solid #333; color: var(--accent); border-radius: 8px; box-sizing: border-box; }
            button { width: 100%; padding: 15px; background: var(--accent); color: #000; border: none; font-weight: 900; border-radius: 8px; cursor: pointer; text-transform: uppercase; margin-top: 10px; }
            .stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px; }
            .stat { background: #1a1a1a; padding: 15px; border-radius: 10px; border-bottom: 3px solid var(--accent); }
            .chart-container { margin-top: 20px; height: 250px; }
        </style>
    </head>
    <body>
        <div class="main">
            <h1 style="letter-spacing:8px; text-align:center; margin:0;">VELOX<span style="color:var(--accent)">PRO</span></h1>
            <p style="text-align:center; color:#555; font-size:0.7rem;">SISTEMA DE AUDITORÍA DE INGRESOS</p>

            <div class="card">
                <form method="POST">
                    <input type="text" placeholder="Pega el link del video (Opcional)" name="url">
                    <select name="p">
                        <option value="yt">YOUTUBE (CPM Alto)</option>
                        <option value="fb">FACEBOOK (CPM Medio)</option>
                        <option value="tt">TIKTOK (CPM Bajo)</option>
                    </select>
                    <input type="number" name="v" placeholder="Número de visitas" required>
                    <button type="submit">ANALIZAR IMPACTO</button>
                </form>

                {% if d and d != "error" %}
                <div class="stat-grid">
                    <div class="stat">
                        <small style="color:#666;">INGRESOS ESTIMADOS</small><br>
                        <span style="font-size:1.2rem; font-weight:bold;">${{ d.money }} USD</span>
                    </div>
                    <div class="stat" style="border-color: #00d4ff;">
                        <small style="color:#666;">VALOR COMERCIAL</small><br>
                        <span style="font-size:1.2rem; font-weight:bold; color:#00d4ff;">${{ d.brands }} USD</span>
                    </div>
                </div>

                <div class="chart-container"><canvas id="myChart"></canvas></div>

                <script>
                    const ctx = document.getElementById('myChart').getContext('2d');
                    new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: ['AdSense', 'Marcas', 'Afiliados'],
                            datasets: [{
                                label: 'Proyección de Ganancias ($)',
                                data: [{{ d.money }}, {{ d.brands }}, {{ d.money * 0.5 }}],
                                backgroundColor: ['#00ff7f', '#00d4ff', '#ff0055']
                            }]
                        },
                        options: { maintainAspectRatio: false, scales: { y: { beginAtZero: true, grid: { color: '#222' } } } }
                    });
                </script>
                {% endif %}
            </div>

            <div style="margin-top:30px; border:1px dashed #333; padding:15px; border-radius:10px;">
                <p style="font-size:10px; color:#444; text-align:center;">ADSTERRA PREMIUM ADS</p>
                <script async="async" data-cfasync="false" src="
