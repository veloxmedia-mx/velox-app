from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Diccionario de estrategias por tipo de contenido
estrategias = [
    {
        "tipo": "Educativo (Tutorial)",
        "pasos": [
            "Gancho: 'El error que el 90% comete en {}.'",
            "Desarrollo: Muestra cómo solucionar ese error en 3 pasos simples.",
            "Cierre: 'Sígueme para dominar {} sin esfuerzo.'"
        ]
    },
    {
        "tipo": "Polémico (Opinión)",
        "pasos": [
            "Gancho: 'La verdad honesta sobre {} que nadie acepta.'",
            "Desarrollo: Da un punto de vista fuerte que genere comentarios.",
            "Cierre: '¿Estás de acuerdo o crees que me equivoqué? Te leo.'"
        ]
    },
    {
        "tipo": "Curiosidad (Storytelling)",
        "pasos": [
            "Gancho: 'Lo que daría por haber sabido esto de {} hace 2 años.'",
            "Desarrollo: Cuenta una historia breve de fracaso a éxito.",
            "Cierre: 'Guarda este video para tu próximo proyecto de {}.'"
        ]
    }
]

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - Estratega Pro</title>
    <style>
        body { background: #050505; color: #fff; font-family: 'Inter', sans-serif; margin: 0; padding: 20px; text-align: center; }
        .container { max-width: 500px; margin: auto; }
        .logo { font-size: 2.5rem; letter-spacing: 10px; font-weight: 100; margin-top: 30px; }
        .subtitle { color: #00ff7f; font-size: 0.7rem; letter-spacing: 3px; margin-bottom: 40px; }
        input { width: 100%; padding: 15px; background: #111; border: 1px solid #00ff7f; border-radius: 10px; color: #fff; margin-bottom: 20px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #fff; color: #000; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; }
        
        /* Estética del Mapa/Diagrama */
        .map-container { margin-top: 40px; text-align: left; position: relative; padding-left: 20px; }
        .step { background: #111; border: 1px solid #222; padding: 15px; border-radius: 10px; margin-bottom: 15px; position: relative; }
        .step::before { content: ''; position: absolute; left: -15px; top: 0; bottom: -15px; width: 2px; background: #00ff7f; }
        .step:last-child::before { display: none; }
        .badge { background: #00ff7f; color: #000; font-size: 10px; padding: 2px 8px; border-radius: 5px; font-weight: bold; }
        
        .ad-box { margin-top: 50px; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">V E L O X</div>
        <div class="subtitle">ESTRATEGIA DE CONTENIDO</div>

        <form method="POST">
            <input type="text" name="topic" placeholder="¿Sobre qué es tu video?" required>
            <button type="submit">CREAR MAPA DE CONTENIDO</button>
        </form>

        {% if plan %}
            <div class="map-container">
                <p style="color:#00ff7f; font-weight:bold;">TIPO: {{ plan.tipo }}</p>
                {% for paso in plan.pasos %}
                    <div class="step">
                        <span class="badge">PASO {{ loop.index }}</span>
                        <p style="margin: 10px 0 0 0;">{{ paso }}</p>
                    </div>
                {% endfor %}
            </div>

            <div class="ad-box">
                <p style="font-size:10px; color:#444;">PATROCINADO</p>
                <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
                <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    plan = None
    if request.method == 'POST':
        topic = request.form.get('topic')
        raw_plan = random.choice(estrategias)
        # Inyectar el tema en cada paso
        plan = {
            "tipo": raw_plan["tipo"],
            "pasos": [p.format(topic) for p in raw_plan["pasos"]]
        }
    return render_template_string(html_content, plan=plan)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
