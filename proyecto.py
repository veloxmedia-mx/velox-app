import os
import requests
from flask import Flask, render_template_string, request, Response
import yt_dlp

app = Flask(__name__)

# --- DISEÑO ÚNICO: NEÓN MATRIX CON AUTODESCARGA ---
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX | CIFRADO EXTREMO</title>
    <style>
        body { 
            background-color: #050505; color: #00ff41; 
            font-family: 'Courier New', Courier, monospace; 
            display: flex; flex-direction: column; align-items: center; justify-content: center; 
            min-height: 100vh; margin: 0; 
            background-image: radial-gradient(#111 1px, transparent 1px); background-size: 15px 15px;
        }
        .container { 
            text-align: center; border: 2px solid #333; padding: 40px; 
            background: rgba(0,0,0,0.95); width: 360px;
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.1);
        }
        h1 { font-size: 3rem; color: #eee; text-shadow: 0 0 15px #00ff41; margin: 0; letter-spacing: 10px; }
        .tag { font-size: 0.6rem; color: #00ff41; letter-spacing: 3px; margin-bottom: 30px; opacity: 0.7; }
        
        input { 
            width: 100%; padding: 15px; margin-bottom: 20px; 
            background: #000; border: 1px solid #444; color: #00ff41; 
            box-sizing: border-box; outline: none; text-align: center; font-size: 0.9rem;
        }
        
        .btn-action { 
            background: #00ff41; color: #000; border: none; padding: 18px; 
            cursor: pointer; width: 100%; font-weight: bold; font-size: 1rem;
            box-shadow: 0 4px 0 #008822; transition: all 0.2s;
        }
        
        .loading-bar { 
            display: none; width: 100%; height: 10px; background: #111; 
            margin-top: 20px; border: 1px solid #00ff41; overflow: hidden;
        }
        .progress { width: 0%; height: 100%; background: #00ff41; transition: width 0.5s; }

        .ad-box { margin-top: 30px; border-top: 1px solid #111; padding-top: 20px; }
    </style>
    <script>
        function iniciarProceso() {
            document.querySelector('.loading-bar').style.display = 'block';
            let bar = document.querySelector('.progress');
            let width = 0;
            let interval = setInterval(() => {
                if (width >= 100) clearInterval(interval);
                else { width += 5; bar.style.width = width + '%'; }
            }, 100);
        }

        // Si el servidor envía el video, el navegador lo descarga y limpia todo
        window.onload = function() {
            const urlParams = new URLSearchParams(window.location.search);
            if (window.location.pathname === '/download_auto') {
                setTimeout(() => {
                    window.location.href = '/'; // Regresa al inicio limpio
                }, 2000);
            }
        };
    </script>
</head>
<body>
    <div class="container">
        <h1>VELOX</h1>
        <div class="tag">SISTEMA DE EXTRACCIÓN MILITAR</div>
        
        <form action="/process" method="POST" onsubmit="iniciarProceso()">
            <input type="text" name="url" placeholder="PEGAR ENLACE TIKTOK" required>
            <button type="submit" class="btn-action">OBTENER VIDEO</button>
        </form>

        <div class="loading-bar">
            <div class="progress"></div>
            <p style="font-size: 10px; margin-top: 5px;">PROCESANDO CIFRADO...</p>
        </div>

        <div class="ad-box">
            <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
            <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
        </div>
    </div>
    <p style="margin-top: 20px; font-size: 0.5rem; color: #333; letter-spacing: 2px;">VELOX MEDIA MX // SIN RASTROS</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

@app.route('/process', methods=['POST'])
def process():
    url = request.form.get('url')
    try:
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url')
            
        # En lugar de mostrar otro botón, enviamos el archivo de una vez
        r = requests.get(video_url, stream=True)
        return Response(r.iter_content(chunk_size=1024), headers={
            "Content-Type": "video/mp4",
            "Content-Disposition": f"attachment; filename=velox_{info.get('id')}.mp4"
        })
    except:
        return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
