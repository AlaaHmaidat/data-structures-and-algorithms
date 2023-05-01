from linked_list_insertions import Linked_List_Insertions

if __name__ == "__main__":
    llist = Linked_List_Insertions()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    # print(llist.insert_before("Z","F"))
    print(llist.insert_after("R","F"))
    print(llist)
 
