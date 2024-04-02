import React, {useState, useEffect} from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import axios from 'axios';

function App() {
  const [persons, setPersons] = useState([])
  const [categories, setCategories] = useState([])
  const [clothes, setClothes] = useState([])
  const [reports, setReports] = useState([])
  const [warning, setWarnings] = useState([])
  const [currentData, setCurrentData] = useState({tabel_num: 0, categories_id: 0, clothes:0 ,person_fio: ""})
  
  async function getPersons() {
    const response = await axios.get("http://127.0.0.1:8000/api/persons/")
    setPersons(response.data.data)
  }

  async function getCategories() {
    const response = await axios.get("http://127.0.0.1:8000/api/categories/")
    setCategories(response.data.data)
  }

  async function getReports() {
    const response = await axios.get("http://127.0.0.1:8000/api/report/")
    setReports(response.data.data)
  }

  async function getWarnings() {
    const response = await axios.get("http://127.0.0.1:8000/api/warning/")
    setWarnings(response.data.data)
  }

  useEffect(() => {
    getPersons()
    getCategories()
    getReports()
    getWarnings()
  }, [])

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
    if (currentData.tabel_num != 0 && currentData.clothes != 0) {
      const response = await axios.post(`http://127.0.0.1:8000/api/post/`, {tabel_num: currentData.tabel_num, clothes: currentData.clothes})
      getReports()
      getWarnings()
    }
  }
  

  return <main className="flex flex-col items-center py-2">
    <div className="border-b-2 py-4">
    <select className="border-4 border-gray-600 px-2 py-1" onChange={handlePerson} required>
      <option value="" selected>Сотрудник</option>
      {persons.map((person) => (
        <option key={person.tabel_num} value={person.tabel_num}>{person.tabel_num}</option>
      ))}
    </select>
    <input className="border-4 border-gray-600 mx-4 px-2 py-1 bg-gray-200" disabled value={currentData.person_fio}></input>
    <select className="border-4 border-gray-600 mx-4 px-2 py-1" onChange={handleCategories} value={currentData.categories_id} required>
      <option value="" selected>Категория одежды</option>
      {categories.map((category) => (
        <option key={category.id} value={category.id}>{category.title}</option>
      ))}
    </select>
    <select className="border-4 border-gray-600 mx-4 px-2 py-1" required onChange={handleClothes} value={currentData.clothes}>
      <option value="" selected>Одежда</option>
      {clothes.map((cloth) => (
        <option key={cloth.id} value={cloth.id}>{cloth.title}</option>
      ))}
    </select>
    <input className="border-4 border-gray-600 mx-4 px-2 py-1 hover:cursor-pointer" type="submit" value="+" onClick={postData}></input>
    </div>
    <ul className="pt-4 border-b-2 pb-4">
    {reports.map((report, index) => (
        <li key={index} className="py-2">
          <div className="grid grid-cols-4 gap-3 border-2 p-2">
            <p className="border-r-2">{report.tabel_num}</p>
            <p className="border-r-2">{report.last_name}</p>
            <p className="border-r-2">{report.cloth}</p>
            <p>{report.created_at.split("T")[0]} {report.created_at.split("T")[1].split(".")[0]}</p>
          </div>
        </li>
      ))}
    </ul>
    <ul className="pt-4">
    {warning.map((warning, index) => (
        <li key={index} className="py-2">
          <div className="grid grid-cols-4 gap-3 border-2 p-2">
            <p className="border-r-2">{warning.tabel_num}</p>
            <p className="border-r-2">{warning.last_name}</p>
            <p className="border-r-2">{warning.cloth}</p>
            <p>{warning.created_at.split("T")[0]} {warning.created_at.split("T")[1].split(".")[0]}</p>
          </div>
        </li>
      ))}
    </ul>
  </main>
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  // <React.StrictMode>
  <App></App>
  // </React.StrictMode>
);
