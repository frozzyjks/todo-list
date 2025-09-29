import sqlite3

# Подключение к базе
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Создаём таблицу задач
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status INTEGER DEFAULT 0
);
""")
conn.commit()

# Функции
def add_task(title):
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()

def show_tasks():
    cursor.execute("SELECT id, title, status FROM tasks")
    tasks = cursor.fetchall()
    if tasks:
        for task in tasks:
            status = "✅" if task[2] == 1 else "❌"
            print(f"{task[0]}. {task[1]} {status}")
    else:
        print("Список дел пуст!")

def complete_task(task_id):
    cursor.execute("UPDATE tasks SET status = 1 WHERE id = ?", (task_id,))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()


while True:
    print("\n📋 Список дел:")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Введите название задачи: ")
        add_task(title)
        print("Задача добавлена!")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_id = int(input("Введите ID задачи для отметки: "))
        complete_task(task_id)
        print("Задача отмечена как выполненная!")
    elif choice == "4":
        task_id = int(input("Введите ID задачи для удаления: "))
        delete_task(task_id)
        print("Задача удалена!")
    elif choice == "5":
        print("Выход...")
        break
    else:
        print("Неверный выбор!")