from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX | AUDIT PRO</title>
    <style>
        body { background:#000; color:#0f0; font-family:monospace; margin:0; padding:15px; }
        .terminal { max-width:500px; margin:auto; border:1px solid #0f0; padding:20px; box-shadow:0 0 20px #0f03; }
        .green { color:#0f0; } .gray { color:#555; }
        input, select { width:100%; padding:12px; background:#000; border:1px solid #0f0; color:#0f0; margin:10px 0; box-sizing:border-box; }
        button { width:100%; padding:15px; background:#0f0; color:#000; border:none; font-weight:bold; cursor:pointer; font-family:monospace; }
        .res { display:none; margin-top:20px; border-top:1px dashed #0f0; padding-top:20px; text-align:left; }
        .stat { margin-bottom:10px; font-size:0.9rem; }
        .big-money { font-size:2rem; background:#0f0; color:#000; padding:10px; text-align:center; font-weight:bold; }
    </style>
</head>
<body>
    <div class="terminal">
        <h1 style="text-align:center; letter-spacing:5px;">VELOX_AUDIT_v5</h1>
        <p class="gray">SISTEMA DE ANÁLISIS DE INGRESOS 2026</p>
        
        <label class="green">> INSERTE LINK DEL VIDEO:</label>
        <input type="text" id="url" placeholder="https://youtube.com/...">
        
        <label class="green">> SELECCIONE REGIÓN:</label>
        <select id="region">
            <option value="2.5">LATAM (CPM Promedio)</option>
            <option value="12.0">USA / EUROPA (CPM Alto)</option>
        </select>
        
        <label class="green">> VISTAS REGISTRADAS:</label>
        <input type="number" id="vistas" placeholder="0">
        
        <button onclick="auditar()">EJECUTAR AUDITORÍA</button>

        <div id="resultado" class="res">
            <div class="stat">> ESCANEANDO LINK... <span id="l_url"></span></div>
            <div class="stat">> PAGO PUBLICIDAD: <span id="r_ads"></span> USD</div>
            <div class="stat">> VALOR DE MARCAS: <span id="r_marcas"></span> USD</div>
            <div class="stat">> CALIDAD DE TRÁFICO: <span id="r_cal"></span></div>
            <br>
            <div class="gray">POTENCIAL TOTAL GENERADO:</div>
            <div class="big-money" id="r_total"></div>
        </div>
    </div>

    <div style="margin-top:30px; text-align:center;">
        <p class="gray" style="font-size:10px;">ANUNCIO PATROCINADO - ADSTERRA</p>
        <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
        <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
    </div>

    <script>
        function auditar() {
            let v = document.getElementById('vistas').value;
            let cpm = document.getElementById('region').value;
            let url = document.getElementById('url').value;
            if(!v) return alert("Pon las vistas, fiera.");

            let ads = (v / 1000) * cpm;
            let marcas = ads * 12;
            
            document.getElementById('l_url').innerText = url.substring(0,25) + "...";
            document.getElementById('r_ads').innerText = ads.toFixed(2);
            document.getElementById('r_marcas').innerText = marcas.toFixed(2);
            document.getElementById('r_cal').innerText = cpm > 3 ? "PREMIUM" : "ESTÁNDAR";
            document.getElementById('r_total').innerText = "$" + (ads + marcas).toFixed(2);
            document.getElementById('resultado').style.display = 'block';
        }
    </script>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
