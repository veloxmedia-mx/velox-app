from flask import Flask, render_template_string, request
import yt_dlp

app = Flask(__name__)

# DISEÑO PREMIUM "HIGH FIDELITY" + ANUNCIOS
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - High Fidelity Media</title>
    <style>
        body {
            background-color: #050505;
            color: #ffffff;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            text-align: center;
        }
        .logo {
            font-size: 3.5rem;
            font-weight: 200;
            letter-spacing: 12px;
            margin-bottom: 5px;
            color: #fff;
        }
        .subtitle {
            font-size: 0.7rem;
            letter-spacing: 4px;
            color: #00ff7f;
            text-transform: uppercase;
            margin-bottom: 50px;
        }
        .input-group {
            width: 90%;
            max-width: 450px;
        }
        input {
            width: 100%;
            padding: 18px;
            background: transparent;
            border: 1px solid #00ff7f;
            border-radius: 15px;
            color: #fff;
            font-size: 1rem;
            text-align: center;
            margin-bottom: 25px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 18px;
            background: #ffffff;
            color: #000;
            border: none;
            border-radius: 15px;
            font-size: 1rem;
            font-weight: bold;
            letter-spacing: 2px;
            cursor: pointer;
            text-transform: uppercase;
            transition: 0.3s;
        }
        button:hover {
            opacity: 0.8;
        }
        .result-box {
            margin-top: 40px;
            width: 90%;
            max-width: 450px;
        }
        .btn-download {
            background: #00ff7f;
            color: #000;
            padding: 15px;
            text-decoration: none;
            display: block;
            border-radius: 15px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .ad-container {
            margin-top: 30px;
            background: rgba(255,255,255,0.05);
            padding: 15px;
            border-radius: 10px;
        }
        .footer-text {
            margin-top: 50px;
            font-size: 0.6rem;
            color: #333;
            letter-spacing: 2px;
        }
    </style>
</head>
<body>
    <div class="logo">V E L O X</div>
    <div class="subtitle">HIGH FIDELITY MEDIA</div>

    <div class="input-group">
        <form method="POST">
            <input type="text" name="url" placeholder="https://vt.tiktok.com/..." required>
            <button type="submit">OBTENER VIDEO</button>
        </form>
    </div>

    {% if video_url %}
    <div class="result-box">
        <p style="color: #00ff7f; font-size: 0.8rem; margin-bottom: 15px;">¡ESTÁ LISTO!</p>
        <a href="{{ video_url }}" class="btn-download" target="_blank">¡DESCARGAR AHORA!</a>
        
        <div class="ad-container">
            <p style="font-size: 0.6rem; color: #666; margin-bottom: 10px;">PUBLICIDAD RECOMENDADA</p>
            <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
            <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
        </div>
    </div>
    {% endif %}

    <div class="footer-text">CIFRADO DE EXTREMO A EXTREMO</div>
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
        except:
            pass
    return render_template_string(html_content, video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
