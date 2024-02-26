import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../pages/home";
import Audio from "../pages/audio";
import Comics from "../pages/comics";
import Kids from "../pages/kids";
import MyBooks from "../pages/my-books";
import Book from "../pages/book";
import Category from "../pages/category";
import Search from "../pages/search";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"*"} element={<Home />}></Route>
        <Route path={""} element={<Home />}></Route>
        <Route path={"/audio"} element={<Audio />}></Route>
        <Route path={"/comics"} element={<Comics />}></Route>
        <Route path={"/kids"} element={<Kids />}></Route>
        <Route path={"/my-books"} element={<MyBooks />}></Route>\
        <Route path={"/book/:id"} element={<Book />}></Route>
        <Route path={"/category/:slug"} element={<Category />}></Route>
        <Route path={"/search"} element={<Search />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
