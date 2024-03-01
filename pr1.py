
my_list = [1, 2, 3, 4, 3, 5, 3]
element_to_remove = 3
count_removed = 0

while element_to_remove in my_list:
    my_list.remove(element_to_remove)
    count_removed += 1

print("لیست پس از حذف عنصر مورد نظر:", my_list)
print("تعداد عناصر حذف شده:", count_removed)
