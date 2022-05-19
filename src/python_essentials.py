def get_list_len(your_list):
    # "list comprehension" - python docs
    list_starts_with_a = [item for item in your_list if item.startswith("a")]
    print(list_starts_with_a)

#     list_starts_with_a = 0
#     for item in your_list:
#         if item.startswith("a"):
#             list_starts_with_a = list_starts_with_a + 1
            
    return len(list_starts_with_a)


my_list = ["aeger", "baser", "aerec", "dhaer", "aegserz", "dwegx"]
get_list_len(my_list)



for i in range(1, 10, 3):
    print(i)
    
