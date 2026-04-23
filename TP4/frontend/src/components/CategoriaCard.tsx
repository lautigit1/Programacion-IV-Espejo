import type { Categoria } from "../types/categoria";

interface Props {
  categoria: Categoria;
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
}

export default function CategoriaCard({ categoria, onEdit, onDelete }: Props) {
  return (
    <div className="bg-white rounded-2xl shadow-md p-5 flex flex-col gap-3 hover:shadow-lg transition-shadow duration-200">
      <div>
        <h3 className="text-lg font-semibold text-gray-800">{categoria.nombre}</h3>
        <p className="text-gray-500 text-sm mt-1">{categoria.descripcion}</p>
      </div>
      <div className="flex gap-2 mt-auto">
        <button
          onClick={() => onEdit(categoria)}
          className="flex-1 rounded-xl px-4 py-2 font-medium bg-yellow-400 hover:bg-yellow-500 text-white transition-colors duration-200 cursor-pointer"
        >
          Editar
        </button>
        <button
          onClick={() => onDelete(categoria.id)}
          className="flex-1 rounded-xl px-4 py-2 font-medium bg-red-500 hover:bg-red-600 text-white transition-colors duration-200 cursor-pointer"
        >
          Eliminar
        </button>
      </div>
    </div>
  );
}
