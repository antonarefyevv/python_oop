from range_task.range import Range

range_1 = Range(3, 5)
range_2 = Range(5, 9)

intersection_range = range_1.get_intersection(range_2)
if intersection_range is not None:
    print(f'Результат пересечения диапазонов Range{range_1} и Range{range_2} = Range{intersection_range}')
else:
    print(f'Результат пересечения диапазонов Range{range_1} и Range{range_2} = {intersection_range}')

union_range = range_1.get_union(range_2)
if len(union_range) == 2:
    print(
        f'Результат объединения диапазонов Range{range_1} и Range{range_2} = [Range{union_range[0]}, Range{union_range[1]}]')
else:
    print(
        f'Результат объединения диапазонов Range{range_1} и Range{range_2} = Range{union_range[0]}')

difference_range = range_1.get_difference(range_2)
if len(difference_range) == 2:
    print(
        f'Результат разности диапазонов Range{range_1} и Range{range_2} = [Range{difference_range[0]}, Range{difference_range[1]}]')
else:
    print(
        f'Результат разности диапазонов Range{range_1} и Range{range_2} = Range{difference_range[0]}')
