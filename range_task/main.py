from range_task.range import Range

range_1 = Range(3, 7)

range_2 = Range(7, 9)

intersection_range = range_1.get_intersection(range_2)
print(intersection_range)

union_range = range_1.get_union(range_2)
print(union_range)

difference_range = range_1.get_difference(range_2)
print(difference_range)


