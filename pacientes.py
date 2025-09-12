from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

# Lista para almacenar los nombres de los pacientes (en memoria)
pacientes = []

@app.route('/')
def index():
    """ formulario para registrar pacientes"""
    return render_template('registro.html')

@app.route('/registrar', methods=['POST'])
def registrar_paciente():
    """Procesa el formulario de registro de pacientes"""
    nombre = request.form.get('nombre', '').strip()
    
    if nombre:
        pacientes.append(nombre)
        flash(f'Paciente {nombre} registrado exitosamente', 'success')
    else:
        flash('Por favor ingrese un nombre válido', 'error')
    
    return redirect(url_for('index'))

@app.route('/cola')
def ver_cola():
    """Página para ver la cola de pacientes"""
    return render_template('cola.html', pacientes=pacientes)

@app.route('/atender', methods=['POST'])
def atender_paciente():
    """Atiende al primer paciente de la cola"""
    if pacientes:
        paciente_atendido = pacientes.pop(0)
        flash(f'Paciente {paciente_atendido} ha sido atendido', 'info')
    else:
        flash('No hay pacientes en la cola', 'warning')
    
    return redirect(url_for('ver_cola'))

# Crear directorio para templates si no existe
if not os.path.exists('templates'):
    os.makedirs('templates')

