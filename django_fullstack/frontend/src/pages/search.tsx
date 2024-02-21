import React, { useState } from "react";
import axios from "axios";
import * as bases from "../components/bases";

export default function Page() {
  const [searchValue, setSearchValue] = useState("");

  const handleSearchSubmit = async (e: any) => {
    e.preventDefault();

    try {
      const url = "http://127.0.0.1:8000/api/";
      const response = await axios.post(url, { search: searchValue });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <bases.Base>
      <div className="flex justify-center p-4">
        <form onSubmit={handleSearchSubmit}>
          <div className="relative mt-2 rounded-md shadow-sm">
            <input
              type="text"
              name="search"
              id="search"
              className="block w-[500px] rounded-md border-0 py-4 pl-4 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600"
              placeholder="Книги, авторы, жанры"
            />
          </div>
        </form>
      </div>
    </bases.Base>
  );
}
