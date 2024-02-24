import { useState } from "react";
import axios from "axios";
import * as bases from "../components/bases";
import Categories from "../components/categories";

const categories = [
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
  const [searchValue, setSearchValue] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  const handleSearchSubmit = async (e: any) => {
    e.preventDefault();

    try {
      const url = "http://127.0.0.1:8000/api/";
      const response = await axios.post(url, { search: searchValue });
      setSearchResults(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <bases.Base>
      <div className="flex flex-col gap-8 items-center p-4">
        <form onSubmit={handleSearchSubmit}>
          <div className="relative mt-2 rounded-md shadow-sm">
            <input
              type="text"
              name="search"
              id="search"
              className="block w-[500px] rounded-md border-0 py-4 pl-4 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600"
              placeholder="Книги, авторы, жанры"
              value={searchValue}
              onChange={(e) => setSearchValue(e.target.value)}
            />
          </div>
        </form>
        <div className="w-2/4 flex flex-col gap-4 items-center justify-center">
          <p className="font-semibold text-xl">Категории</p>
          <Categories content={categories} className={"justify-center"} />
        </div>
      </div>
    </bases.Base>
  );
}
