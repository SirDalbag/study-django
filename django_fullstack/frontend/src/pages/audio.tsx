import * as bases from "../components/bases";
import { useConstructor } from "../components/hooks";
import * as constants from "../components/constants";
import Categories from "../components/categories";
import Carousel from "../components/carousel";

export default function Page() {
  const books = useConstructor(
    constants.books,
    "books",
    `${constants.host}/api/books/`
  );
  const categories = useConstructor(
    constants.categories,
    "categories",
    `${constants.host}/api/categories/`
  );

  return (
    <bases.Base>
      <div className="container mx-auto px-32 py-12">
        <div className="flex flex-col gap-8">
          <p className="font-semibold text-5xl tracking-wide">Все аудиокниги</p>
          <Categories content={categories} />
          <Carousel content={books} />
        </div>
      </div>
    </bases.Base>
  );
}
