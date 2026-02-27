from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX | TRENDS</title>
    <style>
        :root { --accent: #ff0055; --bg: #fff; }
        body { background: #f4f4f4; color: #222; font-family: 'Helvetica Neue', sans-serif; margin: 0; padding: 0; }
        header { background: #000; color: #fff; padding: 15px; text-align: center; border-bottom: 4px solid var(--accent); }
        .nav { background: #fff; padding: 10px; font-size: 0.8rem; text-align: center; border-bottom: 1px solid #ddd; position: sticky; top: 0; z-index: 100; }
        .container { max-width: 800px; margin: 20px auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .category { color: var(--accent); font-weight: bold; font-size: 0.8rem; text-transform: uppercase; }
        h1 { font-size: 2.2rem; line-height: 1.1; margin: 10px 0; color: #111; }
        .meta { color: #888; font-size: 0.8rem; margin-bottom: 20px; }
        .news-img { width: 100%; height: 400px; background: #ddd; border-radius: 5px; margin-bottom: 20px; display: flex; align-items: center; justify-content: center; color: #888; overflow: hidden; }
        p { line-height: 1.6; font-size: 1.1rem; color: #333; }
        
        /* ADSTERRA PLACEHOLDERS */
        .ad-slot { background: #fafafa; border: 1px dashed #ccc; padding: 10px; margin: 20px 0; text-align: center; min-height: 250px; }
        .sidebar-ad { position: fixed; right: 10px; top: 100px; width: 160px; height: 600px; background: #eee; border: 1px solid #ddd; display: none; }
        
        @media (max-width: 600px) { h1 { font-size: 1.6rem; } .sidebar-ad { display: none; } }
    </style>
</head>
<body>

<header>
    <h2 style="margin:0; letter-spacing:5px;">VELOX<span style="color:var(--accent)">NEWS</span></h2>
</header>

<div class="nav">TECNOLOGÍA • NEGOCIOS • IA • TIKTOK TRENDS</div>

<div class="container">
    <div class="category">Tendencias Digitales</div>
    <h1>El secreto que los grandes creadores usan para facturar en 2026</h1>
    <div class="meta">Por: Redacción Velox • Actualizado hace 5 min</div>

    <div class="ad-slot">
        <p style="font-size:10px; color:#aaa;">PUBLICIDAD</p>
        <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
        <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
    </div>

    <p>En el panorama actual de la economía digital, la monetización se ha vuelto el pilar fundamental para cualquier emprendedor tecnológico. Las plataformas como Adsterra han revolucionado la forma en que el tráfico se convierte en ingresos reales.</p>
    
    <div class="news-img">
        <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80" style="width:100%; height:100%; object-fit:cover;">
    </div>

    <p>Según expertos en el área, el contenido de nicho es el que mejor paga. No se trata de cuántas personas te ven, sino de QUIÉN te ve. Los nichos de tecnología y finanzas personales siguen liderando el CPM en este primer trimestre de 2026.</p>

    <div class="ad-slot">
        <p style="font-size:10px; color:#aaa;">PUBLICIDAD RECOMENDADA</p>
        </div>

    <p>Para escalar un negocio digital, la automatización y el uso de herramientas inteligentes de análisis (como nuestra calculadora Velox) son indispensables. La clave está en la consistencia y en la capacidad de adaptar el contenido a las nuevas audiencias.</p>
    
    <p style="background:#eee; padding:15px; border-left:4px solid var(--accent);">
        <strong>Dato curioso:</strong> El 70% de los clics en anuncios ocurren en dispositivos móviles durante las primeras horas de la mañana.
    </p>

    <p>¿Estás listo para dar el siguiente paso? Mantente conectado a Velox News para más actualizaciones sobre la economía de los creadores.</p>
</div>

</body>
</html>
''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
