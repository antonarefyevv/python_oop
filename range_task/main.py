from range_task.range import Range

range_1 = Range(1, 5)
range_2 = Range(1, 3)

print(range_1.get_length())

intersection_range = range_1.get_intersection(range_2)

if intersection_range is not None:
    print(f'Результат пересечения диапазонов Range{range_1} и Range{range_2} = Range{intersection_range}')
else:
    print(f'Результат пересечения диапазонов Range{range_1} и Range{range_2} = {intersection_range}')

union_range = range_1.get_union(range_2)
print(f'Результат объединения диапазонов Range{range_1} и Range{range_2} = {union_range}')

difference_range = range_1.get_difference(range_2)
print(f'Результат разности диапазонов Range{range_1} и Range{range_2} = {difference_range}')
