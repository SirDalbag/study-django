import React, { useState } from "react";
import axios from "axios";
import * as bases from "../components/bases";

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
      <div className="flex flex-col gap-3 items-center p-4">
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
        <div>
          <h1>{(searchResults as any).message}</h1>
        </div>
      </div>
    </bases.Base>
  );
}
