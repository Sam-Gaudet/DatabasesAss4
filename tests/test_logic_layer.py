import pytest
from app.logic_layer import TaskManager

def test_load_tasks(task_manager):
    # Initially empty
    tasks = task_manager.load_tasks()
    assert len(tasks) == 0
    
    # Add some tasks
    task_manager.add_task("Task 1")
    task_manager.add_task("Task 2")
    
    tasks = task_manager.load_tasks()
    assert len(tasks) == 2
    assert tasks[0]["task_text"] == "Task 1"
    assert tasks[1]["task_text"] == "Task 2"

def test_add_task(task_manager):
    task_id = task_manager.add_task("New task")
    assert task_id is not None
    
    tasks = task_manager.load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task_text"] == "New task"

def test_update_task(task_manager):
    task_id = task_manager.add_task("Original")
    task_manager.update_task("Updated", task_id)
    
    tasks = task_manager.load_tasks()
    assert tasks[0]["task_text"] == "Updated"

def test_delete_task(task_manager):
    task_id = task_manager.add_task("To delete")
    tasks = task_manager.load_tasks()
    assert len(tasks) == 1
    
    task_manager.delete_task(task_id)
    tasks = task_manager.load_tasks()
    assert len(tasks) == 0

def test_invalid_db_config():
    with pytest.raises(RuntimeError):
        TaskManager({
            "host": "invalid",
            "user": "invalid",
            "password": "invalid",
            "database": "invalid"
        })