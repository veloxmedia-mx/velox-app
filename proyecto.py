from flask import Flask, render_template_string, request

app = Flask(__name__)

def generar_mapa(tema):
    # Esta es la lógica que estructura el "Árbol"
    return {
        "idea_central": tema.upper(),
        "ramas": [
            {
                "titulo": "1. ESTRUCTURA DE NEGOCIO",
                "puntos": [f"Nicho: Especializado en {tema}", "Modelo: Suscripción o Servicio High Ticket", "Diferenciador: Calidad 'High Fidelity'"]
            },
            {
                "titulo": "2. ESTRATEGIA DE CONTENIDO",
                "puntos": [f"Gancho: El secreto de {tema}", "Formato: Video vertical educativo", "CTA: Lead Magnet gratuito"]
            },
            {
                "titulo": "3. MONETIZACIÓN",
                "puntos": ["Adsense / Adsterra", "Afiliados relacionados", "Venta de consultoría"]
            }
        ]
    }

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX - Architect</title>
    <style>
        body { background: #050505; color: #fff; font-family: 'Courier New', Courier, monospace; margin: 0; padding: 20px; text-align: center; }
        .container { max-width: 600px; margin: auto; }
        .logo { font-size: 3rem; letter-spacing: 15px; font-weight: 100; color: #fff; margin-bottom: 0; }
        .subtitle { color: #00ff7f; font-size: 0.8rem; letter-spacing: 5px; margin-bottom: 40px; }
        
        input { width: 100%; padding: 20px; background: transparent; border: 2px solid #00ff7f; border-radius: 0; color: #fff; font-size: 1.2rem; text-align: center; margin-bottom: 20px; }
        button { width: 100%; padding: 20px; background: #00ff7f; color: #000; border: none; font-weight: bold; cursor: pointer; font-size: 1rem; letter-spacing: 2px; }
        
        /* DISEÑO DE ÁRBOL / ESTRUCTURA */
        .tree-container { margin-top: 50px; text-align: left; border-left: 2px solid #333; padding-left: 20px; margin-left: 10px; }
        .node-main { color: #00ff7f; font-size: 1.5rem; margin-bottom: 30px; font-weight: bold; border: 1px solid #00ff7f; padding: 10px; display: inline-block; }
        .branch { margin-bottom: 30px; position: relative; }
        .branch::before { content: '├──'; position: absolute; left: -22px; color: #333; }
        .branch-title { font-weight: bold; color: #fff; background: #222; padding: 5px 10px; display: inline-block; margin-bottom: 10px; }
        .point { font-size: 0.9rem; color: #aaa; margin-left: 20px; margin-bottom: 5px; }
        .point::before { content: '• '; color: #00ff7f; }

        .ad-section { margin-top: 60px; border-top: 1px solid #222; padding-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="logo">VELOX</h1>
        <p class="subtitle">BUSINESS ARCHITECT</p>

        <form method="POST">
            <input type="text" name="topic" placeholder="TU IDEA DE NEGOCIO O CONTENIDO" required>
            <button type="submit">GENERAR MAPA ESTRUCTURAL</button>
        </form>

        {% if mapa %}
            <div class="tree-container">
                <div class="node-main">ORIGEN: {{ mapa.idea_central }}</div>
                
                {% for rama in mapa.ramas %}
                <div class="branch">
                    <div class="branch-title">{{ rama.titulo }}</div>
                    {% for punto in rama.puntos %}
                        <div class="point">{{ punto }}</div>
                    {% endfor %}
                </div>
                {% endfor %}
            </div>

            <div class="ad-section">
                <p style="font-size: 10px; color: #444; letter-spacing: 2px;">SPONSORED BY ADSTERRA</p>
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
    mapa = None
    if request.method == 'POST':
        tema = request.form.get('topic')
        mapa = generar_mapa(tema)
    return render_template_string(html_content, mapa=mapa)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
