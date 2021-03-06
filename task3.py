def appearance(intervals):
    def merge_intervals(intervals):
        """
        Функция для объединения общих временных интервалов.
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for current in intervals[1:]:
            if current[0] <= res[-1][1]:
                res[-1][1] = max(current[1], res[-1][1])
            else:
                res.append(current)
        return res

    lesson = [intervals['lesson']]
    pupil = merge_intervals(
        [[intervals['pupil'][i], intervals['pupil'][i+1]]
         for i in range(0, len(intervals['pupil']), 2)]
    )
    tutor = merge_intervals(
        [[intervals['tutor'][i], intervals['tutor'][i+1]]
         for i in range(0, len(intervals['tutor']), 2)]
    )
    common_intervals = lesson + pupil + tutor

    time_intervals = []

    for interval in common_intervals:
        time_intervals.append((interval[0], 1))
        time_intervals.append((interval[1], -1))

    time_intervals.sort(key=lambda x: x[0])

    common_time = 0
    count = 0
    start = -1

    for i in time_intervals:
        count += i[1]
        if count == 3:
            start = i[0]
        elif count == 2 and start > 0:
            common_time += (i[0] - start)
            start = -1

    return common_time


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], (
            f'Error on test case {i}, '
            f'got {test_answer}, expected {test["answer"]}'
        )
