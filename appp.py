import os
import streamlit as st

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            st.success(f"File '{filename}' created successfully.")
    except FileExistsError:        
        st.warning(f"File '{filename}' already exists.")
    except Exception as e:
        st.error('An error occurred!')

def view_all_files():
    files = os.listdir()
    if not files:
        st.warning('No files found!')
    else:
        st.write('Files in directory:')
        st.write(files)

def delete_file(filename):
    try:
        os.remove(filename)
        st.success(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        st.warning(f"File '{filename}' not found.")
    except Exception as e:
        st.error('An error occurred!')

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            st.write(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        st.warning(f"File '{filename}' doesn't exist.")
    except Exception as e:
        st.error('An error occurred!')

def edit_file(filename, content):
    try:
        with open(filename, 'a') as f:
            f.write(content + "\n")
            st.success(f"File '{filename}' edited successfully.")
    except FileNotFoundError:
        st.warning(f"File '{filename}' doesn't exist.")
    except Exception as e:
        st.error('An error occurred!')

def main():
    st.title('File Management System')

    option = st.selectbox('Select an action:', ['Create File', 'View All Files', 'Delete File', 'Read File', 'Edit File', 'Exit'])

    if option == 'Create File':
        filename = st.text_input('Enter file name to create:')
        if st.button('Create'):
            create_file(filename)

    elif option == 'View All Files':
        if st.button('View Files'):
            view_all_files()

    elif option == 'Delete File':
        filename = st.text_input('Enter file name to delete:')
        if st.button('Delete'):
            delete_file(filename)

    elif option == 'Read File':
        filename = st.text_input('Enter file name to read:')
        if st.button('Read'):
            read_file(filename)

    elif option == 'Edit File':
        filename = st.text_input('Enter file name to edit:')
        content = st.text_area('Enter content to append:')
        if st.button('Edit'):
            edit_file(filename, content)

    elif option == 'Exit':
        st.write('Closing the app...')

if __name__ == '__main__':
    main()
