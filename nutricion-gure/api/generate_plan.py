from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class UserProfile(BaseModel):
    age: int
    height: int
    weight: float
    goal: str

@app.post("/api/generate_plan")
async def generate_plan(profile: UserProfile):
    """
    Recibe el perfil del usuario, llamaría a Gemini,
    y devuelve el plan nutricional en formato JSON.
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        return {"error": "GEMINI_API_KEY no configurada"}

    # --- Respuesta MOCK (simulada) para desarrollo ---
    mock_response = {
      "PlanID": "PLN-CYC-MOCK-001",
      "AnalysisSummary": "Análisis para ciclista de 32 años, 75 kg. El objetivo es la mejora de W/kg. El plan se centra en un déficit calórico controlado y una alta ingesta proteica.",
      "CurrentStrategy": "Recomposición Corporal para Optimización de W/kg",
      "DetailedMealPlan": [
        { "day": "Lunes (Entrenamiento Intensidad Z3/Z4 - 2h)", "meals": { "breakfast": { "meal": "Gachas de avena (80g) con bebida de almendras y plátano.", "function": "Energía sostenida gracias a carbohidratos complejos." }, "lunch": { "meal": "Ensalada grande de garbanzos con atún.", "function": "Recuperación completa con proteína y carbohidratos." }, "dinner": { "meal": "Pechuga de pavo a la plancha con boniato asado.", "function": "Proteína magra para la síntesis proteica nocturna." } } }
      ],
      "KeyNutrientFocus": [{"nutrient": "Hierro", "importance": "Vital para el transporte de oxígeno."}]
    }
    return mock_response