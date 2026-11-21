import argparse
import itertools
import json


def check_four_cycles():
    counts = {}
    for residue in range(4):
        cycles = []
        for word in itertools.product(range(3), repeat=4):
            if all(word[position] == word[(position - 1) % 4]
                   for position in range(4)):
                continue
            if all(word[position] == word[(position + 2) % 4]
                   for position in range(4)):
                continue
            if all(word[position] == (word[(position - 1) % 4]
                                     + word[(position - residue) % 4] ** 2) % 3
                   for position in range(4)):
                cycles.append(word)
        expected = (0, 1, 1, 2) if residue == 2 else (0, 1, 2, 2)
        rotations = {expected[offset:] + expected[:offset] for offset in range(4)}
        assert set(cycles) == (rotations if residue in (2, 3) else set())
        counts[str(residue)] = len(cycles)
    return counts


def inspect_parameter(parameter, cap):
    values = bytearray([0] * parameter + [1])
    required_gaps = (parameter + 2) // 4
    previous_zero = None
    consecutive_gaps = 0
    capture = None
    while len(values) <= cap:
        position = len(values)
        values.append((values[position - 1] + values[position - parameter] ** 2) % 3)
        if values[position] == 0:
            if previous_zero is not None and position - previous_zero == 4:
                consecutive_gaps += 1
            else:
                consecutive_gaps = 0
            previous_zero = position
            if consecutive_gaps >= required_gaps:
                capture = position
                break
    if capture is None:
        return {'k': parameter, 'capture_found': False, 'last_index': cap}
    for position in range(len(values), capture + parameter + 4):
        values.append((values[position - 1] + values[position - parameter] ** 2) % 3)
    assert values[capture:capture + parameter] == values[capture + 4:capture + parameter + 4]
    assert any(values[capture + offset] != values[capture + (offset + 2) % 4]
               for offset in range(4))
    preperiod = max((position for position in range(1, capture)
                     if values[position] != values[position + 4]), default=0)
    start = capture - 4 * required_gaps
    assert start >= parameter + 1
    assert all((values[position] == 0) == ((position - start) % 4 == 0)
               for position in range(start, capture + 1))
    if parameter == 2:
        assert (preperiod, capture, start) == (0, 9, 5)
    else:
        assert capture == preperiod + 6
        residue = parameter % 4
        assert residue in (2, 3)
        expected_pair = (2, 2) if residue == 2 else (1, 2)
        assert tuple(values[preperiod:preperiod + 2]) == expected_pair
        assert values[preperiod + 2] == 0
        marker = preperiod + 1 - parameter
        assert (values[marker] != 0) == (residue == 3)
        assert start == preperiod - parameter + (4 if residue == 2 else 5)
        if residue == 2:
            assert values[start - 4] != 0
        else:
            assert values[start - 5] == 0 and values[start - 1] != 0
    return {'k': parameter, 'capture_found': True, 'mu': preperiod,
            'z': capture, 's': start, 'offset': capture - preperiod,
            'four_period_state_equality': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-k', type=int, default=80)
    parser.add_argument('--cap', type=int, default=1000000)
    arguments = parser.parse_args()
    assert 3 <= arguments.max_k <= 1000
    assert arguments.max_k + 4 <= arguments.cap <= 10000000
    rows = [inspect_parameter(parameter, arguments.cap)
            for parameter in range(2, arguments.max_k + 1)
            if parameter % 4 in (2, 3)]
    output = {'coverage': 'Finite trajectories and all 81 four-letter words per lag residue; '
                          'the universal conditional identity is proved in note.tex.',
              'max_k': arguments.max_k, 'cap_per_k': arguments.cap,
              'four_cycle_counts_by_lag_residue': check_four_cycles(),
              'captured_count': sum(row['capture_found'] for row in rows),
              'bounded_search_without_capture': [row['k'] for row in rows if not row['capture_found']],
              'parameters': rows}
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
