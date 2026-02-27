from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    gancho = ""
    tema = ""
    if request.method == 'POST':
        tema = request.form.get('topic', 'tu nicho')
        opciones = [
            f"El secreto de {tema} que nadie te dice.",
            f"Deja de perder tiempo en {tema} y haz esto.",
            f"Lo que aprendí de {tema} después de 1 año."
        ]
        gancho = random.choice(opciones)

    html = f'''
    <body style="background:#000;color:#fff;text-align:center;font-family:sans-serif;padding:50px;">
        <h1 style="letter-spacing:10px;">V E L O X</h1>
        <p style="color:#00ff7f;">CREATOR AI</p>
        <form method="POST" style="margin:30px;">
            <input name="topic" placeholder="Ej: Fitness" style="padding:10px;border-radius:5px;border:1px solid #00ff7f;background:none;color:#fff;">
            <button style="padding:10px 20px;background:#fff;border:none;border-radius:5px;cursor:pointer;">GENERAR</button>
        </form>
        {f'<div style="border:1px dashed #00ff7f;padding:20px;"><h3>{gancho}</h3></div>' if gancho else ''}
        
        <div style="margin-top:50px;">
            <p style="font-size:10px;color:#444;">PUBLICIDAD</p>
            <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
            <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
        </div>
    </body>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
