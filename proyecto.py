from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX | AUDITORIA PRO</title>
    <style>
        body { background:#000; color:#0f0; font-family:'Courier New', monospace; margin:0; padding:15px; text-align:center; }
        .terminal { max-width:450px; margin:50px auto; border:1px solid #0f0; padding:30px; box-shadow:0 0 15px #0f04; background:#050505; border-radius:10px; }
        h1 { font-size:2rem; letter-spacing:8px; margin-bottom:5px; text-shadow:0 0 10px #0f0; }
        .tag { font-size:0.6rem; color:#555; margin-bottom:30px; letter-spacing:3px; }
        input, select { width:100%; padding:15px; margin:10px 0; background:#000; border:1px solid #0f0; color:#0f0; font-family:monospace; font-size:1.1rem; box-sizing:border-box; }
        button { width:100%; padding:18px; background:#0f0; color:#000; border:none; font-weight:bold; cursor:pointer; font-size:1rem; margin-top:10px; transition:0.3s; }
        button:hover { background:#fff; box-shadow:0 0 20px #fff; }
        #res { display:none; margin-top:25px; text-align:left; border-top:1px dashed #0f0; padding-top:20px; }
        .money-box { background:#0f0; color:#000; padding:15px; font-size:1.8rem; font-weight:900; text-align:center; margin-top:10px; }
        .ad-space { margin-top:40px; border:1px solid #222; padding:15px; background:#080808; }
    </style>
</head>
<body>
    <div class="terminal">
        <h1>VELOX</h1>
        <div class="tag">REVENUE AUDIT SYSTEM v6.0</div>
        
        <input type="text" id="link" placeholder="INSERTE LINK DEL VIDEO">
        <select id="plataforma">
            <option value="4.5">YOUTUBE (CPM ALTO)</option>
            <option value="1.2">FACEBOOK (CPM MEDIO)</option>
            <option value="0.05">TIKTOK (CPM BAJO)</option>
        </select>
        <input type="number" id="vistas" placeholder="CANTIDAD DE VISTAS">
        
        <button onclick="ejecutar()">INICIAR ESCANEO</button>

        <div id="res">
            <div style="font-size:0.7rem; color:#0f0; margin-bottom:10px;">> ESCANEO EXITOSO...</div>
            <strong>ADSENSE EST:</strong> <span id="pago" style="color:#fff;"></span> USD<br>
            <strong>SPONSORS EST:</strong> <span id="marcas" style="color:#fff;"></span> USD<br><br>
            <div style="font-size:0.7rem; color:#0f0;">> POTENCIAL TOTAL DE GANANCIA:</div>
            <div class="money-box" id="total"></div>
        </div>
    </div>

    <div class="ad-space">
        <p style="font-size:10px; color:#444; margin-bottom:15px;">ANUNCIO PATROCINADO</p>
        <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
        <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
    </div>

    <script>
        function ejecutar() {
            let v = document.getElementById('vistas').value;
            let cpm = document.getElementById('plataforma').value;
            if(!v || v <= 0) { alert("ERROR: INGRESE VISTAS VALIDAS"); return; }

            let ads = (v / 1000) * cpm;
            let m = ads * 12; // Estimado de marcas pro

            document.getElementById('pago').innerText = ads.toLocaleString('en-US', {minimumFractionDigits: 2});
            document.getElementById('marcas').innerText = m.toLocaleString('en-US', {minimumFractionDigits: 2});
            document.getElementById('total').innerText = "$" + (ads + m).toLocaleString('en-US', {minimumFractionDigits: 2}) + " USD";
            document.getElementById('res').style.display = 'block';
        }
    </script>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
