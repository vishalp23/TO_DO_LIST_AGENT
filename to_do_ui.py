import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI API client
client = OpenAI(api_key=os.getenv("API_KEY"))

# Configure the database
DATABASE_URL = "sqlite:///todo_list.db"
Base = declarative_base()
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

# Function to add a task
def add_task(task_description):
    task = Task(description=task_description)
    session.add(task)
    session.commit()
    return f"Task added: {task_description}"

# Function to view all tasks
def view_tasks():
    tasks = session.query(Task).all()
    return tasks

# Function to delete a task
def delete_task(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        return f"Task {task_id} deleted successfully!"
    return f"Task with ID {task_id} not found."

# Streamlit UI
st.set_page_config(page_title="AI To-Do List", page_icon="📝")
st.title("📝 AI-Powered To-Do List")
st.subheader("Manage your tasks effortlessly with AI.")

# Section: Display Tasks
st.subheader("📋 Your Current Tasks")
tasks = view_tasks()
if tasks:
    for task in tasks:
        st.markdown(f"**{task.id}. {task.description}**")
else:
    st.info("Your to-do list is empty!")

# AI Assistance
st.subheader("🤖 AI-Powered Assistance")
user_input = st.text_input("Ask AI to help manage your tasks (e.g., 'Add Buy groceries').")
if st.button("Ask AI"):
    if user_input.strip():
        # AI Prompt
        ai_prompt = f"""
        You are a to-do list assistant. The user said: "{user_input}".
        The current to-do list is stored in a database and includes the following tasks:
        {[{'id': t.id, 'description': t.description} for t in tasks]}.

        Your task is to:
        - Understand the user's intent (add, view, delete, update, prioritize, search, clear tasks).
        - Respond appropriately with the action to be performed.
        - Provide the response in the following format:
            - For adding: "ACTION: add task description"
            - For deleting: "ACTION: delete task_id"
            - For viewing: "ACTION: view"
            - For clearing: "ACTION: clear"
        """

        try:
            # Get AI response
            ai_response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for managing a to-do list."},
                    {"role": "user", "content": ai_prompt}
                ],
                max_tokens=500,
                temperature=0.5
            ).choices[0].message.content.strip()

            # Process AI Response
            if "ACTION: add" in ai_response:
                # Extract task description
                task_to_add = ai_response.split("ACTION: add")[1].strip()
                result = add_task(task_to_add)
                st.success(result)
                st.rerun()
            elif "ACTION: delete" in ai_response:
                # Extract task ID to delete
                try:
                    task_id_to_delete = int(ai_response.split("ACTION: delete")[1].strip())
                    result = delete_task(task_id_to_delete)
                    st.success(result)
                    st.rerun()
                except ValueError:
                    st.error("AI provided an invalid task ID to delete.")
            elif "ACTION: view" in ai_response:
                # Display the current to-do list
                st.text("Your Current Tasks:")
                for task in tasks:
                    st.text(f"{task.id}. {task.description}")
            elif "ACTION: clear" in ai_response:
                # Clear all tasks
                session.query(Task).delete()
                session.commit()
                st.success("All tasks have been cleared.")
                st.rerun()
            else:
                st.error(f"AI Response: {ai_response}")
        except Exception as e:
            st.error(f"Error communicating with AI: {e}")
    else:
        st.error("Please enter a valid command for AI.")
