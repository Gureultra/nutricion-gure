interface MealCardProps {
  title: string;
  meal: {
    meal: string;
    function: string;
  };
}

const MealCard = ({ title, meal }: MealCardProps) => {
  return (
    <div className="bg-[#282828] p-4 rounded-lg border border-transparent hover:border-red-500 transition-colors">
      <h3 className="font-bold text-white">{title}</h3>
      <p className="text-gray-300">{meal.meal}</p>
      <p className="text-xs text-gray-400 mt-2">{meal.function}</p>
    </div>
  );
};

export default MealCard;