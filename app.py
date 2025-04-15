from src.model.sistema import Sistema
from src.view.console.menu import Menu
if __name__ == "__main__":
    sistema = Sistema()
    menu = Menu(sistema)
    menu.mostrar_menu()