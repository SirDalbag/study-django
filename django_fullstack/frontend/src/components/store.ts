import { configureStore } from "@reduxjs/toolkit";
import * as components from "./components";
import * as constants from "./constants";
export const store = configureStore({
  reducer: {
    // @ts-ignore
    books: components.constructorReducer(constants.books),
    // @ts-ignore
    book: components.constructorReducer(constants.book),
    // @ts-ignore
    bookCategories: components.constructorReducer(constants.bookCategories),
    // @ts-ignore
    booksCategory: components.constructorReducer(constants.booksCategory),
    // @ts-ignore
    categories: components.constructorReducer(constants.categories),
    // @ts-ignore
    category: components.constructorReducer(constants.category),
  },
});
export default store;