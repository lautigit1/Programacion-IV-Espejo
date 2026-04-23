import type { Producto } from '../types/producto'

interface Props {
  producto: Producto
  onEdit: (producto: Producto) => void
  onDelete: (id: number) => void
}

export default function ProductoCard({ producto, onEdit, onDelete }: Props) {
  const primeraImagen = producto.imagen_url[0] ?? null

  return (
    <div className="bg-white rounded-2xl shadow-md overflow-hidden flex flex-col gap-0 hover:shadow-lg transition-shadow duration-200">
      {/* Imagen */}
      {primeraImagen ? (
        <img
          src={primeraImagen}
          alt={producto.nombre}
          className="w-full h-40 object-cover"
          onError={(e) => {
            e.currentTarget.src =
              'https://placehold.co/400x160/e5e7eb/9ca3af?text=Sin+imagen'
          }}
        />
      ) : (
        <div className="w-full h-40 bg-gray-100 flex items-center justify-center text-gray-400 text-sm">
          Sin imagen
        </div>
      )}

      <div className="p-4 flex flex-col gap-3">
      <div className="flex justify-between items-start">
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2">
            <h2 className="text-lg font-semibold text-gray-800 truncate">
              {producto.nombre}
            </h2>
            <span
              className={`text-xs font-medium rounded-full px-2 py-0.5 shrink-0 ${
                producto.disponible
                  ? 'bg-green-100 text-green-700'
                  : 'bg-gray-100 text-gray-500'
              }`}
            >
              {producto.disponible ? 'Disponible' : 'No disponible'}
            </span>
          </div>
          <p className="text-sm text-gray-500 mt-1 line-clamp-2">
            {producto.descripcion}
          </p>
        </div>
        <span className="ml-2 text-xs font-medium bg-gray-100 text-gray-500 rounded-full px-2 py-0.5 shrink-0">
          #{producto.id}
        </span>
      </div>

      <div className="text-blue-600 font-semibold text-sm">
        ${producto.precio_base.toFixed(2)}
      </div>

      <div className="flex gap-2 pt-1">
        <button
          onClick={() => onEdit(producto)}
          className="flex-1 bg-yellow-400 hover:bg-yellow-500 text-black rounded-xl px-4 py-2 font-medium text-sm transition-colors duration-150 cursor-pointer"
        >
          Editar
        </button>
        <button
          onClick={() => onDelete(producto.id)}
          className="flex-1 bg-red-500 hover:bg-red-600 text-white rounded-xl px-4 py-2 font-medium text-sm transition-colors duration-150 cursor-pointer"
        >
          Eliminar
        </button>
      </div>
      </div>
    </div>
  )
}
