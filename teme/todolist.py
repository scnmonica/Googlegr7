import datetime

class ToDoList:
    def __init__(self):
        self.categories = set()
        self.tasks = []

    def add_task(self, task, deadline, responsible, category):
        if self.check_duplicate_task(task):
            print("Taskul există deja în listă.")
            return

        if category not in self.categories:
            print("Categoria specificată nu există.")
            return

        self.tasks.append({
            'task': task,
            'deadline': deadline,
            'responsible': responsible,
            'category': category
        })

    def check_duplicate_task(self, task):
        for existing_task in self.tasks:
            if existing_task['task'] == task:
                return True
        return False

    def show_tasks(self, sort_by_category=False):
        if sort_by_category:
            sorted_tasks = sorted(self.tasks, key=lambda x: x['category'])
        else:
            sorted_tasks = self.tasks

        for index, task in enumerate(sorted_tasks, start=1):
            print(f"Task {index}:")
            print(f"Task: {task['task']}")
            print(f"Deadline: {task['deadline']}")
            print(f"Responsible: {task['responsible']}")
            print(f"Category: {task['category']}")
            print()

    def sort_tasks(self, sort_option):
        if sort_option == 1:
            self.tasks.sort(key=lambda x: x['task'])
        elif sort_option == 2:
            self.tasks.sort(key=lambda x: x['task'], reverse=True)
        elif sort_option == 3:
            self.tasks.sort(key=lambda x: datetime.datetime.strptime(x['deadline'], '%d.%m.%Y %H:%M'))
        elif sort_option == 4:
            self.tasks.sort(key=lambda x: datetime.datetime.strptime(x['deadline'], '%d.%m.%Y %H:%M'), reverse=True)
        elif sort_option == 5:
            self.tasks.sort(key=lambda x: x['responsible'])
        elif sort_option == 6:
            self.tasks.sort(key=lambda x: x['responsible'], reverse=True)
        elif sort_option == 7:
            self.tasks.sort(key=lambda x: x['category'])
        elif sort_option == 8:
            self.tasks.sort(key=lambda x: x['category'], reverse=True)

    def filter_tasks(self, field, filter_value):
        filtered_tasks = []

        for task in self.tasks:
            if field == 1 and task['task'].startswith(filter_value):
                filtered_tasks.append(task)
            elif field == 2 and task['deadline'].startswith(filter_value):
                filtered_tasks.append(task)
            elif field == 3 and task['responsible'].startswith(filter_value):
                filtered_tasks.append(task)
            elif field == 4 and task['category'].startswith(filter_value):
                filtered_tasks.append(task)

        for index, task in enumerate(filtered_tasks, start=1):
            print(f"Task {index}:")
            print(f"Task: {task['task']}")
            print(f"Deadline: {task['deadline']}")
            print(f"Responsible: {task['responsible']}")
            print(f"Category: {task['category']}")
            print()

    def edit_task(self, task_index, field, new_value):
        task = self.tasks[task_index - 1]

        if field == 1:
            if self.check_duplicate_task(new_value):
                print("Taskul există deja în listă")
                return
            task['task'] = new_value
        elif field == 2:
            task['deadline'] = new_value
        elif field == 3:
            task['responsible'] = new_value
        elif field == 4:
            if new_value not in self.categories:
                print("Categoria specificată nu există.")
                return
            task['category'] = new_value

    def delete_task(self, task_index):
        if task_index < 1 or task_index > len(self.tasks):
            print("Indexul taskului este invalid.")
            return
        del self.tasks[task_index - 1]

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task['task']},{task['deadline']},{task['responsible']},{task['category']}\n")

    def load_tasks_from_file(self, filename):
        self.tasks = []
        self.categories = set()
        with open(filename, 'r') as file:
            for line in file:
                task_data = line.strip().split(',')
                self.add_task(task_data[0], task_data[1], task_data[2], task_data[3])


# Exemplu de utilizare

todo_list = ToDoList()

while True:
    print("1. Adăugare task")
    print("2. Afișare taskuri")
    print("3. Sortare taskuri")
    print("4. Filtrare taskuri")
    print("5. Adăugare task")
    print("6. Editare task")
    print("7. Ștergere task")
    print("8. Salvare taskuri în fișier")
    print("9. Încărcare taskuri din fișier")
    print("10. Ieșire")
    choice = input("Alegeți o opțiune: ")

    if choice == '1':
        task = input("Introduceți taskul: ")
        deadline = input("Introduceți data limită (ex. 22.01.2022 21:30): ")
        responsible = input("Introduceți persoana responsabilă: ")
        category = input("Introduceți categoria: ")
        todo_list.add_task(task, deadline, responsible, category)

    elif choice == '2':
        sort_option = input("Sortare după categorie? (da/nu): ")
        if sort_option.lower() == 'da':
            todo_list.show_tasks(sort_by_category=True)
        else:
            todo_list.show_tasks()

    elif choice == '3':
        sort_option = int(input("Introduceți opțiunea de sortare: "))
        todo_list.sort_tasks(sort_option)

    elif choice == '4':
        field = int(input("Introduceți câmpul după care se realizează filtrarea: "))
        filter_value = input("Introduceți valoarea de filtrare: ")
        todo_list.filter_tasks(field, filter_value)

    elif choice == '5':
        task = input("Introduceți taskul: ")
        deadline = input("Introduceți data limită (ex. 22.01.2022 21:30): ")
        responsible = input("Introduceți persoana responsabilă: ")
        category = input("Introduceți categoria: ")
        todo_list.add_task(task, deadline, responsible, category)

    elif choice == '6':
        task_index = int(input("Introduceți indexul taskului de editat: "))
        field = int(input("Introduceți câmpul de editat: "))
        value = input("Introduceți noua valoare: ")
        todo_list.edit_task(task_index, field, value)

    elif choice == '7':
        task_index = int(input("Introduceți indexul taskului de șters: "))
        todo_list.delete_task(task_index)

    elif choice == '8':
        filename = input("Introduceți numele fișierului pentru salvare: ")
        todo_list.save_tasks_to_file(filename)

    elif choice == '9':
        filename = input("Introduceți numele fișierului pentru încărcare: ")
        todo_list.load_tasks_from_file(filename)

    elif choice == '10':
        break

    else:
        print("Opțiune invalidă. Reîncercați.")

