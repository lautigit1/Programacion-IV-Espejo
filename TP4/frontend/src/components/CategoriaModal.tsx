import { useState, useEffect } from "react";
import type { Categoria } from "../types/categoria";

interface FormState {
  nombre: string;
  descripcion: string;
}

interface Props {
  categoria: Categoria | null; // null = modo crear
  onClose: () => void;
  onSave: (data: FormState) => void;
}

export default function CategoriaModal({ categoria, onClose, onSave }: Props) {
  const [form, setForm] = useState<FormState>({ nombre: "", descripcion: "" });

  useEffect(() => {
    if (categoria) {
      setForm({ nombre: categoria.nombre, descripcion: categoria.descripcion });
    } else {
      setForm({ nombre: "", descripcion: "" });
    }
  }, [categoria]);

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    onSave(form);
  }

  return (
    <div className="bg-black bg-opacity-40 fixed inset-0 flex items-center justify-center z-50">
      <div className="bg-white rounded-2xl p-6 shadow-lg w-full max-w-md mx-4">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">
          {categoria ? "Editar categoría" : "Nueva categoría"}
        </h2>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div>
            <label
              htmlFor="nombre"
              className="block text-sm font-medium text-gray-700 mb-1"
            >
              Nombre
            </label>
            <input
              id="nombre"
              type="text"
              value={form.nombre}
              onChange={(e) => setForm({ ...form, nombre: e.target.value })}
              required
              className="w-full border border-gray-300 rounded-xl px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
            />
          </div>

          <div>
            <label
              htmlFor="descripcion"
              className="block text-sm font-medium text-gray-700 mb-1"
            >
              Descripción
            </label>
            <textarea
              id="descripcion"
              value={form.descripcion}
              onChange={(e) => setForm({ ...form, descripcion: e.target.value })}
              required
              rows={3}
              className="w-full border border-gray-300 rounded-xl px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400 transition resize-none"
            />
          </div>

          <div className="flex gap-3 mt-2">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 rounded-xl px-4 py-2 font-medium border border-gray-300 text-gray-600 hover:bg-gray-50 transition-colors duration-200 cursor-pointer"
            >
              Cancelar
            </button>
            <button
              type="submit"
              className="flex-1 rounded-xl px-4 py-2 font-medium bg-blue-500 hover:bg-blue-600 text-white transition-colors duration-200 cursor-pointer"
            >
              Guardar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
