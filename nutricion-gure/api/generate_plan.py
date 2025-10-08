# api/generate_plan.py

import os
import json
from http.server import BaseHTTPRequestHandler
from pydantic import BaseModel, ValidationError
import google.generativeai as genai

# Modelo de Pydantic para validar los datos de entrada
class UserProfile(BaseModel):
    age: int
    height: int
    weight: float
    body_fat: int
    stress_level: int
    sleep_hours: float
    training_days: int
    goal: str

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Maneja las peticiones POST a la ruta /api/generate_plan
        """
        try:
            # --- Leer y validar el cuerpo de la petición ---
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                profile = UserProfile(**data)
            except (json.JSONDecodeError, ValidationError) as e:
                self.send_response(400) # Bad Request
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_response = {"error": "Petición mal formada o datos inválidos.", "details": str(e)}
                self.wfile.write(json.dumps(error_response).encode('utf-8'))
                return

            # --- Lógica para llamar a Gemini ---
            gemini_api_key = os.getenv("GEMINI_API_KEY")
            if not gemini_api_key:
                raise Exception("La clave de API de Gemini no está configurada en el servidor.")
            
            genai.configure(api_key=gemini_api_key)

            prompt = f"""
            **Rol del Modelo (Gemini):** Actúa como un Nutricionista Deportivo Certificado y Entrenador de Rendimiento Físico, especializado en ciclismo. Tu tono debe ser autoritario, motivador y sumamente preciso.

            **Instrucción de Formato (MANDATORIA):** Genera la respuesta SIEMPRE en un objeto JSON estructurado que incluya las siguientes claves: "PlanID", "AnalysisSummary", "CurrentStrategy", "PhaseAdjustments", "DetailedMealPlan" (para 7 días), y "KeyNutrientFocus". NO incluyas ```json ni ningún otro texto fuera del objeto JSON.

            **Reglas Estrictas de Generación Nutricional:**
            - **Foco España:** USA SOLO alimentos comunes y fáciles de encontrar en un supermercado estándar en España.
            - **Personalización:** Adapta las recetas a un nivel de habilidad en la cocina medio y un presupuesto medio.

            **Datos del Ciclista para el Plan:**
            - Edad: {profile.age} años
            - Altura: {profile.height} cm
            - Peso: {profile.weight} kg
            - Grasa Corporal Estimada: {profile.body_fat}%
            - Nivel de Estrés Reportado: {profile.stress_level}/10
            - Horas de Sueño: {profile.sleep_hours}
            - Días de entrenamiento/semana: {profile.training_days}
            - **Objetivo Principal:** "{profile.goal}"

            Ahora, genera el plan nutricional completo en el formato JSON solicitado.
            """

            model = genai.GenerativeModel('gemini-1.5-pro-latest')
            response = model.generate_content(prompt)
            
            cleaned_response_text = response.text.strip().replace("```json", "").replace("```", "")
            
            if not cleaned_response_text:
                raise Exception("La respuesta de la IA estaba vacía.")

            plan_json = json.loads(cleaned_response_text)
            
            # --- Enviar respuesta exitosa ---
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(plan_json).encode('utf-8'))

        except Exception as e:
            # --- Manejar errores internos del servidor ---
            print(f"Error interno en la función: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {"error": "Error interno del servidor.", "details": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
        
        return
