from flask import Flask, render_template, request, send_file, after_this_request
import yt_dlp
import os
import glob
from datetime import datetime

app = Flask(__name__)

# --- FUNCIÓN PARA LIMPIAR BASURA ANTIGUA ---
def limpiar_archivos_viejos():
    # Busca cualquier archivo que empiece con VELOX_ y lo borra
    for f in glob.glob("VELOX_*.mp4"):
        try:
            os.remove(f)
        except:
            pass

# --- INTERFAZ VELOX GRAFFITI STYLE ---
HTML_DESIGN = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - High Fidelity Media</title>
    <style>
        body {
            margin: 0; padding: 0;
            background-color: #000;
            background-image: 
                linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)),
                url('https://img.freepik.com/free-vector/colorful-graffiti-background_23-2148283416.jpg');
            background-size: cover; background-position: center;
            color: white; font-family: 'Segoe UI', sans-serif;
            display: flex; justify-content: center; align-items: center;
            height: 100vh; overflow: hidden;
        }
        .container {
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(8px);
            padding: 40px; border-radius: 20px;
            border: 1px solid #00ff96;
            text-align: center; width: 90%; max-width: 400px;
            box-shadow: 0 0 40px rgba(0, 255, 150, 0.3);
        }
        h1 { 
            font-size: 3.5rem; letter-spacing: 12px; margin: 0; font-weight: 200; 
            text-shadow: 0 0 15px #00ff96;
        }
        .subtitle { 
            font-size: 0.8rem; color: #00ff96; letter-spacing: 4px; margin-bottom: 35px; 
            text-transform: uppercase;
        }
        input[type="text"] {
            width: 100%; padding: 15px; background: rgba(255, 255, 255, 0.05);
            border: 1px solid #333; border-radius: 8px; color: white;
            text-align: center; margin-bottom: 20px; outline: none;
        }
        button {
            width: 100%; padding: 16px; background: #fff; color: #000;
            border: none; border-radius: 8px; font-weight: bold;
            letter-spacing: 2px; cursor: pointer; transition: 0.3s;
        }
        button:hover { background: #00ff96; box-shadow: 0 0 20px #00ff96; }
        
        .loading { display: none; margin-top: 20px; }
        .bar { height: 4px; width: 100%; background: #222; border-radius: 2px; overflow: hidden; }
        .fill { width: 100%; height: 100%; background: #00ff96; animation: move 2s infinite; }
        @keyframes move { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); } }
        
        #success-msg { display: none; color: #00ff96; font-weight: bold; margin-top: 20px; text-shadow: 0 0 5px #00ff96; }
        .footer { margin-top: 40px; font-size: 0.6rem; color: #666; letter-spacing: 2px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>VELOX</h1>
        <div class="subtitle">High Fidelity Media</div>
        
        <form action="/descargar" method="post" id="dlForm">
            <input type="text" name="url" id="urlIn" placeholder="PEGAR ENLACE AQUÍ" required>
            <button type="submit" id="btn-go">OBTENER VIDEO</button>
        </form>

        <div class="loading" id="loader">
            <div class="bar"><div class="fill"></div></div>
            <p style="color:#00ff96; font-size:0.8rem; margin-top:10px;">PROCESANDO VIDEO...</p>
        </div>

        <div id="success-msg">✅ ¡DESCARGA LISTA!</div>
        <div class="footer">CIFRADO DE EXTREMO A EXTREMO</div>
    </div>

    <script>
        document.getElementById('dlForm').onsubmit = function() {
            document.getElementById('btn-go').style.display = 'none';
            document.getElementById('loader').style.display = 'block';
            
            setTimeout(() => {
                document.getElementById('loader').style.display = 'none';
                document.getElementById('success-msg').style.display = 'block';
                setTimeout(() => {
                    document.getElementById('success-msg').style.display = 'none';
                    document.getElementById('btn-go').style.display = 'block';
                    document.getElementById('urlIn').value = '';
                }, 3000);
            }, 9000);
        };
    </script>
</body>
</html>
'''

@app.route('/')
def inicio():
    limpiar_archivos_viejos() # Limpia la PC cada vez que alguien entra
    return HTML_DESIGN

@app.route('/descargar', methods=['POST'])
def descargar():
    video_url = request.form['url']
    nombre = f'VELOX_{datetime.now().strftime("%H%M%S")}.mp4'

    @after_this_request
    def auto_delete(response):
        try: os.remove(nombre)
        except: pass
        return response

    ydl_opts = {'outtmpl': nombre, 'format': 'best', 'quiet': True}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return send_file(nombre, as_attachment=True)
    except:
        return '<script>alert("Link no válido"); window.location.href="/";</script>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))