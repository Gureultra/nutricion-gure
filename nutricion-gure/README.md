# Nutricion_Gure- Asesor Nutricional Para Ciclistas sin Complejos

Gure Ultra es una aplicación de nutrición de precisión para ciclistas recreativos que genera planes de alimentación dinámicos y ajustables en tiempo real según las indicaciones del entrenador y de las sensaciones del ciclista.

## Tech Stack

- **Frontend:** Next.js (React) con TypeScript y Tailwind CSS.
- **Backend:** Python 3.11 con FastAPI, desplegado como Funciones Serverless en Vercel.
- **IA:** Google Gemini.
- **Email:** Brevo (antes Sendinblue).
- **Despliegue:** Vercel.

## Cómo Empezar

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu_usuario/gure-ultra.git](https://github.com/tu_usuario/gure-ultra.git)
    cd gure-ultra
    ```

2.  **Instalar dependencias:**
    ```bash
    npm install
    pip install -r requirements.txt
    ```

3.  **Configurar variables de entorno:**
    Crea un archivo `.env` a partir de `.env.example` y añade tus claves de API.

4.  **Ejecutar localmente:**
    ```bash
    vercel dev
    ```