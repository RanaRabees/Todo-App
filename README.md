# Todo App

This is simple Todo API Project implemented using FastAPI, SQLAlchemy and Streamlit. It provides basic functionality for managing tasks, allowing you to perform operations such as retrieving tasks (GET), adding new tasks (POST), and deleting tasks (DELETE).

## Installation

Make sure you have the necessary packages installed using pip.
You can install them with the following command:

#### FastAPI

```bash
pip install fastapi
```

#### SqlAlchemy

```bash
pip install sqlalchemy
```

#### StreamLit

```bash
pip install streamlit
```

#### Pytest

```bash
pip install pytest
```

#### Uvicorn

```bash
pip install uvicorn
```

#### Psycopg2

```bash
pip install psycopg2
```

#### Pydantic

```bash
pip install pydantic
```

#### Typing

```bash
pip install typing
```

## Setup

### 1. **Set up PostgreSQL Database:**

- Create a database named `todo_app` (or your preferred name).
  - Create a Table named `Tasks` (or your preferred name).
  - Create a folder named `.steamlit` in this folder now create two files First `.gitignore` Second `secrets.toml`
  - In .gitignore File Paste This Code
    ``` secrets.toml ```
  - In secrets.toml File Paste This Code
    ``` SQLALCHEMY_DATABASE_URL = "Your Neon Database Connection String" ```
  - Also you can add SQLALCHEMY_DATABASE_URL in database.py with your database credentials.
  - Now you can run the project.

### 2. **Run the FastAPI application using uvicorn**

```bash
uvicorn main:app --reload
```

### 3. **Run the Streamlit client using the following command**

```bash
streamlit run streamlit_client.py
```

## API Endpoints

### Get All Todos

- **URL:** `/todos`
- **Method:** GET
- **Description:** Retrieve a list of all tasks.

### Add New Todos

- **URL:** `/todos`
- **Method:** POST
- **Description:** Add a new task to the list.
- **Request Body:**

  ```json
  {
    "id": "Todo Id",
    "title": "Todo Title",
    "description": "Todo Description"
  }
  ```

### Delete Task

- **URL:** `/todos/{todos_id}`
- **Method:** DELETE
- **Description:** Delete a task by providing its ID in the URL.

## **Contributing:**

Feel free to customize the project to meet your specific requirements or extend its functionality
We appreciate your interest in contributing to this project! By working together, we can make this Todo REST API even more versatile and valuable for the community.
If you want to contribute you can fork this repository and contribute with pull requests for improvements, new features, or bug fixes. Make sure to follow the coding style and document your changes properly.
We welcome contributions to this project! Here's a quick guide:

#### 1. **Fork the repository:** Create a copy of this repository under your GitHub account

#### 2. **Clone the forked repository:**

   ```bash
   git clone https://github.com/RanaRabees/Todo-API-Project.git
   ```

#### 3. **Create a new branch:** Isolate your changes from the main codebase

   ```bash
   git checkout -b new-feature-branch
   ```

#### 4. **Make your changes:** Implement your additions or modifications

#### 5. **Test your changes thoroughly:** Ensure everything works as expected

#### 6. **Commit your changes:**

   ```bash
   git add .
   ```

   ```bash
   git commit -m "Describe your changes briefly"
   ```

#### 7. **Push your changes:**

   ```bash
   git push origin new-feature-branch
   ```

#### 8. **Create a pull request:** Go to the original repository and create a pull request, detailing your changes and reasoning

#### 9. **Review and merge:** The project maintainers will review your changes and provide feedback. Upon approval, they'll merge your changes into the main codebase

### **Ideas for Contributions:**

- **New features:** Expand functionality with additional features.
- **Improved UI:** Enhance the user experience with visual or interactive elements.
- **Bug fixes:** Identify and resolve any bugs or errors.
- **Performance optimizations:** Improve code speed and efficiency.
- **Testing enhancements:** Expand test coverage for robustness.
- **Documentation additions:** Clarify or expand existing documentation.
