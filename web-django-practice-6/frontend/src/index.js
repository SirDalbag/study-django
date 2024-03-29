import React, {useState, useEffect} from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import axios from 'axios';

function App() {
  const [persons, setPersons] = useState([])
  const [categories, setCategories] = useState([])
  const [clothes, setClothes] = useState([])
  const [currentData, setCurrentData] = useState({tabel_num: 0, categories_id: 0, clothes:0 ,person_fio: ""})
  
  async function getPersons() {
    const response = await axios.get("http://127.0.0.1:8000/api/persons/")
    setPersons(response.data.data)
  }

  async function getCategories() {
    const response = await axios.get("http://127.0.0.1:8000/api/categories/")
    setCategories(response.data.data)
  }

  useEffect(() => {
    getPersons()
    getCategories()
  }, [])

  useEffect(() => {
    console.log(currentData)
  }, [currentData])

  function handlePerson(e) {
    const selectedTabelNum = parseInt(e.target.value)
    const filteredPerson = persons.filter((element) => element.tabel_num == selectedTabelNum)
    setCurrentData({...currentData, tabel_num: selectedTabelNum, person_fio: filteredPerson.length != 0 ? filteredPerson[0].last_name : ""})
  }

  async function handleCategories(e) {
    const selectedCategoriesId = e.target.value
    setCurrentData({...currentData, categories_id: selectedCategoriesId})
    if (selectedCategoriesId != "") {
      const response = await axios.get(`http://127.0.0.1:8000/api/clothes/?filter={"id":${selectedCategoriesId}}`)
      setClothes(response.data.data)

    } else {
      setClothes([])
    }
    setCurrentData({...currentData, categories_id: selectedCategoriesId, clothes: 0})
  }

  async function handleClothes(e) {
    const selectedClothes = parseInt(e.target.value)
    setCurrentData({...currentData, clothes: selectedClothes})
  }

  async function postData() {
    const response = await axios.post(`http://127.0.0.1:8000/api/post/`, {tabel_num: currentData.tabel_num, clothes: currentData.clothes})
  }
  

  return <main>
    <select onChange={handlePerson} required>
      <option value="" selected>Сотрудник</option>
      {persons.map((person) => (
        <option key={person.tabel_num} value={person.tabel_num}>{person.tabel_num}</option>
      ))}
    </select>
    <input disabled value={currentData.person_fio}></input>
    <select onChange={handleCategories} value={currentData.categories_id} required>
      <option value="" selected>Категория одежды</option>
      {categories.map((category) => (
        <option key={category.id} value={category.id}>{category.title}</option>
      ))}
    </select>
    <select required onChange={handleClothes} value={currentData.clothes}>
      <option value="" selected>Одежда</option>
      {clothes.map((cloth) => (
        <option key={cloth.id} value={cloth.id}>{cloth.title}</option>
      ))}
    </select>
    <input type="submit" value="+" onClick={postData}></input>
  </main>
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  // <React.StrictMode>
  <App></App>
  // </React.StrictMode>
);
