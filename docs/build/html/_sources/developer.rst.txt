Developer Documentation
=======================

Architecture Overview
---------------------

The application follows a 3-layer architecture:

1. **Presentation Layer**: Kivy-based GUI (``main.py``, ``*.kv`` files)
2. **Logic Layer**: Task management operations (``logic_layer.py``)
3. **Data Layer**: Database interactions (``db_layer.py``)

Design Decisions
----------------

- **Database Choice**: MySQL was chosen for its reliability and ease of use
- **ORM**: Direct SQL queries are used for simplicity in this small application
- **Error Handling**: Exceptions are caught and re-raised with context

Future Enhancements
-------------------

1. Add task categories or tags
2. Implement task priorities
3. Add due dates and reminders
4. Support multiple task lists
5. Add user authentication