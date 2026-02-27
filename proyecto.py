import os
import requests
from flask import Flask, render_template_string, request, Response
import yt_dlp

app = Flask(__name__)

# --- DISEÑO MATRIX LUXURY ---
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VELOX | CIFRADO EXTREMO</title>
    <style>
        body { 
            background-color: #0a0a0a; 
            color: #00ff41; 
            font-family: 'Courier New', Courier, monospace; 
            display: flex; flex-direction: column; align-items: center; justify-content: center; 
            min-height: 100vh; margin: 0; 
            background-image: linear-gradient(0deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px);
            background-size: 30px 30px;
        }
        .container { 
            text-align: center; border: 1px solid #00ff41; padding: 40px; 
            box-shadow: 0 0 30px rgba(0, 255, 65, 0.2); background: #000; 
            width: 380px; position: relative;
        }
        h1 { 
            font-size: 2.8rem; color: #d1d1d1; text-shadow: 0 0 10px #00ff41; 
            margin: 0 0 10px 0; letter-spacing: 8px; font-weight: bold;
        }
        .subtitle { font-size: 0.7rem; color: #00ff41; margin-bottom: 30px; letter-spacing: 2px; }
        input { 
            width: 100%; padding: 15px; margin-bottom: 20px; 
            background: #050505; border: 1px solid #00ff41; 
            color: #00ff41; box-sizing: border-box; outline: none; text-align: center;
        }
        .btn-main { 
            background: #00ff41; color: #000; border: none; padding: 18px; 
            cursor: pointer; width: 100%; font-weight: bold; font-size: 1rem;
            transition: 0.3s; box-shadow: 0 0 15px #00ff41;
        }
        .btn-main:hover { background: #00cc33; box-shadow: 0 0 25px #00ff41; }
        
        .success-box { 
            margin-top: 25px; border: 1px double #00ff41; padding: 15px; 
            animation: blink 2s infinite; 
        }
        @keyframes blink { 50% { opacity: 0.7; } }

        .download-link {
            color: #000; background: #00ff41; text-decoration: none;
            padding: 10px 20px; display: inline-block; margin-top: 10px;
            font-weight: bold; width: 80%;
        }

        .ad-space { margin-top: 30px; border-top: 1px solid #222; padding-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>VELOX</h1>
        <div class
