from range_task.range import Range

range_1 = Range(1, 5)
print(range_1.get_length())

range_2 = Range(2, 5)
print(range_2.get_length())

range_3 = Range(7, 9)
print(range_3.get_length())

print(range_3.start)
print(range_2.is_inside(5))

print(range_1.get_intersection(range_2))

print(range_1.get_union(range_3))

print(range_2.get_difference(range_1))
