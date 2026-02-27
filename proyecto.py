from flask import Flask, render_template_string, request
import yt_dlp

app = Flask(__name__)

# DISEÑO PREMIUM CORREGIDO
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
        .btn-download { background: #00ff7f; color: #000; padding: 15px; text-decoration: none; display: block; border-radius: 10px; font-weight: bold; margin-top: 20px; }
        .ad-container { margin-top: 30px; padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px; width: 100%; }
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
            <a href="{{ video_url }}" class="btn-download" target="_blank">¡DESCARGAR AHORA!</a>
            <p style="font-size: 0.7rem; color: #666; margin-top: 5px;">(Si no inicia, mantén presionado y dale "Descargar vínculo")</p>
            
            <div class="ad-container">
                <p style="font-size: 0.6rem; color: #444;">PUBLICIDAD</p>
                <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
                <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
            </div>
        {% endif %}
    </div>
    <div style="margin-top: 40px; font-size: 0.5rem; color: #222; letter-spacing: 2px;">CIFRADO DE EXTREMO A EXTREMO</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            ydl_opts = {'format': 'best', 'quiet': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_url = info.get('url')
        except Exception as e:
            print(f"Error: {e}")
    return render_template_string(html_content, video_url=video_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
