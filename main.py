#Ben Weber/ weberbj
#I210 Mastery Project 3
#Initial Setup and Wish List class
'''Import statements'''
from gift import Gift
from people import Person
from data_handling import *

'''Establish wishlist class: Part 1'''
class WishList:
    wishlist_count = 0
    wishlist_list = []

    '''Constructor: Part 1'''
    def __init__(self, gift_list, child, address):
        self.__wishlist_number = WishList.wishlist_count
        self.__gift_list = gift_list
        self.__child = child
        self.__delivery = False
        self.__address = address
        WishList.wishlist_count += 1
        WishList.wishlist_list.append(self)

    '''To-string Method: Part 1'''
    def __str__(self):
        reply = ''
        reply += ('Wishlist for: ' + str(self.__child.get_name()) + '\n')
        reply += ('Gift List: ' + str(len(self.__gift_list)) + '\n')
        reply += ('Delivery address: ' + self.__address + '\n')
        reply += ('Wishlist number: ' + str(WishList.wishlist_count))
        return reply

    '''Method to allow child to add to wishlist: Part 1'''
    def child_add(self, gift):
        if self.__delivery == False:
            '''This looks at the gift.py file'''
            if isinstance(gift, Gift):
                if gift in self.__gift_list:
                    print('This is already in the giftlist.')
                else:
                    self.__gift_list.append(gift)
            else:
                print('This is not a valid gift!')
        else:
            print('The gift has already been delivered!')

    '''Allow parents to delete gift object: Part 1'''
    def parental_control(self, gift):
        if gift in self.__gift_list:
            self.__gift_list.remove(gift)
        else:
            print('That item isn\'t in the giftlist')
    
    '''Method to purchase the wishlist: Part 1'''
    def purchase_list(self):  
        if self.__delivery == False:
                if len(self.__gift_list) >= 1:
                    self.__delivery = True
                    print('The list is being delivered: ', self.__delivery)
                else:
                    print('The wishlist is empty and cannot be delivered')
        else:
            print('The Wish List has already been purchased and' 
                    'shouldn\'t be delivered again')
    
    '''Method to display all gifts in a wishlist: Part 2'''
    def display_all_gifts(self):
        if len(self.__gift_list) >= 1:
            temp_list = []
            for gift in self.__gift_list:
                '''This uses table_print function from data_handling.py'''
                temp_list.append((gift.get_name(), gift.get_cost(), gift.get_color()))
                table_print(('gift', 'cost', 'color'), temp_list)
        else:
            print('No information to display')

    '''Extra Credit: Wishlist total Price'''
    def wishlist_total_price(self):
        wishlist_price = 0
        for gift in self.__gift_list:
            if len(self.__gift_list) >= 1:
                wishlist_price += gift.get_cost()
            else:
                print('There is nothing to add in the list!')
        print('The total cost of the wishlist is: ${}'.format(wishlist_price))

    '''Gift reporting and testing: most popular gift among all wishlists'''
    @staticmethod
    def most_popular():
        pop_dct = {}
        for wishlist in WishList.wishlist_list:
            for gift in wishlist.__gift_list:
                if gift.get_name() in pop_dct:
                    pop_dct[str(gift.get_name())] += 1
                else:
                    pop_dct[str(gift.get_name())] = 1
        max_key = max(pop_dct, key = pop_dct.get)
        print('The gift that was most popular is : ', max_key)

    '''This is a static method to show all the gifts in a state.'''
    @staticmethod
    def all_gifts_state(state):
        state_dct = {}
        state_count = 0
        for wishlist in WishList.wishlist_list:            
            if (wishlist.__delivery == False) and (wishlist.__address.find(state) != -1):
                new_list = wishlist.__address.split(',')
                for i in new_list:
                    if i[1] == state:
                        state_count += 1
                    else:
                        state_count = 1
                header1 = 'Gift'
                header2 = 'Total Quantity'
                table_print([header1, header2], state_dct)
        print(state_count)
            
