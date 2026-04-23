import type { Producto } from '../types/producto'
import ProductoCard from './ProductoCard'

interface Props {
  productos: Producto[]
  onEdit: (producto: Producto) => void
  onDelete: (id: number) => void
}

export default function ProductoList({ productos, onEdit, onDelete }: Props) {
  if (productos.length === 0) {
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
            d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
          />
        </svg>
        <p className="text-lg font-medium">No hay productos todavía</p>
        <p className="text-sm">Hacé clic en "Nuevo Producto" para empezar</p>
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {productos.map((prod) => (
        <ProductoCard
          key={prod.id}
          producto={prod}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  )
}
