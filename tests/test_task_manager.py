# import pytest
# from task_manager_project.app.task_manager import TaskManager

# @pytest.fixture
# def manager():
#     """Фикстура для создания нового менеджера задач."""
#     return TaskManager()

# def test_add_task(manager):
#     """Тестирует добавление задач."""
    
#     # Проверим добавление задачи с нормальным приоритетом
#     task = manager.add_task("Test Task 1", "normal")
#     assert task == {"name": "Test Task 1", "priority": "normal", "completed": False}
#     assert len(manager.tasks) == 1  # Убедимся, что задача добавлена в список

#     # Проверим добавление задачи с низким приоритетом
#     task = manager.add_task("Test Task 2", "low")
#     assert task == {"name": "Test Task 2", "priority": "low", "completed": False}
#     assert len(manager.tasks) == 2  # Убедимся, что задача добавлена в список

#     # Проверим добавление задачи с высоким приоритетом
#     task = manager.add_task("Test Task 3", "high")
#     assert task == {"name": "Test Task 3", "priority": "high", "completed": False}
#     assert len(manager.tasks) == 3  # Убедимся, что задача добавлена в список

#     # Проверим обработку ошибки для неверного приоритета
#     with pytest.raises(ValueError):
#         manager.add_task("Test Task 4", "invalid_priority")

# def test_list_tasks(manager):
#     """Тестирует метод list_tasks."""
    
#     # Убедимся, что список задач изначально пустой
#     assert manager.list_tasks() == []
    
#     # Добавим несколько задач
#     manager.add_task("Task 1", "normal")
#     manager.add_task("Task 2", "high")
    
#     # Проверим, что метод list_tasks возвращает правильный список
#     tasks = manager.list_tasks()
#     assert len(tasks) == 2
#     assert tasks[0]["name"] == "Task 1"
#     assert tasks[1]["name"] == "Task 2"

# def test_mark_task_completed(manager):
#     """Тестирует метод mark_task_completed."""
    
#     # Добавим задачу
#     manager.add_task("Task 1", "normal")
    
#     # Убедимся, что задача не завершена
#     task = manager.list_tasks()[0]
#     assert task["completed"] is False
    
#     # Отметим задачу как выполненную
#     updated_task = manager.mark_task_completed("Task 1")
    
#     # Убедимся, что задача помечена как выполненная
#     assert updated_task["completed"] is True
#     assert updated_task["name"] == "Task 1"
    
#     # Попробуем отметить несуществующую задачу
#     with pytest.raises(ValueError):
#         manager.mark_task_completed("Nonexistent Task")

# def test_remove_task(manager):
#     """Тестирует метод remove_task."""
    
#     # Добавим задачи
#     manager.add_task("Task 1", "normal")
#     manager.add_task("Task 2", "high")
    
#     # Убедимся, что задачи добавлены
#     tasks = manager.list_tasks()
#     assert len(tasks) == 2
    
#     # Удалим задачу
#     removed_task = manager.remove_task("Task 1")
#     assert removed_task["name"] == "Task 1"
    
#     # Убедимся, что задача удалена
#     tasks = manager.list_tasks()
#     assert len(tasks) == 1
#     assert tasks[0]["name"] == "Task 2"
    
#     # Попробуем удалить несуществующую задачу
#     with pytest.raises(ValueError):
#         manager.remove_task("Nonexistent Task")

#  Task manager, улучшенный с помощью Allure

import pytest
import allure
from app.task_manager import TaskManager

@pytest.fixture
def manager():
    return TaskManager()

@allure.feature("Task Management")
@allure.story("Добавление задач")
def test_add_task(manager):

    """Добавление задач"""
    
    with allure.step("Добавить задачу с нормальным приоритетом"):
        task = manager.add_task("Test Task 1", "normal")
        assert task == {"name": "Test Task 1", "priority": "normal", "completed": False}
        assert len(manager.tasks) == 1

    with allure.step("Добавить задачу с низким приоритетом"):
        task = manager.add_task("Test Task 2", "low")
        assert task == {"name": "Test Task 2", "priority": "low", "completed": False}
        assert len(manager.tasks) == 2

    with allure.step("Добавить задачу с высоким приоритетом"):
        task = manager.add_task("Test Task 3", "high")
        assert task == {"name": "Test Task 3", "priority": "high", "completed": False}
        assert len(manager.tasks) == 3

    with allure.step("Попробовать добавить задачу с неверным приоритетом"):
        with pytest.raises(ValueError):
            manager.add_task("Test Task 4", "invalid_priority")

@allure.feature("Task Management")
@allure.story("Просмотр задач")
def test_list_tasks(manager):

    """Список задач"""
    
    with allure.step("Убедиться, что список задач изначально пустой"):
        assert manager.list_tasks() == []

    with allure.step("Добавить задачи и проверить список"):
        manager.add_task("Task 1", "normal")
        manager.add_task("Task 2", "high")
        tasks = manager.list_tasks()
        assert len(tasks) == 2
        assert tasks[0]["name"] == "Task 1"
        assert tasks[1]["name"] == "Task 2"

@allure.feature("Task Management")
@allure.story("Завершение задач")
def test_mark_task_completed(manager):

    """Завершение задач"""
    
    with allure.step("Добавить задачу и убедиться, что она не завершена"):
        manager.add_task("Task 1", "normal")
        task = manager.list_tasks()[0]
        assert task["completed"] is False

    with allure.step("Отметить задачу как выполненную"):
        updated_task = manager.mark_task_completed("Task 1")
        assert updated_task["completed"] is True
        assert updated_task["name"] == "Task 1"

    with allure.step("Попробовать завершить несуществующую задачу"):
        with pytest.raises(ValueError):
            manager.mark_task_completed("Nonexistent Task")

@allure.feature("Task Management")
@allure.story("Удаление задач")
def test_remove_task(manager):

    """Удаление задач"""
    
    with allure.step("Добавить задачи в список"):
        manager.add_task("Task 1", "normal")
        manager.add_task("Task 2", "high")
        tasks = manager.list_tasks()
        assert len(tasks) == 2

    with allure.step("Удалить существующую задачу"):
        removed_task = manager.remove_task("Task 1")
        assert removed_task["name"] == "Task 1"

    with allure.step("Проверить, что задача удалена"):
        tasks = manager.list_tasks()
        assert len(tasks) == 1
        assert tasks[0]["name"] == "Task 2"

    with allure.step("Попробовать удалить несуществующую задачу"):
        with pytest.raises(ValueError):
            manager.remove_task("Nonexistent Task")
