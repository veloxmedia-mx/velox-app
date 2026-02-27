from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'no_warnings': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_url = info.get('url')
        except Exception as e:
            print(f"Error: {e}")

    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)

# Crea la carpeta templates si no existe y guarda este HTML como index.html
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - Descarga TikTok</title>
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            background-image: radial-gradient(circle, #1a1a1a 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .container {
            text-align: center;
            border: 3px solid #00ff00;
            padding: 40px;
            box-shadow: 0 0 20px #00ff00, inset 0 0 10px #00ff00;
            background: rgba(0, 0, 0, 0.9);
            max-width: 90%;
            width: 400px;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 20px;
            text-shadow: 3px 3px #ff00ff;
            letter-spacing: 5px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            background: #222;
            border: 1px solid #ff00ff;
            color: #00ff00;
            box-sizing: border-box;
        }
        button {
            background: #ff00ff;
            color: #fff;
            border: none;
            padding: 15px 30px;
            font-size: 1.2rem;
            cursor: pointer;
            width: 100%;
            font-weight: bold;
            box-shadow: 5px 5px #00ff00;
        }
        button:hover {
            transform: translate(-2px, -2px);
            box-shadow: 7px 7px #00ff00;
        }
        .result {
            margin-top: 30px;
            border-top: 2px dashed #00ff00;
            padding-top: 20px;
        }
        .ad-container {
            margin-top: 25px;
            padding: 10px;
            border: 1px solid #333;
        }
        .download-btn {
            background: #00ff00;
            color: #000;
            text-decoration: none;
            padding: 10px 20px;
            display: inline-block;
            margin-top: 10px;
            font-weight: bold;
        }
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
            <p style="color: #ff00ff;">¡PROCESO COMPLETADO!</p>
            <a href="{{ video_url }}" class="download-btn" target="_blank">DESCARGAR AHORA</a>
            
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

# Esto es un truco para que Render maneje el HTML interno sin archivos extra
@app.route('/test-html')
def test():
    return html_content

@app.route('/')
def home():
    import flask
    return flask.render_template_string(html_content, video_url=None)

@app.route('/', methods=['POST'])
def download():
    import flask
    url = flask.request.form.get('url')
    video_url = None
    try:
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url')
    except:
        pass
    return flask.render_template_string(html_content, video_url=video_url)
