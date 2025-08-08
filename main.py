# main.py
from task_model import TaskModel

def main():
    task = TaskModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
<<<<<<< HEAD
    task.mark_as_complete()
    print(f"Tarea completada: {task.is_completed()}")
=======
    task.set_done()
    print(f"Tarea completada: {task.is_done()}")
    task.remove_task()
    print(f"Tarea eliminada: {task.get_task_name()}")
>>>>>>> juan-tuiran

if __name__ == "__main__":
    main()

