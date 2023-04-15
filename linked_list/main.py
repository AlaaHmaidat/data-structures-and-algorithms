from linked_list import Linked_List,Doubly_Linked_List

if __name__ == "__main__":
    llist = Linked_List()

    llist.insert("A")
    llist.insert("B")
    print(llist.__str__())

    print(llist.includes("C"))

    llist = Doubly_Linked_List()

    llist.insert("A")
    llist.insert("B")
    
    print(llist.to_string())

    print(llist.includes("A"))
