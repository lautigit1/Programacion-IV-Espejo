import type { Categoria } from '../types/categoria'

interface Props {
  categoria: Categoria
  onEdit: (categoria: Categoria) => void
  onDelete: (id: number) => void
}

export default function CategoriaCard({ categoria, onEdit, onDelete }: Props) {
  return (
    <div className="bg-white rounded-2xl shadow-md p-4 flex flex-col gap-3 hover:shadow-lg transition-shadow duration-200">
      <div className="flex justify-between items-start">
        <div className="flex-1 min-w-0">
          <h2 className="text-lg font-semibold text-gray-800 truncate">
            {categoria.nombre}
          </h2>
          <p className="text-sm text-gray-500 mt-1 line-clamp-2">
            {categoria.descripcion}
          </p>
        </div>
        <span className="ml-2 text-xs font-medium bg-gray-100 text-gray-500 rounded-full px-2 py-0.5 shrink-0">
          #{categoria.id}
        </span>
      </div>

      <div className="flex gap-2 pt-1">
        <button
          onClick={() => onEdit(categoria)}
          className="flex-1 bg-yellow-400 hover:bg-yellow-500 text-black rounded-xl px-4 py-2 font-medium text-sm transition-colors duration-150 cursor-pointer"
        >
          Editar
        </button>
        <button
          onClick={() => onDelete(categoria.id)}
          className="flex-1 bg-red-500 hover:bg-red-600 text-white rounded-xl px-4 py-2 font-medium text-sm transition-colors duration-150 cursor-pointer"
        >
          Eliminar
        </button>
      </div>
    </div>
  )
}
