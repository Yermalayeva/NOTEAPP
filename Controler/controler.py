import UI.userMenuConsole as ui
import Controler.command as com


def start():
    while True:
        ui.menu_console()
        user_input = input()
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.show("ID")
        elif user_input == '3':
            com.show("date")
        elif user_input == '4':
            break
        elif user_input == '5':
            com.add_note()
        elif user_input == '6':
            com.show("all")
            com.del_notes()
        else:
            print("Программа Журнал заметок завершена")
