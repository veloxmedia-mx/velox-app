import os
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# --- TU DISEÑO CON EL FIX DE DESCARGA ---
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - Descarga TikTok</title>
    <style>
        body { background-color: #000; color: #fff; font-family: 'Courier New', monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; background-image: radial-gradient(circle, #1a1a1a 1px, transparent 1px); background-size: 20px 20px; }
        .container { text-align: center; border: 3px solid #00ff00; padding: 30px; box-shadow: 0 0 20px #00ff00; background: rgba(0,0,0,0.9); width: 350px; }
        h1 { font-size: 2.5rem; text-shadow: 3px 3px #ff00ff; letter-spacing: 5px; }
        input { width: 100%; padding: 12px; margin-bottom: 20px; background: #222; border: 1px solid #ff00ff; color: #00ff00; box-sizing: border-box; }
        button { background: #ff00ff; color: #fff; border: none; padding: 15px; cursor: pointer; width: 100%; font-weight: bold; box-shadow: 4px 4px #00ff00; }
        .result { margin-top: 25px; border-top: 2px dashed #00ff00; padding-top: 15px; }
        .download-btn { background: #00ff00; color: #000; text-decoration: none; padding: 15px; display: block; margin-top: 10px; font-weight: bold; font-size: 1.1rem; border-radius: 5px; }
        .ad-container { margin-top: 20px; padding: 5px; background: #111; border: 1px solid #333; }
    </style>
</head>
<body>
    <div class="container">
        <h1>VELOX</h1>
        <form method="POST">
            <input type="text" name="url" placeholder="PEGA LINK DE TIKTOK AQUÍ" required>
            <button type="submit">OBTENER VIDEO</button>
        </form>

        {% if video_url %}
        <div class="result">
            <p style="color: #ff00ff; font-weight: bold;">¡ESTÁ LISTO!</p>
            
            <a href="{{ video_url }}" class="download-btn" download="video_velox.mp4" target="_blank">
                ¡DESCARGAR AHORA!
            </a>
            <p style="font-size: 0.7rem; color: #888; margin-top: 5px;">(Si no inicia, mantén presionado y dale "Descargar vínculo")</p>

            <div class="ad-container">
                <p style="font-size: 10px; color: #666; margin-bottom: 5px;">PUBLICIDAD RECOMENDADA</p>
                <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
                <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
            </div>
        </div>
        {% endif %}
    </div>
    <p style="margin-top: 20px; font-size: 0.8rem; color: #444;">VELOX MEDIA MX &copy; 2026</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    video_url = None
    if request.method == 'POST':
        import yt_dlp
        url = request.form.get('url')
        try:
            # Esta configuración es más potente para saltar bloqueos
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'quiet': True,
                'no_warnings': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # Buscamos el link directo al archivo
                video_url = info.get('url')
        except Exception as e:
            print(f"Error: {e}")
    
    return render_template_string(html_content, video_url=video_url)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
