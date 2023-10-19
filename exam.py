import json
import os
from datetime import datetime


notes_file = "notes.json"

if not os.path.isfile(notes_file):
    with open(notes_file, "w") as file:
        json.dump([], file)

def load_notes():
    with open(notes_file, "r") as file:
        notes = json.load(file)
    return notes

def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=4)

def create_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Заголовок: ")
    body = input("Текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_at": timestamp,
        "updated_at": timestamp
    }

    notes.append(note)
    save_notes(notes)
    print("Заметка создана успешно!")

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Новый заголовок (Enter, чтобы оставить без изменений): ")
            new_body = input("Новый текст (Enter, чтобы оставить без изменений): ")

            if new_title:
                note["title"] = new_title
            if new_body:
                note["body"] = new_body

            note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            break
    else:
        print("Заметка с указанным ID не найдена.")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            break
    else:
        print("Заметка с указанным ID не найдена.")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Создано: {note['created_at']}, Обновлено: {note['updated_at']}")

if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Вывести список заметок")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            list_notes()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из меню.")
