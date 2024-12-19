import sqlite3
import os

# Ruta de la base de datos
DB_PATH = "time_tracker.db"


def connect():
    """Conectar a la base de datos SQLite."""
    return sqlite3.connect(DB_PATH)


def initialize_db():
    """Inicializa la base de datos con las tablas necesarias."""
    with connect() as conn:
        cursor = conn.cursor()

        # Crear tabla Categorías
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)

        # Crear tabla Actividades
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities  (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
        """)

        # Crear tabla Metas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER NOT NULL,
            hours_meta REAL NOT NULL,
            weekly_hours REAL NOT NULL,
            week_start DATE NOT NULL,
            week_end DATE NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
        """)

        # Crear tabla Registros
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS time_logs  (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            activity_id INTEGER NOT NULL,
            time_spent REAL NOT NULL,
            date DATE NOT NULL,
            FOREIGN KEY (activity_id) REFERENCES activities (id)
        )
        """)

        print("Base de datos inicializada.")


# CRUD para la tabla 'categories'


def create_category(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()


def read_categories():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    conn.close()
    return categories


def update_category(category_id, new_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE categories SET name = ? WHERE id = ?", (new_name, category_id)
    )
    conn.commit()
    conn.close()


def delete_category(category_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    conn.commit()
    conn.close()


# CRUD para la tabla 'activities'


def create_activity(name, category_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO activities (name, category_id) VALUES (?, ?)", (name, category_id)
    )
    conn.commit()
    conn.close()


def read_activities():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT activities.id, activities.name, categories.name AS category_name 
        FROM activities
        INNER JOIN categories ON activities.category_id = categories.id
    """)
    activities = cursor.fetchall()
    conn.close()
    return activities


def update_activity(activity_id, new_name, new_category_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE activities SET name = ?, category_id = ? WHERE id = ?",
        (new_name, new_category_id, activity_id),
    )
    conn.commit()
    conn.close()


def delete_activity(activity_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM activities WHERE id = ?", (activity_id,))
    conn.commit()
    conn.close()


# CRUD para la tabla 'goals'


def create_goal(category_id, hours_meta, week_hours, start_date, end_date):
    conn = sqlite3.connect('time_tracker.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO goals (category_id, hours_meta, weekly_hours, week_start, week_end) VALUES (?, ?, ?, ?, ?)",
        (category_id, hours_meta, week_hours, start_date, end_date)
    )
    conn.commit()
    conn.close()


def read_goals():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT goals.id, categories.name AS category_name, goals.weekly_hours, goals.week_start, goals.week_end
        FROM goals
        INNER JOIN categories ON goals.category_id = categories.id
    """)
    goals = cursor.fetchall()
    conn.close()
    return goals


def update_goal(goal_id, new_weekly_hours, new_start_date, new_end_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE goals 
        SET weekly_hours = ?, week_start = ?, week_end = ? 
        WHERE id = ?
    """,
        (new_weekly_hours, new_start_date, new_end_date, goal_id),
    )
    conn.commit()
    conn.close()


def delete_goal(goal_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM goals WHERE id = ?", (goal_id,))
    conn.commit()
    conn.close()


# CRUD para la tabla 'time_logs'


def log_time(activity_id, duration, log_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO time_logs (activity_id, time_spent, date) VALUES (?, ?, ?)",
        (activity_id, duration, log_date),
    )
    conn.commit()
    conn.close()


def read_time_logs():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT time_logs.id, activities.name AS activity_name, time_logs.time_spent, time_logs.date
        FROM time_logs
        INNER JOIN activities ON time_logs.activity_id = activities.id
    """)
    time_logs = cursor.fetchall()
    conn.close()
    return time_logs


def update_time_log(log_id, new_duration, new_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE time_logs SET time_spent = ?, date = ? WHERE id = ?",
        (new_duration, new_date, log_id),
    )
    conn.commit()
    conn.close()


def delete_time_log(log_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM time_logs WHERE id = ?", (log_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Llamado a los CRUDs de test.
    # # Crear categorías
    # create_category("Salud")
    # create_category("Trabajo")
    # print("categories:", read_categories())

    # # Crear metas
    # create_goal(1, 10, 5, "2024-12-18", "2024-12-24")  # 10 horas para Salud
    # create_goal(2, 15, 5, "2024-12-18", "2024-12-24")  # 15 horas para Trabajo
    # print("goals:", read_goals())

    # # Actualizar meta
    # update_goal(1, 12, "2024-12-18", "2024-12-24")  # Cambiar a 12 horas
    # print("Metas después de actualizar:", read_goals())

    # # Eliminar una meta
    # delete_goal(2)  # Eliminar la meta para Trabajo
    # print("Metas después de eliminar:", read_goals())
    ##
    if not os.path.exists(DB_PATH):
        initialize_db()
    else:
        print("La base de datos ya existe.")
