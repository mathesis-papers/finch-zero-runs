import argparse
import hashlib
import json
from pathlib import Path


def require(condition, description):
    if not condition:
        raise ValueError(description)


def sequence(lag, count):
    values = [0] * (count + 1)
    values[lag] = 1
    for index in range(lag + 1, count + 1):
        values[index] = (values[index - 1] + values[index - lag] ** 2) % 3
    return values


def pack(values):
    packed = 0
    for value in values:
        packed = 3 * packed + value
    return packed


def zero_mask(packed, gaps):
    for position in range(4 * gaps + 1):
        if (packed % 3 == 0) != (position % 4 == 0):
            return False
        packed //= 3
    return True


def is_run(values, lag, start, gaps):
    return start >= lag + 1 and gaps >= 1 and all(
        (values[start + position] == 0) == (position % 4 == 0)
        for position in range(4 * gaps + 1)
    )


def capture_examples():
    rows = []
    for lag in range(2, 42):
        values = sequence(lag, lag)
        phase = tuple(values[1:])
        positions = {phase: 0}
        for step in range(1, 200001):
            term = (phase[-1] + phase[0] ** 2) % 3
            phase = phase[1:] + (term,)
            values.append(term)
            if phase in positions:
                preperiod = positions[phase]
                period = step - preperiod
                break
            positions[phase] = step
        else:
            raise ValueError('Small-lag orbit exceeds the stated bound')
        row = {'lag': lag, 'least_preperiod': preperiod, 'least_period': period}
        if period == 4:
            gaps = (lag + 2) // 4
            count = preperiod + 4 * gaps + 4 * lag + 30
            for index in range(len(values), count + 1):
                values.append((values[index - 1] + values[index - lag] ** 2) % 3)
            endpoint = next(start + 4 * gaps
                            for start in range(lag + 1, len(values) - 4 * gaps)
                            if is_run(values, lag, start, gaps))
            offset = endpoint - preperiod
            require(offset == (9 if lag == 2 else 6), 'Capture offset differs')
            start = endpoint - 4 * gaps
            if lag % 4 == 2:
                require((values[start - 4] != 0) == (lag != 2),
                        'First neighborhood condition differs')
            else:
                require(values[start - 5] == 0 and values[start - 1] != 0,
                        'Second neighborhood condition differs')
            row.update(capture_endpoint=endpoint, capture_offset=offset)
        rows.append(row)
    return {'lag_range': {'first': 2, 'last': 41},
            'state_bound_per_lag': 200000,
            'scope': 'Finite examples of the capture theorem and neighborhood corollary; '
                     'the general statements have written proofs in the note.',
            'orbits': rows}


