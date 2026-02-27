from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX | TOXIC-CHECK AI</title>
    <style>
        :root { --neon: #ff0055; --bg: #050505; }
        body { background: var(--bg); color: #fff; font-family: 'Courier New', monospace; margin: 0; padding: 15px; text-align: center; }
        .container { max-width: 500px; margin: 30px auto; border: 1px solid #222; padding: 25px; border-radius: 20px; background: #0a0a0a; box-shadow: 0 0 20px rgba(255,0,85,0.1); }
        h1 { color: var(--neon); letter-spacing: 5px; font-size: 1.5rem; }
        textarea { width: 100%; height: 120px; background: #000; border: 1px solid #333; color: #0f0; padding: 15px; border-radius: 10px; box-sizing: border-box; resize: none; margin-top: 15px; }
        button { width: 100%; padding: 15px; background: var(--neon); color: #fff; border: none; font-weight: bold; border-radius: 10px; cursor: pointer; margin-top: 15px; text-transform: uppercase; }
        #loader { display: none; margin-top: 20px; color: var(--neon); }
        #result { display: none; margin-top: 25px; padding: 20px; border: 1px solid var(--neon); border-radius: 10px; text-align: left; background: rgba(255,0,85,0.05); }
        .score { font-size: 3rem; font-weight: 900; color: var(--neon); text-align: center; display: block; }
        .ad-space { margin-top: 40px; padding: 10px; border: 1px dashed #444; }
    </style>
</head>
<body>

<div class="container">
    <h1>TOXIC-CHECK <span style="font-size:0.8rem; color:#444;">AI</span></h1>
    <p style="font-size:0.8rem; color:#777;">Pega el último mensaje de esa persona y descubre la verdad.</p>
    
    <textarea id="chatInput" placeholder="Ej: 'No me pasa nada, haz lo que quieras...'"></textarea>
    
    <button onclick="analizar()">AUDITAR MENSAJE</button>

    <div id="loader">ANALIZANDO MICRO-AGRESIONES Y PATRONES...</div>

    <div id="result">
        <label style="font-size:0.7rem; color:#777;">NIVEL DE TOXICIDAD:</label>
        <span class="score" id="v_score">0%</span>
        <p id="v_desc" style="font-size:0.9rem; line-height:1.4;"></p>
        <hr style="border:0; border-top:1px solid #222;">
        <small style="color:#0f0;">CONSEJO DE VELOX AI:</small>
        <p id="v_advice" style="font-size:0.8rem; font-style:italic; color:#aaa;"></p>
    </div>
</div>

<div class="ad-space">
    <p style="font-size:10px; color:#444;">ANUNCIO PATROCINADO (ADSTERRA)</p>
    <script async="async" data-cfasync="false" src="https://pl28804683.effectivegatecpm.com/5e09cff53476280c79e769b840e93d6f/invoke.js"></script>
    <div id="container-5e09cff53476280c79e769b840e93d6f"></div>
</div>

<script>
    function analizar() {
        const text = document.getElementById('chatInput').value;
        if(text.length < 5) return alert("Escribe un mensaje real, fiera.");

        document.getElementById('loader').style.display = "block";
        document.getElementById('result').style.display = "none";

        setTimeout(() => {
            document.getElementById('loader').style.display = "none";
            document.getElementById('result').style.display = "block";
            
            // Lógica de "IA" simulada
            const score = Math.floor(Math.random() * (99 - 40 + 1) + 40);
            document.getElementById('v_score').innerText = score + "%";
            
            let desc = "";
            let advice = "";

            if(score > 80) {
                desc = "ALERTA ROJA. Detectamos gaslighting de manual y manipulación de alto nivel. Esa persona sabe exactamente qué botones apretar.";
                advice = "Bloquea, borra el número y vete a vivir a otro país. Estás avisado.";
            } else if(score > 60) {
                desc = "TOXICIDAD PASIVO-AGRESIVA. Hay un 60% de probabilidad de que el mensaje tenga un doble sentido diseñado para hacerte sentir culpable.";
                advice = "Contesta con un 'Ok' y mira cómo el mundo arde. No des explicaciones.";
            } else {
                desc = "DUDOSO. El sistema detecta inseguridad y falta de comunicación clara, pero no llega a ser un peligro nuclear.";
                advice = "Mándale un sticker de un perrito y espera 2 horas antes de volver a escribir.";
            }

            document.getElementById('v_desc').innerText = desc;
            document.getElementById('v_advice').innerText = advice;
        }, 2500);
    }
</script>

</body>
</html>
''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
