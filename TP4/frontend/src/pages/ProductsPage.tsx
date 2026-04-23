import { useState, useEffect } from "react";
import type { Producto } from "../types/producto";

const API_URL = "http://localhost:8000/productos";

export default function ProductsPage() {
  const [productos, setProductos] = useState<Producto[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchProductos();
  }, []);

  async function fetchProductos() {
    try {
      const response = await fetch(`${API_URL}/`);
      if (!response.ok) throw new Error("Error al cargar los productos");
      const data: Producto[] = await response.json();
      setProductos(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error desconocido");
    }
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Productos</h1>
      </div>

      {error && (
        <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-600 rounded-xl text-sm">
          {error}
          <button
            onClick={() => setError(null)}
            className="ml-2 font-bold cursor-pointer"
          >
            ✕
          </button>
        </div>
      )}

      {productos.length === 0 ? (
        <p className="text-center text-gray-400 py-12">
          No hay productos. Podés crearlos desde el archivo <code className="bg-gray-100 px-1 rounded">.http</code>.
        </p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {productos.map((producto) => (
            <div
              key={producto.id}
              className="bg-white rounded-2xl shadow-md p-5 hover:shadow-lg transition-shadow duration-200"
            >
              <h3 className="text-lg font-semibold text-gray-800">{producto.nombre}</h3>
              <p className="text-gray-500 text-sm mt-1">{producto.descripcion}</p>
              <div className="mt-3 flex items-center justify-between">
                <span className="text-blue-600 font-semibold">
                  ${producto.precio_base.toFixed(2)}
                </span>
                <span
                  className={`text-xs px-2 py-1 rounded-full font-medium ${
                    producto.disponible
                      ? "bg-green-100 text-green-600"
                      : "bg-red-100 text-red-500"
                  }`}
                >
                  {producto.disponible ? "Disponible" : "No disponible"}
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