# Template para registro de pacientes
registro_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Pacientes</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: #0a0a0a;
            background-image: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #16213e 35%, #0a0a0a 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #e0e6ed;
        }
        
        .container {
            background: rgba(30, 41, 59, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(148, 163, 184, 0.2);
            padding: 50px 40px;
            border-radius: 24px;
            min-width: 450px;
            text-align: center;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            position: relative;
            overflow: hidden;
        }
        
        .container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #06b6d4, #8b5cf6, #ec4899, #06b6d4);
            background-size: 200% 100%;
            animation: shimmer 3s linear infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        h1 {
            color: #f8fafc;
            margin-bottom: 40px;
            font-size: 2.8em;
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        
        .icon {
            font-size: 3em;
            margin-bottom: 20px;
            background: linear-gradient(135deg, #06b6d4, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .form-group {
            margin-bottom: 30px;
            text-align: left;
        }
        
        label {
            display: block;
            margin-bottom: 12px;
            color: #cbd5e1;
            font-weight: 500;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        input[type="text"] {
            width: 100%;
            padding: 18px 20px;
            background: rgba(15, 23, 42, 0.6);
            border: 2px solid rgba(148, 163, 184, 0.2);
            border-radius: 12px;
            font-size: 16px;
            color: #f1f5f9;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        input[type="text"]:focus {
            outline: none;
            border-color: #06b6d4;
            background: rgba(15, 23, 42, 0.8);
            box-shadow: 0 0 0 4px rgba(6, 182, 212, 0.1);
            transform: translateY(-1px);
        }
        
        input[type="text"]::placeholder {
            color: #64748b;
        }
        
        .btn {
            background: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 100%);
            color: white;
            padding: 16px 32px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            margin: 12px 8px;
            text-decoration: none;
            display: inline-block;
            position: relative;
            overflow: hidden;
        }
        
        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        
        .btn:hover::before {
            left: 100%;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 20px 25px -5px rgba(6, 182, 212, 0.2);
        }
        
        .btn-secondary {
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        }
        
        .btn-secondary:hover {
            box-shadow: 0 20px 25px -5px rgba(16, 185, 129, 0.2);
        }
        
        .flash-messages {
            margin-bottom: 25px;
        }
        
        .flash-message {
            padding: 16px 20px;
            border-radius: 12px;
            margin-bottom: 12px;
            border-left: 4px solid;
            animation: slideIn 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .flash-success {
            background: rgba(5, 150, 105, 0.2);
            color: #6ee7b7;
            border-left-color: #10b981;
        }
        
        .flash-error {
            background: rgba(239, 68, 68, 0.2);
            color: #fca5a5;
            border-left-color: #ef4444;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">
            <i class="fas fa-user-plus"></i>
        </div>
        <h1>Registro de Pacientes</h1>
        
        <div class="flash-messages">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="flash-message flash-{{ category }}">
                            <i class="fas fa-check-circle" style="margin-right: 8px;"></i>
                            {{ message }}
                        </div>
                    {% endfor %}
                {% endif %}
            {% endwith %}
        </div>
        
        <form method="POST" action="{{ url_for('registrar_paciente') }}">
            <div class="form-group">
                <label for="nombre">
                    <i class="fas fa-user" style="margin-right: 8px;"></i>
                    Nombre del Paciente
                </label>
                <input type="text" id="nombre" name="nombre" required 
                       placeholder="Ingrese el nombre completo del paciente">
            </div>
            
            <button type="submit" class="btn">
                <i class="fas fa-plus" style="margin-right: 8px;"></i>
                Registrar Paciente
            </button>
            <a href="{{ url_for('ver_cola') }}" class="btn btn-secondary">
                <i class="fas fa-list" style="margin-right: 8px;"></i>
                Ver Cola
            </a>
        </form>
    </div>
</body>
</html>'''

# Template para ver la cola de pacientes 
cola_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cola de Pacientes</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: #0a0a0a;
            background-image: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #16213e 35%, #0a0a0a 100%);
            min-height: 100vh;
            padding: 20px;
            color: #e0e6ed;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: rgba(30, 41, 59, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(148, 163, 184, 0.2);
            padding: 40px;
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            position: relative;
            overflow: hidden;
        }
        
        .container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #06b6d4, #8b5cf6, #ec4899, #06b6d4);
            background-size: 200% 100%;
            animation: shimmer 3s linear infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        h1 {
            color: #f8fafc;
            margin-bottom: 40px;
            font-size: 2.8em;
            font-weight: 700;
            text-align: center;
            letter-spacing: -0.02em;
        }
        
        .header-icon {
            text-align: center;
            margin-bottom: 20px;
        }
        
        .header-icon i {
            font-size: 3em;
            background: linear-gradient(135deg, #06b6d4, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            flex-wrap: wrap;
            gap: 15px;
        }
        
        .btn {
            background: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 100%);
            color: white;
            padding: 16px 24px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            display: inline-block;
            position: relative;
            overflow: hidden;
        }
        
        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        
        .btn:hover::before {
            left: 100%;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 20px 25px -5px rgba(6, 182, 212, 0.2);
        }
        
        .btn-danger {
            background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
        }
        
        .btn-danger:hover {
            box-shadow: 0 20px 25px -5px rgba(239, 68, 68, 0.2);
        }
        
        .btn-success {
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        }
        
        .btn-success:hover {
            box-shadow: 0 20px 25px -5px rgba(16, 185, 129, 0.2);
        }
        
        .patient-count {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(148, 163, 184, 0.2);
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 25px;
            text-align: center;
            font-weight: 600;
            color: #cbd5e1;
            backdrop-filter: blur(10px);
        }
        
        .patient-count .number {
            font-size: 2em;
            font-weight: 700;
            color: #06b6d4;
            margin-left: 10px;
        }
        
        .table-container {
            overflow-x: auto;
            margin-bottom: 20px;
            border-radius: 16px;
            border: 1px solid rgba(148, 163, 184, 0.2);
            background: rgba(15, 23, 42, 0.4);
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th, td {
            padding: 20px;
            text-align: left;
            border-bottom: 1px solid rgba(148, 163, 184, 0.1);
        }
        
        th {
            background: rgba(30, 41, 59, 0.8);
            color: #f1f5f9;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 1px;
        }
        
        td {
            color: #cbd5e1;
        }
        
        tr:hover td {
            background: rgba(30, 41, 59, 0.4);
        }
        
        .position-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-weight: 600;
            font-size: 14px;
        }
        
        .position-1 {
            background: linear-gradient(135deg, #dc2626, #ef4444);
            color: white;
        }
        
        .position-other {
            background: rgba(100, 116, 139, 0.3);
            color: #94a3b8;
        }
        
        .status-badge {
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        .status-next {
            background: rgba(239, 68, 68, 0.2);
            color: #fca5a5;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }
        
        .status-waiting {
            background: rgba(100, 116, 139, 0.2);
            color: #94a3b8;
            border: 1px solid rgba(100, 116, 139, 0.3);
        }
        
        .no-patients {
            text-align: center;
            padding: 60px 20px;
            color: #64748b;
        }
        
        .no-patients i {
            font-size: 4em;
            margin-bottom: 20px;
            opacity: 0.5;
        }
        
        .no-patients h3 {
            font-size: 1.5em;
            margin-bottom: 10px;
            color: #94a3b8;
        }
        
        .flash-messages {
            margin-bottom: 25px;
        }
        
        .flash-message {
            padding: 16px 20px;
            border-radius: 12px;
            margin-bottom: 12px;
            border-left: 4px solid;
            animation: slideIn 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .flash-success {
            background: rgba(5, 150, 105, 0.2);
            color: #6ee7b7;
            border-left-color: #10b981;
        }
        
        .flash-info {
            background: rgba(6, 182, 212, 0.2);
            color: #7dd3fc;
            border-left-color: #06b6d4;
        }
        
        .flash-warning {
            background: rgba(245, 158, 11, 0.2);
            color: #fcd34d;
            border-left-color: #f59e0b;
        }
        
        @media (max-width: 768px) {
            .controls {
                flex-direction: column;
                align-items: stretch;
            }
            
            .btn {
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header-icon">
            <i class="fas fa-users"></i>
        </div>
        <h1>Cola de Pacientes</h1>
        
        <div class="flash-messages">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="flash-message flash-{{ category }}">
                            <i class="fas fa-info-circle" style="margin-right: 8px;"></i>
                            {{ message }}
                        </div>
                    {% endfor %}
                {% endif %}
            {% endwith %}
        </div>
        
        <div class="patient-count">
            <i class="fas fa-user-clock"></i>
            Pacientes en cola:
            <span class="number">{{ pacientes|length }}</span>
        </div>
        
        <div class="controls">
            <a href="{{ url_for('index') }}" class="btn btn-success">
                <i class="fas fa-user-plus" style="margin-right: 8px;"></i>
                Nuevo Paciente
            </a>
            
            {% if pacientes %}
                <form method="POST" action="{{ url_for('atender_paciente') }}" style="display: inline;">
                    <button type="submit" class="btn btn-danger" 
                            onclick="return confirm('¿Confirma atender al siguiente paciente?')">
                        <i class="fas fa-stethoscope" style="margin-right: 8px;"></i>
                        Atender Paciente
                    </button>
                </form>
            {% endif %}
        </div>
        
        <div class="table-container">
            {% if pacientes %}
                <table>
                    <thead>
                        <tr>
                            <th><i class="fas fa-hashtag"></i> Posición</th>
                            <th><i class="fas fa-user"></i> Paciente</th>
                            <th><i class="fas fa-clock"></i> Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for paciente in pacientes %}
                            <tr>
                                <td>
                                    <span class="position-badge {{ 'position-1' if loop.index == 1 else 'position-other' }}">
                                        {{ loop.index }}
                                    </span>
                                </td>
                                <td>
                                    <strong>{{ paciente }}</strong>
                                </td>
                                <td>
                                    {% if loop.index == 1 %}
                                        <span class="status-badge status-next">
                                            <i class="fas fa-arrow-right" style="margin-right: 4px;"></i>
                                            Siguiente
                                        </span>
                                    {% else %}
                                        <span class="status-badge status-waiting">
                                            <i class="fas fa-hourglass-half" style="margin-right: 4px;"></i>
                                            Esperando
                                        </span>
                                    {% endif %}
                                </td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            {% else %}
                <div class="no-patients">
                    <i class="fas fa-bed"></i>
                    <h3>Sin pacientes en cola</h3>
                    <p>La sala de espera está vacía. Registre el primer paciente para comenzar.</p>
                </div>
            {% endif %}
        </div>
    </div>
</body>
</html>'''

# Escribir los templates
with open('templates/registro.html', 'w', encoding='utf-8') as f:
    f.write(registro_html)

with open('templates/cola.html', 'w', encoding='utf-8') as f:
    f.write(cola_html)

if __name__ == '__main__':
    print(" Sistema de lista de pacientes ")
    print("=============================================")
    print("Navegue a: http://127.0.0.1:5000")
    print("Para detener el servidor presione Ctrl+C")
    app.run(debug=True)