class MenuServices:
    def __init__(self,usercart_services):
        self.menu = {}
        self.usercart_services = usercart_services
    def add_menu(self,m):
        self.menu[m.menu_id] = m

    def show_menu(self):
        print(" ========== MENU ========== ")
        for m in self.menu.values():
            print(f"Menu_ID: {m.menu_id} | Res_ID: {m.res_id} | Item_Name: {m.item_name} | Price: {m.price}")

    def view_cart_menu(self,menu_id,cart_id):
        print("========== ITEM IN CART ==========")
        menu_id = int(menu_id)
        m = self.menu.get(menu_id)
        if m:
            print(f"Item name: {m.item_name} | Price: {m.price} | ")
        else:
            print("Item not found")

    def get_item(self,menu_id):
        return self.menu.get(menu_id)
    




