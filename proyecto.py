from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Base de datos de ganchos virales
hooks = [
    "El secreto que las marcas de {} no quieren que sepas...",
    "3 herramientas gratuitas de {} que te ahorrarán horas.",
    "Por esto tu contenido de {} no está funcionando.",
    "Cómo logré pasar de 0 a 10k seguidores hablando de {}.",
    "Deja de hacer esto si quieres crecer en el nicho de {}."
]

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - Creator Tools</title>
    <style>
        body { background-color: #050505; color: #ffffff; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; text-align: center; }
        .logo { font-size: 3rem; font-weight: 100; letter-spacing: 10px; margin-bottom: 5px; }
        .subtitle { font-size: 0.7rem; letter-spacing: 4px; color: #00ff7f; margin-bottom: 40px; }
        .container { width: 90%; max-width: 450px; }
        input { width: 100%; padding: 15px; background: transparent; border: 1px solid #00ff7f; border-radius: 10px; color: #fff; text-align: center; margin-bottom: 20px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #fff; color: #000; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; text-transform: uppercase; }
        .hook-box { margin-top: 30px; padding: 20px; border: 1px dashed #00ff7f; border-radius: 10px; background: rgba(0, 255, 127, 0.05); }
        .ad-container { margin-top: 40px; min-height: 250px; background: rgba(255,255,255,0.03); border-radius: 10px; padding: 10px; }
    </style>
</head>
<body>
    <div class="logo">V E L O X</div>
    <div class="subtitle">CREATOR AI TOOLS</div>

    <div class="container">
        <form method="POST">
            <input type="text" name="topic" placeholder="¿De qué trata tu video? (ej: Fitness)" required>
            <button type="submit">GENERAR GANCHO VIRAL</button>
        </form>

        {% if result %}
            <div class="hook-box">
                <p style="color: #00ff7f; font-size: 0.8rem;">TU GANCHO LISTO:</p>
                <h3 style="font-size: 1.2rem; line-height: 1.5;">{{ result }}</h3>
            </div>
            
            <div class="ad-container">
                <p style="font-size: 0.6rem; color: #444;">CONTENIDO PATROCINADO</p>
                <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
                <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
            </div>
        {% endif %}
    </div>
    <div style="margin-top: 50px; font-size: 0.5rem; color: #222; letter-spacing: 2px;">HERRAMIENTAS PROFESIONALES PARA CREADORES</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        topic = request.form.get('topic')
        template = random.choice(hooks)
        result = template.format(topic)
    return render_template_string(html_content, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
