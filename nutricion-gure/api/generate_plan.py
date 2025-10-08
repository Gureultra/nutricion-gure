# api/generate_plan.py (Versión de prueba)

import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """
        Una función de prueba que ignora la petición y siempre
        devuelve un mensaje de éxito en formato JSON.
        """
        # 1. Envía una respuesta de éxito (200 OK)
        self.send_response(200)

        # 2. Especifica que el contenido es JSON
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # 3. Escribe el cuerpo de la respuesta
        response_body = {"message": "La API de prueba funciona correctamente!"}
        self.wfile.write(json.dumps(response_body).encode('utf-8'))

        return
