

# Function to display the main menu
def show_menu():
    print("\n--- To-Do List Application ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    print("-----------------------------")

# Function to add a task
def add_task(todo_list):
    task = input("Enter the task you want to add: ")
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

# Function to view all tasks
def view_tasks(todo_list):
    if not todo_list:
        print("No tasks to display.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
        print("-------------------")

# Function to delete a task
def delete_task(todo_list):
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Invalid task number.")

# Main function to run the app
def main():
    todo_list = []  # Store tasks in a list
    
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option (1-4): "))
            if choice == 1:
                add_task(todo_list)
            elif choice == 2:
                view_tasks(todo_list)
            elif choice == 3:
                delete_task(todo_list)
            elif choice == 4:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice, please choose a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
