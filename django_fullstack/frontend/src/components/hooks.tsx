import { useState, useEffect } from "react";
import axios from "axios";

const useBooks = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/books/");
        setBooks(response.data.message);
      } catch (error) {
        console.error("Error fetching books:", error);
      }
    };

    fetchData();
  }, []);

  return books;
};

const useBook = (id: string | undefined) => {
  const [book, setBook] = useState(null);

  useEffect(() => {
    const fetchBook = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/book/${id}/`
        );
        setBook(response.data.message);
        console.log(response.data.message);
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

export { useBooks, useBook, useCategories };
