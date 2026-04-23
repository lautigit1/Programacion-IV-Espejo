import { useState, useEffect } from "react";
import type { Categoria } from "../types/categoria";
import CategoriaList from "../components/CategoriaList";
import CategoriaModal from "../components/CategoriaModal";

const API_URL = "http://localhost:8000/categorias";

interface FormData {
  nombre: string;
  descripcion: string;
}

export default function CategoriasPage() {
  const [categorias, setCategorias] = useState<Categoria[]>([]);
  const [modalAbierto, setModalAbierto] = useState(false);
  const [categoriaEditando, setCategoriaEditando] = useState<Categoria | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchCategorias();
  }, []);

  async function fetchCategorias() {
    try {
      const response = await fetch(`${API_URL}/`);
      if (!response.ok) throw new Error("Error al cargar las categorías");
      const data: Categoria[] = await response.json();
      setCategorias(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error desconocido");
    }
  }

  async function handleGuardar(formData: FormData) {
    try {
      if (categoriaEditando) {
        const response = await fetch(`${API_URL}/${categoriaEditando.id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(formData),
        });
        if (!response.ok) throw new Error("Error al actualizar la categoría");
      } else {
        const response = await fetch(`${API_URL}/`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(formData),
        });
        if (!response.ok) throw new Error("Error al crear la categoría");
      }
      await fetchCategorias();
      cerrarModal();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error desconocido");
    }
  }

  async function handleEliminar(id: number) {
    try {
      const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
      if (!response.ok) throw new Error("Error al eliminar la categoría");
      await fetchCategorias();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error desconocido");
    }
  }

  function abrirModalCrear() {
    setCategoriaEditando(null);
    setModalAbierto(true);
  }

  function abrirModalEditar(categoria: Categoria) {
    setCategoriaEditando(categoria);
    setModalAbierto(true);
  }

  function cerrarModal() {
    setModalAbierto(false);
    setCategoriaEditando(null);
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-gray-800">Categorías</h1>
        <button
          onClick={abrirModalCrear}
          className="rounded-xl px-4 py-2 font-medium bg-blue-500 hover:bg-blue-600 text-white transition-colors duration-200 cursor-pointer"
        >
          + Nueva categoría
        </button>
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

      <CategoriaList
        categorias={categorias}
        onEdit={abrirModalEditar}
        onDelete={handleEliminar}
      />

      {modalAbierto && (
        <CategoriaModal
          categoria={categoriaEditando}
          onClose={cerrarModal}
          onSave={handleGuardar}
        />
      )}
    </div>
  );
}
