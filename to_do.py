import os
from dotenv import load_dotenv
from openai import OpenAI  # Ensure the OpenAI library is installed
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv("API_KEY"))

# Initialize the database
Base = declarative_base()
DATABASE_URL = "sqlite:///todo_list.db"  # SQLite database
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Define the Task model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)

# Create the tasks table
Base.metadata.create_all(engine)

# Function to interact with the LLM
def ask_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for navigating LinkedIn job applications."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

# Function to add a task to the database
def add_task(task_description):
    task = Task(description=task_description)
    session.add(task)
    session.commit()
    return f"Added: {task_description}"

# Function to view all tasks
def view_tasks():
    tasks = session.query(Task).all()
    if not tasks:
        return "Your to-do list is empty!"
    return "Your tasks:\n" + "\n".join(f"{task.id}. {task.description}" for task in tasks)

# Function to delete a task by ID
def delete_task(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        return f"Removed: {task.description}"
    else:
        return f"Task with ID '{task_id}' not found!"

# Main interaction loop
def chatbot():
    print("Hello! I'm your to-do list assistant. How can I help you?")
    
    while True:
        user_input = input("You: ")
        
        # Use the LLM to determine the intent and generate a response
        prompt = f"""
        You are a to-do list assistant. The user said: "{user_input}".
        The current to-do list is stored in a database.
        Your task is to:
        1. Detect if the user wants to add, view, or delete a task.
        2. Respond appropriately.
        3. If adding or deleting, return the task in the format "ACTION: add task" or "ACTION: delete ID".
        """
        
        llm_response = ask_llm(prompt)
        
        # Parse the LLM response
        if "ACTION: add" in llm_response:
            task = llm_response.split("ACTION: add")[1].strip()
            response = add_task(task)
        elif "ACTION: delete" in llm_response:
            task_id = llm_response.split("ACTION: delete")[1].strip()
            response = delete_task(task_id)
        elif "view" in llm_response.lower():
            response = view_tasks()
        else:
            response = llm_response  # Use the LLM's generated response
        
        print("Bot:", response)
        
        # Exit condition
        if "bye" in user_input.lower():
            print("Bot: Goodbye! Have a great day!")
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
