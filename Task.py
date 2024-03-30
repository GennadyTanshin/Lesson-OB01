# Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append({"Наименование задачи": description, "Срок выполнения": due_date, "Выполнено": False})

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task["Наименование задачи"] == description:
                task["Выполнено"] = True
                break

    def show_current_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if not task["Выполнено"]:
                print(f'{task["Наименование задачи"]} (Выполнить: {task["Срок выполнения"]})')


task_manager = Task()


task_manager.add_task("Помыть слона", "14-01-2024")
task_manager.add_task("Проветрить сумку кенгуру", "20-02-2024")

task_manager.show_current_tasks()

task_manager.mark_task_completed("Помыть слона")

task_manager.show_current_tasks()
