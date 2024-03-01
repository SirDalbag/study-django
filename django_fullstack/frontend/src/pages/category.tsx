import { Link, useParams } from "react-router-dom";
import { useConstructor } from "../components/hooks";
import * as constants from "../components/constants";
import * as bases from "../components/bases";
import Carousel from "../components/carousel";

export default function Page() {
  const { slug } = useParams();
  const category: any = useConstructor(
    constants.category,
    "category",
    `${constants.host}/api/category/${slug}/`
  );
  const books = useConstructor(
    constants.booksCategory,
    "booksCategory",
    `${constants.host}/api/books/${slug}/`
  );
  console.log(category);
  return (
    <bases.Base>
      <div className="container mx-auto px-32 py-12">
        <div className="flex flex-col gap-8">
          <p className="font-semibold text-5xl tracking-wide">
            Книги в жанре «{category?.name}»
          </p>
          <Carousel content={books} />
        </div>
      </div>
    </bases.Base>
  );
}
