class MenuService:
    def __init__(self,menu_repo):
        self.menu_repo = menu_repo

    def add_menu(self,m):
        self.menu_repo.add(m)

    def show_menu(self):
        self.menu_repo.show_menu()

    def get_item_name(self,menu_id):
        return self.menu_repo.get_name(menu_id)
    
    def get_price(self,menu_id):
        return self.menu_repo.get_price(menu_id)
    
    def get(self,menu_id):
        return self.menu_repo.get(menu_id)