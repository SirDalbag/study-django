import { Link } from "react-router-dom";
import * as bases from "../components/bases";

const category = [
  { id: 1, name: "САМОРАЗВИТИЕ", slug: "/books/self-development" },
  { id: 2, name: "ФАНТАСТИКА", slug: "/books/fiction" },
  { id: 3, name: "РОМАНТИКА", slug: "/books/romance" },
  { id: 4, name: "ПСИХОЛОГИЯ", slug: "/books/psychology" },
  { id: 5, name: "ДЕТЕКТИВЫ", slug: "/books/detectives" },
  { id: 6, name: "ПРОЗА", slug: "/books/prose" },
  { id: 7, name: "ТРИЛЛЕРЫ И ХОРРОРЫ", slug: "/books/thrillers-and-horror" },
  { id: 8, name: "ФЭНТЕЗИ", slug: "/books/fantasy" },
  { id: 9, name: "НОН-ФИКШН", slug: "/books/non-fiction" },
  { id: 10, name: "КЛАССИКА", slug: "/books/classic" },
  { id: 11, name: "YOUNG ADULT", slug: "/books/young-adult" },
  { id: 12, name: "БИЗНЕС", slug: "/books/business" },
  { id: 13, name: "ИСТОРИЯ", slug: "/books/history" },
  { id: 14, name: "ЗДОРОВЬЕ", slug: "/books/health" },
  {
    id: 15,
    name: "БИОГРАФИИ И МЕМУАРЫ",
    slug: "/books/biographies-and-memoirs",
  },
];

export default function Page() {
  return (
    <bases.Base>
      <div className="container mx-auto px-32 py-12">
        <div className="flex flex-col gap-8">
          <p className="font-semibold text-5xl tracking-wide">Все книги</p>
          <div className="flex flex-wrap gap-2">
            {category.map((item) => (
              <Link to={item.slug} key={item.id}>
                <p className="tracking-wide border-2 rounded-full py-1 px-2.5 bg-white hover:border-blue-600 hover:text-blue-600">
                  {item.name}
                </p>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </bases.Base>
  );
}
