from linked_list import Linked_List
from doubly_linked_list import Doubly_Linked_List

if __name__ == "__main__":
    llist = Linked_List()
    llist.insert("A")
    print(llist)
    print(llist.includes("C"))

    dllist = Doubly_Linked_List()
    dllist.insert("A")
    print(dllist)
    print(dllist.includes("C"))
