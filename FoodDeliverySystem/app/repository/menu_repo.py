class MenuRepo:
    def __init__(self):
        self.menu = {}

    def add(self,m):
        self.menu[m.menu_id] = m

    def show_menu(self):
        print("\n ========== MENU ===========\n")
        for mid,mobj in self.menu.items():
            print(f"Menu ID: {mid} | Item Name: {mobj.item_name} | Description: {mobj.desc} | Price: {mobj.price}")

    def get_name(self,menu_id):
        return self.menu.get(menu_id).item_name
    
    
    def get_price(self,menu_id):
        return self.menu.get(menu_id).price
    
    def get(self,menu_id):
        return self.menu.get(menu_id)
        