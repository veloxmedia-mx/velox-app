from flask import Flask, render_template_string, request
import yt_dlp

app = Flask(__name__)

# DISEÑO PREMIUM + MOTOR ANTIBLOQUEO
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - High Fidelity Media</title>
    <style>
        body { background-color: #050505; color: #ffffff; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; text-align: center; }
        .logo { font-size: 3rem; font-weight: 100; letter-spacing: 10px; margin-bottom: 5px; }
        .subtitle { font-size: 0.7rem; letter-spacing: 4px; color: #00ff7f; margin-bottom: 40px; }
        .input-group { width: 90%; max-width: 400px; }
        input { width: 100%; padding: 15px; background: transparent; border: 1px solid #00ff7f; border-radius: 10px; color: #fff; text-align: center; margin-bottom: 20px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #fff; color: #000; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; letter-spacing: 1px; }
        .btn-download { background: #00ff7f !important; color: #000 !important; padding: 20px; text-decoration: none; display: block; border-radius: 10px; font-weight: bold; margin-top: 25px; box-shadow: 0 0 15px #00ff7f; }
        .ad-container { margin-top: 30px; padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px; }
    </style>
</head>
<body>
    <div class="logo">V E L O X</div>
    <div class="subtitle">HIGH FIDELITY MEDIA</div>

    <div class="input-group">
        <form method="POST">
            <input type="text" name="url" placeholder="Pega el link de TikTok aquí" required>
            <button type="submit">OBTENER VIDEO</button>
        </form>

        {% if video_url %}
            <div id="success-area">
                <p style="color: #00ff7f; margin-top: 20px;">¡VIDEO LOCALIZADO!</p>
                <a href="{{ video_url }}" class="btn-download" target="_blank" rel="noopener noreferrer">¡DESCARGAR AHORA!</a>
                
                <p style="font-size: 0.7rem; color: #888; margin-top: 10px;">TIP: Si se abre el video, dale a los 3 puntitos y 'Descargar' o mantén presionado el botón.</p>

                <div class="ad-container">
                    <p style="font-size: 0.6rem; color: #444;">PUBLICIDAD RECOMENDADA</p>
                    <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
                    <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
                </div>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            # Nueva configuración para saltar el Error 403
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'quiet': True,
                'no_warnings': True,
                # Usamos un User-Agent de móvil para que TikTok suelte el video más fácil
                'user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
                'nocheckcertificate': True,
                'add_header': [
                    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language: en-US,en;q=0.5',
                ]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # Buscamos la URL directa más limpia
                video_url = info.get('url')
        except Exception as e:
            print(f"Error crítico: {e}")
            
    return render_template_string(html_content, video_url=video_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
