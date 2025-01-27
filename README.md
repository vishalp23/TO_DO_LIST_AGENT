# 📝 AI-Powered To-Do List

An interactive to-do list application powered by **Streamlit** and **OpenAI GPT-4**. This app allows users to manage their tasks effortlessly with natural language commands, utilizing AI to understand and execute actions like adding, deleting, and viewing tasks.

---

## 🚀 Features

- **AI-Powered Commands**: Use natural language to add, delete, view, or clear tasks.
- **Task Management**: Store tasks in an SQLite database for persistence.
- **Interactive UI**: A clean and intuitive user interface built with Streamlit.
- **Dynamic Task Updates**: Tasks update in real-time after AI processes your commands.

---

## 📂 Project Structure

```plaintext
.
├── app.py                 # Main Streamlit application
├── todo_list.db           # SQLite database for tasks
├── .env                   # Environment variables (e.g., OpenAI API key)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/vishalp23/TO_DO_LIST_AGENT.git
cd TO_DO_LIST_AGENT
```

### 2. **Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Set Up Environment Variables**
Create a `.env` file in the root directory with the following content:
```plaintext
API_KEY=your_openai_api_key
```
Replace `your_openai_api_key` with your OpenAI API key.

### 5. **Run the Application**
```bash
streamlit run app.py
```

### 6. **Open in Browser**
Visit the URL shown in your terminal, typically [http://localhost:8501](http://localhost:8501).

---

## 🧠 How to Use

1. **View Tasks**: The app automatically displays all your current tasks.
2. **Ask AI for Help**:
   - Use the input field under **"AI-Powered Assistance"** to type commands like:
     - `"Add Buy groceries"`
     - `"Delete task 1"`
     - `"Clear all tasks"`
   - AI will process the command and update the task list.
3. **AI Response**: The app will confirm the action (e.g., "Task added" or "Task deleted").

---

## ⚙️ Key Functionalities

- **Add a Task**: Type natural language commands like `"Add 'Finish homework'"`.
- **Delete a Task**: Use commands like `"Delete task 2"`.
- **Clear All Tasks**: Use `"Clear all tasks"` to reset the list.
- **View Tasks**: AI will display your current tasks with `"Show my tasks"`.

---

## 📦 Dependencies

- **Python 3.8+**
- **Streamlit**: For the user interface.
- **OpenAI**: For GPT-4-powered natural language processing.
- **SQLAlchemy**: For managing tasks in an SQLite database.
- **dotenv**: For handling environment variables.

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## 🛡️ Security Notes

1. **Environment Variables**:
   - Store sensitive API keys in the `.env` file, and ensure it is included in `.gitignore`.
2. **GitHub Push Protection**:
   - The `.env` file is excluded from version control to prevent accidental exposure of secrets.

---

## ✨ Future Enhancements

- **Priority Levels**: Allow users to set task priorities (e.g., High, Medium, Low).
- **Task Deadlines**: Add due dates for tasks.
- **Search Functionality**: Enable searching tasks by keywords.
- **Reminders**: Integrate a notification system for upcoming deadlines.

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them:
   ```bash
   git push origin feature-name
   ```
4. Open a Pull Request.

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📧 Contact

For questions or suggestions, feel free to contact [vishalp23](https://github.com/vishalp23).

---
