import streamlit as st

# Initialize the task list in session state if it doesn't exist
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Task Management System Function
def task():
    st.title("📝 Task Management System")
    
    # Input for the total number of tasks (only for initial entry)
    total_tasks = st.number_input("How many tasks do you want to add? 🔢", min_value=1, step=1, key="total_tasks")
    
    for i in range(1, total_tasks + 1):
        task_name = st.text_input(f"Enter task {i} 🗒️", key=f"task_{i}")
        if task_name and task_name not in st.session_state.tasks:
            st.session_state.tasks.append(task_name)
    
    if st.button("👀 View Today's Tasks"):
        st.write(f"Today's tasks are: {st.session_state.tasks}")
    
    # Add Task
    add = st.text_input("Enter task to add 🆕", key="add_task")
    if st.button("➕ Add Task"):
        if add and add not in st.session_state.tasks:
            st.session_state.tasks.append(add)
            st.success(f"✅ Task '{add}' added successfully!")
    
    # Update Task
    updated_val = st.text_input("Enter task to update 🔄", key="update_task")
    if st.button("✏️ Update Task"):
        if updated_val in st.session_state.tasks:
            new_task = st.text_input("Enter new task 📝", key="new_task")
            ind = st.session_state.tasks.index(updated_val)
            if new_task:
                st.session_state.tasks[ind] = new_task
                st.success(f"🔄 Task updated successfully to: {new_task}")
    
    # Delete Task
    del_val = st.text_input("Enter task to delete ❌", key="delete_task")
    if st.button("🗑️ Delete Task"):
        if del_val in st.session_state.tasks:
            st.session_state.tasks.remove(del_val)
            st.success(f"❌ Task '{del_val}' deleted successfully.")
    
    # View All Tasks
    if st.button("📋 View All Tasks"):
        st.write(f"All tasks: {st.session_state.tasks}")
    
    if st.button("🚪 Exit"):
        st.write("Closing the program...")

# Run the task management system
if __name__ == "__main__":
    task()

# this code to check the output in streamlit
# bash command: streamlit run to_do.py