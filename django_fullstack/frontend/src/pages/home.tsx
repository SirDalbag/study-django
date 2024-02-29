import * as bases from "../components/bases";
import { useBooks, useCategories } from "../components/hooks";
import Categories from "../components/categories";
import Carousel from "../components/carousel";

import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import * as components from "../components/components";
import * as constants from "../components/constants";
import * as store from "../components/store";

export default function Page() {
  const dispatch = useDispatch();
  const books = useSelector((state: any) => state.books);

  async function getBooks() {
    if (!books.load) {
      components.constructorWebAction(
        dispatch,
        constants.books,
        `${constants.host}/api/books/`,
        "GET"
      );
    }
  }

  useEffect(() => {
    getBooks();
  }, []);

  useEffect(() => {
    console.log("books: ", books);
  }, [books]);
  // const books = useBooks();
  const categories = useCategories();

  return (
    <bases.Base>
      <div className="container mx-auto px-32 py-12">
        <div className="flex flex-col gap-8">
          <p className="font-semibold text-5xl tracking-wide">Все книги</p>
          <Categories content={categories} />
          {/* <Carousel content={books} /> */}
        </div>
      </div>
    </bases.Base>
  );
}
