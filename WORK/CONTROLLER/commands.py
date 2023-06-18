import REPOSITORY.loadFromFile as lF
import REPOSITORY.writeToFile as wF
import MODELS.Note


def add_note():
    title = input("ВВЕДИТЕ ЗАГОЛОВОК:\n")
    body = input("ВВЕДИТЕ ОПИСАНИЕ:\n")
    note = MODELS.Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if MODELS.Note.Note.get_id(note) == MODELS.Note.Note.get_id(i):
            MODELS.Note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("ЗАМЕТКА СОЗДАНА И УСМЕШНО ДОБАВЛЕНА")


def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("ЖУРНАЛ ЗАМЕТОК:")
            for i in array_notes:
                print(MODELS.Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", MODELS.Note.Note.get_id(i))
            id = input("\nВВЕДИТЕ ID ЗАМЕТКИ ")
            flag = True
            for i in array_notes:
                if id == MODELS.Note.Note.get_id(i):
                    print(MODELS.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("ТАКОГО ID НЕ СУЩЕСТВУЕТ")

        elif txt == "date":
            date = input("ФОРМАТ ДАТЫ: DD.MM.YYYY: ")
            flag = True
            for i in array_notes:
                date_note = str(MODELS.Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(MODELS.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("ЗАМЕТКИ С ТАКОЙ ДАТОЙ НЕ СУЩЕСТВУЕТ")
        else:
            print("ЖУРНАЛ ПУСТ")


def del_notes():
    id = input("ВВЕДИТЕ ID ЗАМЕТКИ, КОТОРУЮ ВЫ ХОТИТЕ УДАЛИТЬ: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == MODELS.Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("ЗАМЕТКА С ID: ", id, " УДАЛЕНА!")
    else:
        print("ТАКОГО ID НЕ СУЩЕСТВУЕТ")


def change_note():
    id = input("ВВЕДИТЕ ID ЗАМЕТКИ, КОТОРУЮ ВЫ ХОТИТЕ РЕДАКТИРОВАТЬ: ")
    array_notes = lF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == MODELS.Note.Note.get_id(i):
            i.title = input(":\n")
            i.body = input("РЕДАКТИРОВАТЬ ОПИСАНИЕ ЗАМЕТКИ:\n")
            MODELS.Note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'a')
        print("ЗАМЕТКА С ID ", id, " ИЗМЕНЕНА")
    else:
        print("ТАКОГО ID НЕ СУЩЕСТВУЕТ")








