from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX CONVERT | Herramientas Gratuitas</title>
    <style>
        :root { --primary: #007bff; --bg: #f8f9fa; }
        body { font-family: 'Segoe UI', sans-serif; background: var(--bg); margin: 0; padding: 20px; text-align: center; }
        .app-container { max-width: 600px; margin: 40px auto; background: #fff; padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .logo { font-weight: 900; font-size: 1.5rem; color: #333; margin-bottom: 30px; }
        .drop-zone { border: 2px dashed #ccc; padding: 40px; border-radius: 10px; cursor: pointer; transition: 0.3s; background: #fafafa; }
        .drop-zone:hover { border-color: var(--primary); background: #f0f7ff; }
        .btn { display: none; width: 100%; padding: 15px; background: var(--primary); color: #fff; border: none; border-radius: 8px; font-weight: bold; margin-top: 20px; cursor: pointer; }
        #status { margin-top: 20px; font-size: 0.9rem; color: #666; }
        .ad-container { margin-top: 40px; min-height: 250px; border-top: 1px solid #eee; padding-top: 20px; }
    </style>
</head>
<body>

<div class="app-container">
    <div class="logo">VELOX<span style="color:var(--primary)">CONVERT</span></div>
    <h3>Convertir Imagen a PDF</h3>
    <p style="color:#777; font-size:0.9rem;">Rápido, seguro y sin marcas de agua.</p>

    <div class="drop-zone" onclick="document.getElementById('fileInput').click()">
        <p id="fileName">Haz clic o arrastra tu imagen aquí</p>
        <input type="file" id="fileInput" hidden accept="image/*" onchange="updateName()">
    </div>

    <button id="convertBtn" class="btn" onclick="simularConversion()">CONVERTIR A PDF AHORA</button>

    <div id="status"></div>
</div>

<div class="ad-container">
    <p style="font-size:10px; color:#ccc;">ANUNCIO</p>
    <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
    <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
</div>

<script>
    function updateName() {
        const input = document.getElementById('fileInput');
        const name = input.files[0].name;
        document.getElementById('fileName').innerText = "Archivo listo: " + name;
        document.getElementById('convertBtn').style.display = "block";
    }

    function simularConversion() {
        const status = document.getElementById('status');
        const btn = document.getElementById('convertBtn');
        btn.disabled = true;
        btn.innerText = "PROCESANDO...";
        
        let progreso = 0;
        const intervalo = setInterval(() => {
            progreso += 10;
            status.innerText = "Cifrando y convirtiendo: " + progreso + "%";
            if (progreso >= 100) {
                clearInterval(intervalo);
                status.innerHTML = "<b style='color:green;'>¡Conversión Exitosa!</b><br>Tu descarga comenzará en breve.";
                btn.innerText = "DESCARGAR PDF";
                btn.style.background = "#28a745";
                btn.disabled = false;
                // Aquí podrías redirigir a un anuncio "Direct Link" de Adsterra para ganar más
            }
        }, 300);
    }
</script>

</body>
</html>
''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
