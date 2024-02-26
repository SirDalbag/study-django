import * as bases from "../components/bases";
import { useBooks, useCategories } from "../components/hooks";
import Categories from "../components/categories";
import Carousel from "../components/carousel";

export default function Page() {
  const books = useBooks();
  const categories = useCategories();

  return (
    <bases.Base>
      <div className="container mx-auto px-32 py-12">
        <div className="flex flex-col gap-8">
          <p className="font-semibold text-5xl tracking-wide">Все комиксы</p>
          <Categories content={categories} />
          <Carousel content={books} />
        </div>
      </div>
    </bases.Base>
  );
}