#getters and setters
def get_wishlist_number(self):
    return self.__get_wishlist_number
def set_wishlist_number(self, wishlist_number):
    self.__wishlist_number = wishlist_number

def get_child(self):
    return self.__child
def set_child(self, child):
    self.__child = child

def get_delivery(self):
    return self.__delivery
def set_delivery(self, delivery):
    self.__delivery = delivery

def get_gift_list(self):
    return self.__gift_list
def set_gift_list(self, gift_list):
    self.__gift_list = gift_list

def get_address(self):
    return self.__address
def set_address(self, address):
    self.__address = address


#main
if __name__ == '__main__':

    '''This proves the child and wishlist can be created.'''
    child1 = Person('Bill', '@email')
    wishlist1 = WishList([], child1, 'Chicago, IL')
    child2 = Person('Maria', '@email2')
    wishlist2 = WishList([], child2, 'New York, NY')
    child3 = Person('John', '@email3')
    wishlist3 = WishList([], child3, 'Chicago, IL')
    wishlist4 = WishList([], child3, 'Chicago, IL')
    wishlist5 = WishList([], child2, 'New York, NY')
    
    print('This proves the child add method')
    gift1 = Gift('Toy Car', 5, 'Black')
    gift2 = Gift('Flower', 0, 'Rose')
    gift3 = Gift('Blanket', 10, 'pink')
    wishlist1.child_add(gift1)
    wishlist1.child_add(gift2)
    wishlist1.child_add(gift3)

    gift1 = Gift('Train Set', 100)
    gift2 = Gift('Bike', 56, 'Red')
    gift3 = Gift('Bike', 56, 'Red')
    wishlist2.child_add(gift1)
    wishlist2.child_add(gift2)

    gift1 = Gift('TV', 560)
    gift2 = Gift('GameCube', 99)
    gift3 = Gift('Lamp', 2, 'white')
    wishlist3.child_add(gift1)
    wishlist3.child_add(gift2)
    wishlist3.child_add(gift3)

    gift1 = Gift('Clock', 10)
    gift2 = Gift('GameCube', 99)
    gift3 = Gift('Wreath', 15 , 'green')
    wishlist4.child_add(gift1)
    wishlist4.child_add(gift2)
    wishlist4.child_add(gift3)

    gift1 = Gift('GameCube', 99 )
    gift2 = Gift('Clock', 10)
    gift3 = Gift('TV', 560)
    gift4 = Gift('Toy Bus', 15 , 'yellow')
    wishlist5.child_add(gift1)
    wishlist5.child_add(gift2)
    wishlist5.child_add(gift3)
    wishlist5.child_add(gift4)
    print(wishlist1, '\n' * 2, wishlist2, '\n' * 2, wishlist3, '\n' * 2, wishlist4, '\n' * 2, wishlist5, '\n')

    print('This proves the parental control method.')
    wishlist1.parental_control(gift1)
    wishlist1.parental_control(gift2)
    wishlist1.parental_control(gift3)
    wishlist3.parental_control(gift1)
    wishlist5.parental_control(gift3)
    print(wishlist1, '\n' * 2, wishlist2, '\n' * 2, wishlist3, '\n' * 2, wishlist4, '\n' * 2, wishlist5, '\n')

    print('This proves the purchase purchase list method.')
    wishlist1.purchase_list()
    wishlist2.purchase_list()
    wishlist3.purchase_list()
    '''Wishlist 4 isn't purchased'''
    wishlist5.purchase_list()
    
    print('This proves the display all gifts method.')
    wishlist1.display_all_gifts()
    wishlist2.display_all_gifts()
    wishlist3.display_all_gifts()
    wishlist4.display_all_gifts()
    wishlist5.display_all_gifts()

    '''This checks Part 3: Most popular gift and gifts per state'''
    WishList.most_popular()
    WishList.all_gifts_state('IL')

    '''This is extra credit for total wishlist price'''
    wishlist1.wishlist_total_price()