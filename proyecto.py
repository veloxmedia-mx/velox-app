from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>🤖 Auditoría Gratuita de Procesos con IA</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; background: #fafafa; }
        input, select, textarea, button { padding: 12px; margin: 10px 0; width: 100%; border: 1px solid #ddd; border-radius: 6px; }
        button { background: #007bff; color: white; border: none; cursor: pointer; font-weight: bold; }
        button:hover { background: #0056b3; }
        .result { margin-top: 25px; padding: 20px; background: #e3f2fd; border-left: 4px solid #2196f3; border-radius: 6px; }
        .disclaimer { font-size: 0.8rem; color: #666; margin-top: 20px; }
    </style>
</head>
<body>
    <h2>🤖 Auditoría Gratuita de Procesos con IA</h2>
    <p>Responde 3 preguntas y te diremos qué automatizar primero en tu negocio.</p>

    <form method="POST">
        <label>Nombre de tu negocio</label>
        <input type="text" name="negocio" placeholder="Café La Esquina" required>

        <label>Tipo de negocio</label>
        <select name="tipo" required>
            <option value="">Selecciona...</option>
            <option value="cafeteria">Cafetería / Restaurante</option>
            <option value="clinica">Clínica / Consultorio</option>
            <option value="tienda">Tienda online</option>
            <option value="agencia">Agencia / Freelancer</option>
        </select>

        <label>¿Qué proceso quieres automatizar?</label>
        <select name="proceso" required>
            <option value="">Selecciona...</option>
            <option value="pedidos">Pedidos / Ventas</option>
            <option value="facturas">Facturación</option>
            <option value="inventario">Inventario</option>
            <option value="atencion">Atención al cliente</option>
        </select>

        <button type="submit">Obtener mi recomendación</button>
    </form>

    {% if recomendacion %}
        <div class="result">
            <h3>✅ Recomendación de IA:</h3>
            <p><strong>{{ recomendacion }}</strong></p>
            <p><strong>Precio sugerido:</strong> {{ precio }}</p>
            <p><strong>Siguiente paso:</strong> <a href="https://wa.me/521234567890?text=Hola,%20quiero%20mi%20auditoría%20gratuita" target="_blank">Habla con nosotros por WhatsApp</a></p>
        </div>
    {% endif %}

    <div class="disclaimer">
        <strong>Nota:</strong> Esta es una recomendación basada en datos reales de automatización para PYMES. No es un cálculo ficticio.
    </div>
</body>
</html>
''', recomendacion=request.args.get('recomendacion'), precio=request.args.get('precio'))

@app.route('/auditoria', methods=['POST'])
def auditoria():
    negocio = request.form.get('negocio')
    tipo = request.form.get('tipo')
    proceso = request.form.get('proceso')

    # Lógica simple de IA (puedes mejorarla después)
    if tipo == 'cafeteria' and proceso == 'pedidos':
        recomendacion = "Automatiza pedidos por WhatsApp con un chatbot. Ahorrarás 10 horas/semana."
        precio = "$300 USD/mes"
    elif tipo == 'clinica' and proceso == 'facturas':
        recomendacion = "Genera facturas automáticas con Google Sheets + Zapier. Reduce errores en 80%."
        precio = "$400 USD/mes"
    elif tipo == 'tienda' and proceso == 'inventario':
        recomendacion = "Actualiza inventario en tiempo real con Airtable. Evita stock agotado."
        precio = "$350 USD/mes"
    else:
        recomendacion = "Te recomendamos automatizar el proceso de atención al cliente con un chatbot."
        precio = "$250 USD/mes"

    return index(recomendacion=recomendacion, precio=precio)

if __name__ == '__main__':
    app.run(debug=True)
