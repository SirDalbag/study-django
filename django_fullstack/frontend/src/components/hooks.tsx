import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as components from "../components/components";
import * as constants from "../components/constants";
import * as store from "../components/store";
import axios from "axios";

const useBooks = () => {
  const dispatch = useDispatch();
  const books = useSelector((state: any) => state.bookList);

  useEffect(() => {
    if (!books?.load) {
      components.constructorWebAction(
        dispatch,
        constants.books,
        `http://127.0.0.1:8000/api/books/`,
        "GET"
      );
    }
  }, [books?.load, dispatch]);
  console.log(books?.data);
  return books?.data;
};

export default useBooks;

const useBook = (id: string | undefined) => {
  const [book, setBook] = useState(null);

  useEffect(() => {
    const fetchBook = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/book/${id}/`
        );
        setBook(response.data.message[0]);
      } catch (error) {
        console.error(`Error fetching book with ID ${id}:`, error);
        setBook(null);
      }
    };

    if (id) {
      fetchBook();
    }
  }, [id]);

  return book;
};

const useBookCategories = (ids: any) => {
  const [bookCategories, setBookCategories] = useState(null);

  useEffect(() => {
    const fetchBook = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/book-categories/?${
            ids ? ids.map((id: any) => `category=${id}`).join("&") : ""
          }`
        );
        setBookCategories(response.data.message);
      } catch (error) {
        console.error(`Error fetching categories with IDS ${ids}:`, error);
        setBookCategories(null);
      }
    };

    if (ids) {
      fetchBook();
    }
  }, [ids]);

  return bookCategories;
};

const useBooksCategory = (slug: any) => {
  const [booksCategory, setBooksCategory] = useState(null);

  useEffect(() => {
    const fetchBook = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/books/${slug}/`
        );
        setBooksCategory(response.data.message);
      } catch (error) {
        console.error(`Error fetching books with slug ${slug}:`, error);
        setBooksCategory(null);
      }
    };

    if (slug) {
      fetchBook();
    }
  }, [slug]);

  return booksCategory;
};

const useCategories = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/categories/"
        );
        setCategories(response.data.message);
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    };

    fetchData();
  }, []);

  return categories;
};

const useCategory = (identifier: any) => {
  const [category, setCategory] = useState(null);

  useEffect(() => {
    const fetchBook = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/category/${identifier}/`
        );
        setCategory(response.data.message[0]);
      } catch (error) {
        console.error(`Error fetching book with ID ${identifier}:`, error);
        setCategory(null);
      }
    };

    if (identifier) {
      fetchBook();
    }
  }, [identifier]);

  return category;
};

export {
  useBooks,
  useBook,
  useBookCategories,
  useBooksCategory,
  useCategories,
  useCategory,
};
