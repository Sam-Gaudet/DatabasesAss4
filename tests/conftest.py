import pytest
import sys
import os
import mysql.connector
from mysql.connector import Error
from typing import Generator, Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db_layer import Database
from app.logic_layer import TaskManager

@pytest.fixture(scope="session")
def test_db_config() -> Dict[str, Any]:
    """Configuration for test database connection"""
    return {
        "host": "localhost",
        "user": "root",
        "password": "root123",
        "database": "test_tasklist"
    }

@pytest.fixture(scope="session")
def test_database(test_db_config) -> None:
    """Creates test database if it doesn't exist (session scope)"""
    try:
        conn = mysql.connector.connect(
            host=test_db_config["host"],
            user=test_db_config["user"],
            password=test_db_config["password"]
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {test_db_config['database']}")
        conn.commit()
    except Error as e:
        pytest.fail(f"Failed to create test database: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@pytest.fixture(scope="session")
def test_tables(test_db_config, test_database) -> None:
    """Creates required tables in test database (session scope)"""
    try:
        conn = mysql.connector.connect(**test_db_config)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task_text VARCHAR(255) NOT NULL
            )
        """)
        conn.commit()
    except Error as e:
        pytest.fail(f"Failed to create tables: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@pytest.fixture
def clean_db(test_db_config, test_database, test_tables) -> None:
    """Cleans all data from tables before each test"""
    try:
        conn = mysql.connector.connect(**test_db_config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks")
        conn.commit()
    except Error as e:
        pytest.fail(f"Failed to clean database: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@pytest.fixture
def test_db(test_db_config, test_database, test_tables, clean_db) -> Generator[Database, None, None]:
    """Provides a clean database connection for each test"""
    db = None
    try:
        db = Database(**test_db_config)
        yield db
    except Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        if db:
            db.close()

@pytest.fixture
def task_manager(test_db_config, test_database, test_tables, clean_db) -> Generator[TaskManager, None, None]:
    """Provides a TaskManager instance with clean database for each test"""
    manager = None
    try:
        manager = TaskManager(test_db_config)
        yield manager
    except Exception as e:
        pytest.fail(f"TaskManager initialization failed: {e}")
    finally:
        if manager:
            manager.close()

@pytest.fixture
def sample_task_data() -> Dict[str, Any]:
    """Provides sample task data for testing"""
    return {
        "normal": "Test task",
        "empty": "",
        "long": "A" * 300,
        "special_chars": "Task @#$%^"
    }