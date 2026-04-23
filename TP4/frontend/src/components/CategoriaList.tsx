import type { Categoria } from "../types/categoria";
import CategoriaCard from "./CategoriaCard";

interface Props {
  categorias: Categoria[];
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
}

export default function CategoriaList({ categorias, onEdit, onDelete }: Props) {
  if (categorias.length === 0) {
    return (
      <p className="text-center text-gray-400 py-12">
        No hay categorías aún. ¡Creá la primera!
      </p>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {categorias.map((categoria) => (
        <CategoriaCard
          key={categoria.id}
          categoria={categoria}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}
