import pytest
from app.db_layer import Database

def test_create_table(test_db):
    # Table creation is handled in the fixture
    test_db.cursor.execute("SHOW TABLES LIKE 'tasks'")
    result = test_db.cursor.fetchone()
    assert result is not None

def test_add_task(test_db):
    task_id = test_db.add_task("Test task")
    assert task_id is not None
    
    test_db.cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = test_db.cursor.fetchone()
    assert task["task_text"] == "Test task"

def test_fetch_all_tasks(test_db):
    test_db.add_task("Task 1")
    test_db.add_task("Task 2")
    
    tasks = test_db.fetch_all_tasks()
    assert len(tasks) == 2
    assert tasks[0]["task_text"] == "Task 1"
    assert tasks[1]["task_text"] == "Task 2"

def test_update_task(test_db):
    task_id = test_db.add_task("Original task")
    test_db.update_task("Updated task", task_id)
    
    test_db.cursor.execute("SELECT task_text FROM tasks WHERE id = %s", (task_id,))
    task = test_db.cursor.fetchone()
    assert task["task_text"] == "Updated task"

def test_delete_task(test_db):
    task_id = test_db.add_task("Task to delete")
    test_db.delete_task(task_id)
    
    test_db.cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = test_db.cursor.fetchone()
    assert task is None, "Task should be deleted from database"