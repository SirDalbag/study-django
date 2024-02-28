import { Link, useParams } from "react-router-dom";
import * as bases from "../components/bases";
import { useCategory, useBooksCategory } from "../components/hooks";
import Carousel from "../components/carousel";

export default function Page() {
  const { slug } = useParams();
  const category: any = useCategory(slug);
  const books = useBooksCategory(slug);
  console.log(books);
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
