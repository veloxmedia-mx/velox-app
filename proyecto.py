from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Bases de datos más completas
hooks = [
    "El secreto que nadie te cuenta sobre {}.",
    "Deja de cometer este error si haces {}.",
    "3 herramientas que cambiarán tu forma de hacer {}.",
    "Cómo pasé de novato a experto en {} en 30 días.",
    "Lo que daría por saber esto antes de empezar en {}."
]

tips = [
    "Enfócate en la calidad, no en la cantidad.",
    "Aplica la regla de los 2 minutos para mejorar.",
    "Analiza lo que hace tu competencia y hazlo un 1% mejor.",
    "La constancia vence al talento siempre.",
    "Usa ganchos visuales además de los hablados."
]

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - Creator AI</title>
    <style>
        body { background-color: #050505; color: #ffffff; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .logo { font-size: 2.5rem; font-weight: 100; letter-spacing: 8px; margin-top: 50px; }
        .subtitle { font-size: 0.6rem; letter-spacing: 3px; color: #00ff7f; margin-bottom: 40px; }
        .card { background: #111; border: 1px solid #222; padding: 25px; border-radius: 20px; width: 100%; max-width: 400px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        input { width: 100%; padding: 15px; background: #1a1a1a; border: 1px solid #333; border-radius: 12px; color: #fff; margin-bottom: 15px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #00ff7f; color: #000; border: none; border-radius: 12px; font-weight: bold; cursor: pointer; transition: 0.3s; }
        button:hover { background: #fff; }
        .result-item { text-align: left; margin-top: 25px; border-left: 2px solid #00ff7f; padding-left: 15px; }
        .label { font-size: 0.7rem; color: #00ff7f; text-transform: uppercase; font-weight: bold; }
        .content { font-size: 1.1rem; margin: 5px 0 15px 0; }
        .ad-space { margin-top: 30px; border-radius: 15px; overflow: hidden; background: #000; padding: 10px; border: 1px solid #1a1a1a; }
    </style>
</head>
<body>
    <div class="logo">V E L O X</div>
    <div class="subtitle">CREATOR AI ENGINE</div>

    <div class="card">
        <form method="POST">
            <input type="text" name="topic" placeholder="Ej: Fitness, Gaming, Cocina..." required>
            <button type="submit">GENERAR ESTRATEGIA VIRAL</button>
        </form>

        {% if hook %}
            <div class="result-item">
                <div class="label">Gancho de inicio (0-3 seg):</div>
                <p class="content">"{{ hook }}"</p>
                
                <div class="label">Tip de valor:</div>
                <p class="content">{{ tip }}</p>
                
                <div class="label">Llamado a la acción:</div>
                <p class="content">"Dale like si quieres la parte 2 de {{ topic }}."</p>
            </div>
        {% endif %}
    </div>

    <div class="ad-space">
        <p style="font-size: 10px; color: #333;">PUBLICIDAD RECOMENDADA</p>
        <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
        <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    hook, tip, topic = None, None, None
    if request.method == 'POST':
        topic = request.form.get('topic')
        hook = random.choice(hooks).format(topic)
        tip = random.choice(tips)
    return render_template_string(html_content, hook=hook, tip=tip, topic=topic)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
