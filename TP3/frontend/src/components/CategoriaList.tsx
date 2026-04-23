import type { Categoria } from '../types/categoria'
import CategoriaCard from './CategoriaCard'

interface Props {
  categorias: Categoria[]
  onEdit: (categoria: Categoria) => void
  onDelete: (id: number) => void
}

export default function CategoriaList({ categorias, onEdit, onDelete }: Props) {
  if (categorias.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-20 text-gray-400">
        <svg
          className="w-16 h-16 mb-4 text-gray-300"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={1.5}
            d="M20 7H4a2 2 0 00-2 2v6a2 2 0 002 2h16a2 2 0 002-2V9a2 2 0 00-2-2zM4 7V5a2 2 0 012-2h12a2 2 0 012 2v2"
          />
        </svg>
        <p className="text-lg font-medium">No hay categorías todavía</p>
        <p className="text-sm">Hacé clic en "Nueva Categoría" para empezar</p>
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {categorias.map((cat) => (
        <CategoriaCard
          key={cat.id}
          categoria={cat}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  )
}
