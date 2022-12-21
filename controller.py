import add_to_bd
import search
import view


def phone_book():
    menu = 0
    while menu != 4:
        menu = view.main_menu()
        if menu == 1:
            phone_data = view.write_data()
            add_to_bd.add_to_txt(phone_data)
            add_to_bd.add_to_csv(phone_data)
        elif menu == 2:
            search.full_output()
        elif menu == 3:
            last_name = view.search_data()
            search.find_data(last_name)
