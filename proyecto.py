from flask import Flask, render_template_string, request

app = Flask(__name__)

def construir_estrategia(tema):
    return {
        "nicho": tema.upper(),
        "fase1": ["Analizar competencia en TikTok", f"Definir el 'Por qué' de {tema}", "Crear identidad visual mínima"],
        "fase2": [f"Gancho viral: 'Lo que nadie te dice de {tema}'", "Publicar 3 Reels/TikToks diarios", "Interacción masiva con audiencia"],
        "fase3": ["Lanzar producto digital (Ebook/Curso)", "Optimizar el link de la Bio", f"Escalar anuncios hacia {tema}"],
        "fase4": ["Automatizar ventas", "Crear comunidad en Discord/Telegram", "Revertir ganancias en equipo Pro"]
    }

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX | Business Architect</title>
    <style>
        :root { --neon: #00ff7f; --dark: #0a0a0a; --gray: #1a1a1a; }
        body { background: var(--dark); color: #fff; font-family: 'Inter', sans-serif; margin: 0; padding: 0; overflow-x: hidden; }
        .hero { padding: 60px 20px; text-align: center; background: radial-gradient(circle at top, #111 0%, #0a0a0a 100%); }
        .logo { font-size: 3.5rem; letter-spacing: 15px; font-weight: 100; margin: 0; text-shadow: 0 0 20px rgba(0,255,127,0.3); }
        .subtitle { color: var(--neon); font-size: 0.8rem; letter-spacing: 5px; margin-bottom: 40px; }
        
        .search-container { max-width: 600px; margin: auto; position: relative; }
        input { width: 100%; padding: 20px; background: var(--gray); border: 1px solid #333; border-radius: 5px; color: #fff; font-size: 1rem; transition: 0.3s; }
        input:focus { border-color: var(--neon); outline: none; box-shadow: 0 0 15px rgba(0,255,127,0.2); }
        button { width: 100%; padding: 18px; background: var(--neon); color: #000; border: none; font-weight: bold; cursor: pointer; margin-top: 15px; letter-spacing: 2px; transition: 0.3s; }
        button:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,255,127,0.3); }

        /* DASHBOARD GRID */
        .dashboard { max-width: 1000px; margin: 50px auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; }
        .card { background: var(--gray); border: 1px solid #222; padding: 25px; border-radius: 10px; position: relative; transition: 0.3s; }
        .card:hover { border-color: var(--neon); }
        .card h3 { color: var(--neon); font-size: 0.9rem; letter-spacing: 2px; margin-top: 0; border-bottom: 1px solid #333; padding-bottom: 10px; }
        .card ul { list-style: none; padding: 0; margin-top: 20px; }
        .card li { margin-bottom: 15px; font-size: 0.9rem; color: #ccc; display: flex; align-items: flex-start; }
        .card li::before { content: '→'; color: var(--neon); margin-right: 10px; font-weight: bold; }

        .ad-banner { max-width: 1000px; margin: 40px auto; background: #000; border: 1px dashed #333; padding: 20px; text-align: center; }
        .footer { padding: 40px; font-size: 0.6rem; color: #333; letter-spacing: 3px; text-align: center; }
    </style>
</head>
<body>
    <div class="hero">
        <h1 class="logo">VELOX</h1>
        <div class="subtitle">HIGH-FIDELITY BUSINESS ARCHITECT</div>
        
        <div class="search-container">
            <form method="POST">
                <input type="text" name="topic" placeholder="ESCRIBE TU IDEA (Ej: Marca de Ropa, Agencia, Canal Gamer)" required>
                <button type="submit">GENERAR HOJA DE RUTA MAESTRA</button>
            </form>
        </div>
    </div>

    {% if data %}
    <div style="text-align: center; margin-top: 30px;">
        <span style="border: 1px solid var(--neon); padding: 5px 15px; border-radius: 50px; color: var(--neon); font-size: 0.7rem;">PROYECTO: {{ data.nicho }}</span>
    </div>

    <div class="dashboard">
        <div class="card">
            <h3>01. CIMENTACIÓN Y NICHO</h3>
            <ul>{% for item in data.fase1 %}<li>{{ item }}</li>{% endfor %}</ul>
        </div>
        <div class="card">
            <h3>02. TRACCIÓN Y VIRALIDAD</h3>
            <ul>{% for item in data.fase2 %}<li>{{ item }}</li>{% endfor %}</ul>
        </div>
        <div class="card">
            <h3>03. CONVERSIÓN Y VENTAS</h3>
            <ul>{% for item in data.fase3 %}<li>{{ item }}</li>{% endfor %}</ul>
        </div>
        <div class="card">
            <h3>04. ESCALABILIDAD PRO</h3>
            <ul>{% for item in data.fase4 %}<li>{{ item }}</li>{% endfor %}</ul>
        </div>
    </div>

    <div class="ad-banner">
        <p style="font-size: 0.6rem; color: #444; margin-bottom: 15px;">PUBLICIDAD RECOMENDADA</p>
        <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
        <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
    </div>
    {% endif %}

    <div class="footer">
        POWERED BY VELOX AI ENGINE | 2026 ENCRYPTED SYSTEM
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        topic = request.form.get('topic')
        data = construir_estrategia(topic)
    return render_template_string(html_content, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
