# Task List App

A simple task management application with Kivy UI and MySQL backend.

## Features

- Add, update, and delete tasks
- Persistent storage with MySQL
- Clean and intuitive UI

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- Git (optional)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sam-Gaudet/DatabasesAss4.git
   cd tasklist-app
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**: (mysql, or use the path to your mysql on your computer)
   ```bash
   mysql -u root -p < db_creation.sql
   ```

5. **Configure environment variables**:  
   Copy `.env.example` to `.env` and update it with your database credentials:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=yourpassword
   DB_NAME=tasklist_assignment4
   ```

## Running the Application

```bash
python -m app.main
```

---

## Testing

### Running Unit Tests

To run all tests with basic output:
```bash
pytest tests/
```

For more detailed test output:
```bash
pytest tests/ -v
```

To run tests with specific options:
```bash
pytest tests/ --maxfail=1 --disable-warnings -q
```

To check test coverage:
```bash
pytest --cov=app tests/
```

### Test Options Explained

- `--maxfail=1`: Stop after first failure  
- `--disable-warnings`: Suppress warning messages  
- `-q`: Quiet mode (minimal output)  
- `-v`: Verbose mode (detailed output)  
- `--cov=app`: Generate coverage report for `app` package  

---

## Documentation

### Building Documentation

Install documentation dependencies:
```bash
pip install sphinx sphinx-rtd-theme
```

Important: Set the documentation build flag:
```bash
set BUILDING_DOCS=true  # Windows
export BUILDING_DOCS=true  # macOS/Linu
```

Build the HTML documentation:
```bash
cd docs
make html
```

Remember to unset when done with documentation:
```bash
set BUILDING_DOCS=false  # Windows
unset BUILDING_DOCS  # macOS/Linux
```

If `make` is not available:
```bash
python -m sphinx.cmd.build -b html source build
```

### Viewing Documentation

Open `docs/build/html/index.html` in your browser to view the generated documentation.

## Development Notes

### Challenges and Solutions

**Database Connection Management**  
- *Challenge*: Tests interfering through shared database state  
- *Solution*: Created `clean_db` fixture to reset tables before each test  

**Documentation Generation**  
- *Challenge*: Sphinx failing on Kivy imports  
- *Solution*: Implemented `BUILDING_DOCS` environment flag  

**Test Coverage**  
- *Challenge*: Missing edge case validation  
- *Solution*: Added parameterized tests for:  
  - Empty strings (`""`)  
  - Long inputs (300+ chars)  
  - Special characters (`@#$%`)  

**Environment Configuration**  
- *Challenge*: Hardcoded test credentials  
- *Solution*: Added .env file to .gitignore