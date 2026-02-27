from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>📊 Calculadora de Ingresos Real</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; background: #fafafa; }
        input, select, button { padding: 12px; margin: 10px 0; width: 100%; border: 1px solid #ddd; border-radius: 6px; }
        button { background: #007bff; color: white; border: none; cursor: pointer; font-weight: bold; }
        button:hover { background: #0056b3; }
        .result { margin-top: 25px; padding: 20px; background: #e3f2fd; border-left: 4px solid #2196f3; border-radius: 6px; }
        .disclaimer { font-size: 0.8rem; color: #666; margin-top: 20px; }
    </style>
</head>
<body>
    <h2>📈 Calculadora de Ingresos Estimados (2026)</h2>
    <p>Basada en datos públicos de YouTube, TikTok e Instagram (CPM promedio)</p>

    <label>Vistas / Reproducciones (ej: 500000)</label>
    <input type="number" id="vistas" placeholder="500000" min="1">

    <label>Plataforma</label>
    <select id="plataforma">
        <option value="youtube">YouTube (CPM: $1.50 - $4.50)</option>
        <option value="tiktok">TikTok (CPM: $0.50 - $2.00)</option>
        <option value="instagram">Instagram (CPM: $2.00 - $6.00)</option>
    </select>

    <label>Región</label>
    <select id="region">
        <option value="1.0">Latam</option>
        <option value="3.0">USA / Europa</option>
    </select>

    <button onclick="calcular()">Calcular Ingresos Estimados</button>

    <div class="result" id="resultado" style="display:none;">
        <h3>💰 Resultado Estimado:</h3>
        <p><strong>Ingresos por publicidad:</strong> <span id="ads">$0.00</span></p>
        <p><strong>Potencial por patrocinios:</strong> <span id="sponsor">$0.00</span></p>
        <p><strong>Total estimado:</strong> <span id="total">$0.00</span></p>
    </div>

    <div class="disclaimer">
        <strong>Nota:</strong> Estos son cálculos estimados basados en CPM promedio. No son ingresos reales. Para datos precisos, usa las herramientas oficiales de cada plataforma.
    </div>

    <script>
        function calcular() {
            const vistas = parseFloat(document.getElementById('vistas').value);
            const plataforma = document.getElementById('plataforma').value;
            const region = parseFloat(document.getElementById('region').value);
            
            if (!vistas || vistas <= 0) {
                alert("Por favor, ingresa un número válido de vistas");
                return;
            }

            let cpmMin, cpmMax;
            switch(plataforma) {
                case 'youtube': cpmMin = 1.5; cpmMax = 4.5; break;
                case 'tiktok': cpmMin = 0.5; cpmMax = 2.0; break;
                case 'instagram': cpmMin = 2.0; cpmMax = 6.0; break;
            }

            const ingresoMin = (vistas / 1000) * cpmMin * region;
            const ingresoMax = (vistas / 1000) * cpmMax * region;
            const sponsorMin = ingresoMin * 0.5;
            const sponsorMax = ingresoMax * 0.5;

            document.getElementById('ads').innerText = `$${ingresoMin.toFixed(2)} - $${ingresoMax.toFixed(2)}`;
            document.getElementById('sponsor').innerText = `$${sponsorMin.toFixed(2)} - $${sponsorMax.toFixed(2)}`;
            document.getElementById('total').innerText = `$${(ingresoMin + sponsorMin).toFixed(2)} - $${(ingresoMax + sponsorMax).toFixed(2)}`;
            document.getElementById('resultado').style.display = 'block';
        }
    </script>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(debug=True)
