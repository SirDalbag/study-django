import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import axios from "axios";

function App() {
  const [users, setUsers] = useState([]);
  const [editingUser, setEditingUser] = useState(null);
  const [deletingUser, setDeletingUser] = useState(null);

  async function getUsers() {
    const response = await axios.get("http://127.0.0.1:8000/api/users/");
    setUsers(response.data.data);
  }

  useEffect(() => {
    getUsers()
  }, [])

  const [isOpen, setIsOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);

  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    age: ''
  });

  const openModal = () => {
    setIsOpen(true);
  };

  const openEditModal = (user) => {
    setEditingUser(user);
    setFormData({
      first_name: user.first_name,
      last_name: user.last_name,
      age: user.age
    });
    setIsOpen(true);
  };

  const closeModal = () => {
    setIsOpen(false);
    setIsDeleteModalOpen(false);
    setFormData({
      first_name: '',
      last_name: '',
      age: ''
    });
    setEditingUser(null);
    setDeletingUser(null);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleDelete = async () => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/user/delete/${deletingUser.user_id}`);
      getUsers();
      closeModal();
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  const handleDeleteModalOpen = (user) => {
    setDeletingUser(user);
    setIsDeleteModalOpen(true);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      if (editingUser) {
        await axios.put(`http://127.0.0.1:8000/api/user/edit/${editingUser.user_id}`, formData);
      } else {
        await axios.post('http://127.0.0.1:8000/api/user/add/', formData);
      }
      getUsers();
      closeModal();
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };

  return <div className="flex justify-center">
    <ul role="list" className="divide-y divide-gray-100">
      <li className="flex justify-center my-2">
        <button
          type="button"
          className="inline-flex justify-center w-full rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
          onClick={openModal}
        >
          ADD
        </button>
      </li>
      {users.map((user) => (
        <li key={user.user_id} className="flex items-center justify-between gap-x-6 py-5 border-b">
          <div className="flex min-w-0 gap-x-4">
            <div className="min-w-0 flex-auto">
              <p className="text-sm font-semibold leading-6 text-gray-900">{user.first_name} {user.last_name}<span className="mx-3 truncate text-xs leading-5 text-gray-500">{user.age}</span></p>
            </div>
          </div>
          <div className="hidden shrink-0 sm:flex sm:flex-row sm:items-end gap-3">
            <button
              type="button"
              className="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
              onClick={() => openEditModal(user)}
            >
              EDIT
            </button>
            <button
              type="button"
              className="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
              onClick={() => handleDeleteModalOpen(user)}
            >
              DELETE
            </button>
          </div>
        </li>
      ))}
    </ul>
    {isOpen && (
      <div className="fixed z-10 inset-0 overflow-y-auto">
        <div className="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div className="fixed inset-0 transition-opacity" aria-hidden="true">
            <div className="absolute inset-0 bg-gray-500 opacity-75"></div>
          </div>
          <span className="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
          <div className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <div className="sm:flex sm:items-start">
                <h3 className="text-lg leading-6 font-medium text-gray-900 mb-2">{editingUser ? 'EDIT USER' : 'NEW USER'}</h3>
              </div>
              <form onSubmit={handleSubmit}>
                <div className="mt-2">
                  <input
                    type="text"
                    name="first_name"
                    className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                    placeholder="First Name"
                    value={formData.first_name}
                    onChange={handleInputChange}
                  />
                </div>
                <div className="mt-2">
                  <input
                    type="text"
                    name="last_name"
                    className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                    placeholder="Last Name"
                    value={formData.last_name}
                    onChange={handleInputChange}
                  />
                </div>
                <div className="mt-2">
                  <input
                    type="number"
                    name="age"
                    className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                    placeholder="Age"
                    value={formData.age}
                    onChange={handleInputChange}
                  />
                </div>
                <div className="mt-4">
                  <button
                    type="submit"
                    className="inline-flex justify-center w-full rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                  >
                    SAVE
                  </button>
                </div>
                <div className="mt-4">
                  <button
                    type="button"
                    className="inline-flex justify-center w-full rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                    onClick={closeModal}
                  >
                    CANCEL
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    )}
    {isDeleteModalOpen && (
      <div className="fixed z-10 inset-0 overflow-y-auto">
        <div className="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div className="fixed inset-0 transition-opacity" aria-hidden="true">
            <div className="absolute inset-0 bg-gray-500 opacity-75"></div>
          </div>
          <span className="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
          <div className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <div className="sm:flex sm:items-start">
                <h3 className="text-lg leading-6 font-medium text-gray-900 mb-2">DELETE USER</h3>
              </div>
              <p className="text-sm text-gray-600 mb-4">Are you sure you want to delete <span className="font-bold">{deletingUser && `${deletingUser.first_name} ${deletingUser.last_name}`}</span>?</p>
              <div className="mt-4">
                <button
                  type="button"
                  className="inline-flex justify-center w-full rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                  onClick={handleDelete}
                >
                  DELETE
                </button>
              </div>
              <div className="mt-4">
                <button
                  type="button"
                  className="inline-flex justify-center w-full rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                  onClick={closeModal}
                >
                  CANCEL
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    )}
  </div>
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App></App>);
