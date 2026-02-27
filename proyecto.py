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
        .download-btn { background: #00ff00; color: #000; text-decoration: none; padding: 10px 20px; display: inline-block; font-weight: bold; margin-bottom: 20px; }
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
                <p style="color: red;">Error: TikTok bloqueó la conexión. Intenta de nuevo.</p>
            {% else %}
                <p style="color: #ff00ff;">¡VIDEO LISTO!</p>
                <a href="{{ video_url }}" class="download-btn" target="_blank" referrerpolicy="no-referrer">DESCARGAR AHORA</a>
                
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
            # Aquí está el truco: añadimos un User-Agent real
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'nocheckcertificate': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_url = info.get('url')
        except Exception as e:
            print(f"Error: {e}")
            video_url = "error"
    return render_template_string(HTML_LAYOUT, video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