def calculate():
    lag = 61
    modulus = 3 ** 60

    def transition(packed):
        return 3 * (packed % modulus) + (packed % 3 + (packed // modulus) ** 2) % 3

    states = []
    positions = {}
    packed = 1
    while packed not in positions:
        require(len(states) < 10000, 'Orbit exceeds the specified certificate bound')
        require(0 <= packed < 3 ** lag, 'State outside the ternary encoding')
        positions[packed] = len(states)
        states.append(packed)
        packed = transition(packed)
    cycle_start = positions[packed]
    period = len(states) - cycle_start
    require((len(states), cycle_start, period) == (9685, 739, 8946), 'Orbit parameters differ')
    require(all(transition(states[index]) == states[index + 1]
                for index in range(len(states) - 1)), 'Successor equality fails')
    require(transition(states[-1]) == states[cycle_start], 'Closing equality fails')
    require(packed == 92196811829875935758365998383, 'Closing state differs')
    mask_counts = {str(gaps): sum(zero_mask(state, gaps) for state in states)
                   for gaps in (10, 11, 15)}
    require(mask_counts == {'10': 1, '11': 0, '15': 0}, 'Zero-mask counts differ')
    require([index for index, state in enumerate(states) if zero_mask(state, 10)] == [2759],
            'Ten-gap state index differs')
    values = sequence(lag, len(states) + lag + 2 * period)
    require(all(pack(values[index + 1:index + lag + 1]) == state
                for index, state in enumerate(states)), 'Scalar and packed representations differ')
    require(pack(values[len(states) + 1:len(states) + lag + 1]) == packed,
            'Scalar closing state differs')
    require(all(values[index + period] == values[index]
                for index in range(cycle_start + 1, len(values) - period)),
            'Scalar periodicity differs')
    require(values[739] != values[739 + period], 'Preperiod boundary differs')
    representatives = range(lag + 1, len(states) + 17)
    require(all(not is_run(values, lag, start, 11) for start in representatives),
            'Eleven-gap run occurs')
    ten_gap_starts = [start for start in representatives if is_run(values, lag, start, 10)]
    require(ten_gap_starts == [2780], 'Ten-gap representative differs')
    require(values[2780:2821] == [0, 1, 2, 2] * 10 + [0], 'Ten-gap block differs')
    example = sequence(4, 60)
    example_rows = [
        [0, 0, 0, 1, 1, 1, 1, 2, 0, 1],
        [2, 0, 0, 1, 2, 2, 2, 0, 1, 2],
        [0, 0, 1, 2, 2, 2, 0, 1, 2, 0],
        [0, 1, 2, 2, 2, 0, 1, 2, 0, 0],
        [1, 2, 2, 2, 0, 1, 2, 0, 0, 1],
        [2, 2, 2, 0, 1, 2, 0, 0, 1, 2],
    ]
    require(example[1:61] == [value for row in example_rows for value in row],
            'Example 18 differs')
    small = sequence(2, 80)
    require(small[1:] == [0, 1, 1, 2] * 20, 'Lag-two cycle differs')
    require(is_run(small, 2, 5, 1), 'Lag-two capture run differs')
    require(not any(is_run(small, 2, start, 1) for start in (3, 4)),
            'An earlier lag-two capture run occurs')
    orbit_digest = hashlib.sha256(('\n'.join(map(str, states)) + '\n').encode()).hexdigest()
    return {
        'schema_version': 1,
        'arithmetic': 'exact Python integers and reduction modulo 3',
        'lag': lag,
        'distinct_states': len(states),
        'state_indices': {'first': 0, 'last': 9684, 'closing': 9685},
        'first_repeated_index': cycle_start,
        'closing_state': packed,
        'least_eventual_period': period,
        'least_preperiod': cycle_start,
        'orbit_sha256_decimal_lines': orbit_digest,
        'suffix_mask_counts_by_gaps': mask_counts,
        'direct_scalar_terms': len(values) - 1,
        'direct_packed_comparisons': len(states),
        'run_start_representatives': {'first': 62, 'last': 9701},
        'maximum_gaps': 10,
        'source_upper_bound': 15,
        'ten_gap_start': 2780,
        'ten_gap_end': 2820,
        'ten_gap_start_progression': {'first': 2780, 'step': 8946},
        'ten_gap_block': '(0,1,2,2) repeated 10 times, followed by 0',
        'example_18_terms_matched': 60,
        'lag_two': {'cycle': [0, 1, 1, 2], 'least_period': 4,
                    'least_preperiod': 0, 'first_capture_start': 5,
                    'capture_endpoint': 9, 'capture_offset': 9},
        'capture_examples': capture_examples(),
        'status': 'ALL_CHECKS_OK',
    }


def main():
    parser = argparse.ArgumentParser(description='Exact zero-run and cycle checks for the accompanying note.')
    parser.add_argument('--write', type=Path)
    parser.add_argument('--check', type=Path)
    arguments = parser.parse_args()
    result = calculate()
    if arguments.check:
        require(result == json.loads(arguments.check.read_text()), 'Certificate content differs')
    output = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if arguments.write:
        arguments.write.write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
