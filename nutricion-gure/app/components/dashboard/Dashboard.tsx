// app/components/dashboard/Dashboard.tsx

'use client';

import { useEffect, useState } from 'react';
import Loader from '../ui/Loader';
import MealCard from './MealCard';
import ActionButtons from './ActionButtons';

const Dashboard = () => {
  const [plan, setPlan] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchPlan = async () => {
      setLoading(true);
      setError(null);

      try {
        // Estos son los datos del usuario que enviaremos al backend.
        // En el futuro, vendrían de un formulario de perfil.
        const userProfile = {
          age: 32,
          height: 180,
          weight: 75.0,
          body_fat: 12,
          stress_level: 6,
          sleep_hours: 6.5,
          training_days: 5,
          goal: "Ganar W/kg"
        };

        // Hacemos la llamada real a nuestra API
        const response = await fetch('/api/generate_plan', {
          method: 'POST', // ¡Muy importante que sea POST!
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(userProfile),
        });

        if (!response.ok) {
          // Si la respuesta del servidor no es exitosa (ej. error 500), lanzamos un error.
          const errorData = await response.json();
          throw new Error(errorData.detail || `Error del servidor: ${response.status}`);
        }

        const data = await response.json();
        setPlan(data);

      } catch (err: any) {
        console.error("Error al obtener el plan:", err);
        setError(`No se pudo cargar el plan. ${err.message}`);
      } finally {
        setLoading(false);
      }
    };

    fetchPlan();
  }, []); // Se ejecuta solo una vez cuando el componente se carga

  if (loading) return <Loader />;
  // Mostramos un mensaje de error si la llamada a la API falla
  if (error) return <p className="text-red-500 text-center font-bold">{error}</p>;
  if (!plan) return <p className="text-center">No se ha podido generar un plan.</p>;

  // El resto del componente para mostrar los datos sigue igual
  const todayPlan = plan.DetailedMealPlan[0];

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <div className="lg:col-span-2 space-y-6">
        <div className="bg-[#282828] p-6 rounded-lg">
          <h2 className="text-xl font-bold text-white mb-2">Resumen del Análisis</h2>
          <p className="text-gray-300">{plan.AnalysisSummary}</p>
        </div>
        {todayPlan && (
          <div>
            <h2 className="text-2xl font-bold text-white mb-4">{todayPlan.day}</h2>
            <div className="space-y-4">
              {todayPlan.meals.breakfast && <MealCard title="Desayuno" meal={todayPlan.meals.breakfast} />}
              {todayPlan.meals.lunch && <MealCard title="Almuerzo" meal={todayPlan.meals.lunch} />}
              {todayPlan.meals.dinner && <MealCard title="Cena" meal={todayPlan.meals.dinner} />}
            </div>
          </div>
        )}
      </div>
      <div className="space-y-6">
         <div className="bg-[#282828] p-6 rounded-lg">
           <h3 className="text-lg font-bold text-white mb-2">Estrategia Actual</h3>
           <p className="text-red-400 font-semibold">{plan.CurrentStrategy}</p>
         </div>
         <ActionButtons />
      </div>
    </div>
  );
};

export default Dashboard;