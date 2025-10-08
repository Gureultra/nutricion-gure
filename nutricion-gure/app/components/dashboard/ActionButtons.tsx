const ActionButtons = () => {
  return (
    <div className="bg-[#282828] p-6 rounded-lg">
      <h3 className="text-lg font-bold text-white mb-4">Acciones del Plan</h3>
      <div className="space-y-3">
        <button className="w-full text-left bg-gray-700 hover:bg-red-500 text-white font-bold py-2 px-4 rounded transition-colors">
          Descargar Plan PDF
        </button>
        <button className="w-full text-left bg-gray-700 hover:bg-red-500 text-white font-bold py-2 px-4 rounded transition-colors">
          Enviar a mi Email
        </button>
        <button className="w-full text-left bg-gray-700 hover:bg-red-500 text-white font-bold py-2 px-4 rounded transition-colors">
          Reportar un ajuste
        </button>
      </div>
    </div>
  );
};

export default ActionButtons;