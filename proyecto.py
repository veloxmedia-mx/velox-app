from flask import Flask, request, render_template_string
import yt_dlp

app = Flask(__name__)

HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - Descarga TikTok</title>
    <style>
        body { background-color: #000; color: #fff; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }
        .container { text-align: center; border: 3px solid #00ff00; padding: 30px; box-shadow: 0 0 20px #00ff00; background: #000; max-width: 90%; width: 400px; }
        h1 { font-size: 3rem; text-shadow: 3px 3px #ff00ff; letter-spacing: 5px; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin-bottom: 20px; background: #222; border: 1px solid #ff00ff; color: #00ff00; box-sizing: border-box; }
        button { background: #ff00ff; color: #fff; border: none; padding: 15px; font-size: 1.2rem; cursor: pointer; width: 100%; font-weight: bold; box-shadow: 5px 5px #00ff00; }
        .result { margin-top: 30px; border-top: 2px dashed #00ff00; padding-top: 20px; }
        .download-btn { background: #00ff00; color: #000; text-decoration: none; padding: 15px 25px; display: inline-block; font-weight: bold; margin-bottom: 20px; border-radius: 5px; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
        .ad-container { margin-top: 20px; background: #111; padding: 10px; border: 1px solid #333; }
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
            {% if video_url == "error" %}
                <p style="color: red;">Error: No pudimos obtener el video. Intenta con otro link.</p>
            {% else %}
                <p style="color: #ff00ff;">¡VIDEO LISTO!</p>
                <video width="100%" controls style="margin-bottom: 10px; border: 1px solid #ff00ff;">
                    <source src="{{ video_url }}" type="video/mp4">
                    Tu navegador no soporta el video.
                </video>
                <br>
                <a href="{{ video_url }}" class="download-btn" download="video_velox.mp4" target="_blank" rel="noreferrer">CLIC DERECHO / MANTÉN PARA GUARDAR</a>
                
                <div class="ad-container">
                    <p style="font-size: 10px; color: #666;">PUBLICIDAD RECOMENDADA</p>
                    <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
                    <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
                </div>
            {% endif %}
        </div>
        {% endif %}
    </div>
    <p style="margin-top: 20px; color: #444;">VELOX MEDIA MX &copy; 2026</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    video_url = None
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            # Forzamos a buscar la versión sin marca de agua si es posible
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'quiet': True,
                'no_warnings': True,
                'outtmpl': '-',
                'nocheckcertificate': True,
                'headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                    'Accept': 'video/webm,video/any,video/*;q=0.9,application/json;q=0.7',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Referer': 'https://www.tiktok.com/',
                }
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # Intentamos obtener la URL directa del video
                video_url = info.get('url')
        except:
            video_url = "error"
    return render_template_string(HTML_LAYOUT, video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
