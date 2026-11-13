import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path


def valid_tile(top_left, top_right, bottom_left, bottom_right):
    differences = (top_right - top_left, bottom_right - top_right,
                   bottom_left - bottom_right, top_left - bottom_left)
    return len(set(differences)) == 4


def base_count(index):
    if index % 2:
        return 2 ** ((index + 1) // 2)
    return 3 * 2 ** (index // 2 - 1)


def compatible(top, bottom):
    return all(valid_tile(top[column], top[column + 1],
                          bottom[column], bottom[column + 1])
               for column in range(len(top) - 1))


def graph_from_columns(width):
    column_states = list(product(range(3), repeat=2))
    next_columns = {
        state: [following for following in column_states
                if valid_tile(state[0], following[0], state[1], following[1])]
        for state in column_states
    }
    paths = [(state,) for state in column_states]
    for _ in range(width - 1):
        paths = [path + (following,) for path in paths
                 for following in next_columns[path[-1]]]
    graph = {}
    for path in paths:
        top = tuple(column[0] for column in path)
        bottom = tuple(column[1] for column in path)
        graph.setdefault(top, set()).add(bottom)
    return graph


def direct_graph(width):
    rows = list(product(range(3), repeat=width))
    return {top: neighbors for top in rows
            if (neighbors := {bottom for bottom in rows if compatible(top, bottom)})}


def component_sizes(graph):
    unseen = set(graph)
    sizes = Counter()
    while unseen:
        pending = [unseen.pop()]
        size = 0
        while pending:
            current = pending.pop()
            size += 1
            for neighbor in graph[current]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    pending.append(neighbor)
        sizes[size] += 1
    return dict(sorted(sizes.items()))


def table_data(path):
    return [tuple(map(int, line.split())) for line in path.read_text().splitlines()
            if line.strip() and not line.lstrip().startswith('#')]


def check(data_root):
    tiles = [tile for tile in product(range(3), repeat=4) if valid_tile(*tile)]
    expected_tiles = [(0, 1, 2, 0), (0, 2, 1, 0), (0, 2, 2, 1),
                      (1, 0, 0, 2), (1, 2, 2, 0), (2, 0, 0, 1),
                      (2, 0, 1, 2), (2, 1, 0, 2)]
    assert tiles == expected_tiles
    results = []
    primary_counts = []
    for width in range(2, 13):
        graph = graph_from_columns(width)
        if width <= 6:
            assert graph == direct_graph(width)
        degrees = Counter(map(len, graph.values()))
        assert degrees[2] == 2 and degrees[1] == 4 * base_count(width - 1) - 4
        assert sum(degrees.values()) == len(graph)
        components = component_sizes(graph)
        expected_components = {3: 2}
        if width > 2:
            expected_components[2] = 2 * base_count(width - 1) - 4
        assert components == expected_components
        assert all(top in graph[bottom] for top in graph for bottom in graph[top])
        assert all(top not in graph[top] for top in graph)
        counts = {row: 1 for row in graph}
        extent = 210 if width in (3, 5) else 60
        for index in range(1, extent + 1):
            counts = {row: sum(counts[neighbor] for neighbor in graph[row]) for row in graph}
            total = sum(counts.values())
            assert total == 4 * (base_count(index) + base_count(width - 1) - 2)
            if width == 5:
                primary_counts.append(total // 4)
        results.append({'width': width, 'active_vertices': len(graph),
                        'directed_edges': sum(map(len, graph.values())),
                        'component_counts': components, 'walk_lengths_checked': extent,
                        'direct_row_pair_check': width <= 6})
    ordered_powers = sorted({2 ** exponent for exponent in range(212)} |
                            {3 * 2 ** exponent for exponent in range(212)})
    for index in range(1, 211):
        assert base_count(index) == ordered_powers[index]
        assert 2 * base_count(index) - 2 == sum(
            2 ** min(position, index - position) for position in range(index + 1))
    for index in range(3, 211):
        assert base_count(index) + 1 == 2 * (base_count(index - 2) + 1) - 1
    triangle_checks = []
    for index in range(3, 17):
        longer = base_count(index - 1) + 1
        shorter = base_count(index - 2) + 1
        accepted = sum(longer + shorter > third and longer + third > shorter
                       and shorter + third > longer
                       for third in range(1, longer + shorter + 1))
        assert accepted == base_count(index) + 1
        triangle_checks.append({'index': index, 'sides': [longer, shorter],
                                'integer_triangles': accepted})
    brute_checks = []
    for height, width in [(2, 2), (2, 3), (3, 2), (3, 3), (2, 4), (4, 2), (3, 4)]:
        accepted = 0
        for entries in product(range(3), repeat=height * width):
            if all(valid_tile(entries[row * width + column],
                              entries[row * width + column + 1],
                              entries[(row + 1) * width + column],
                              entries[(row + 1) * width + column + 1])
                   for row in range(height - 1) for column in range(width - 1)):
                accepted += 1
        assert accepted == 4 * (base_count(height - 1) + base_count(width - 1) - 2)
        brute_checks.append({'height': height, 'width': width,
                             'arrays_examined': 3 ** (height * width), 'valid_arrays': accepted})
    for index in range(4, 211):
        assert primary_counts[index - 1] == (primary_counts[index - 2]
                + 2 * primary_counts[index - 3] - 2 * primary_counts[index - 4])
    for index in range(1, 211):
        coefficient = primary_counts[index - 1]
        if index >= 2:
            coefficient -= primary_counts[index - 2]
        if index >= 3:
            coefficient -= 2 * primary_counts[index - 3]
        if index >= 4:
            coefficient += 2 * primary_counts[index - 4]
        assert coefficient == {1: 6, 2: 1, 3: -11}.get(index, 0)
    comparisons = {}
    if data_root:
        primary = table_data(data_root / 'b209723.txt')
        assert len(primary) == 210
        assert all(primary_counts[index - 1] == value for index, value in primary)
        comparisons['A209723_bfile_terms'] = len(primary)
        rectangular = table_data(data_root / 'b209727.txt')
        coordinate_pairs = [(index, diagonal - index)
                            for diagonal in range(2, 100)
                            for index in range(1, diagonal)]
        assert len(rectangular) == 1512
        for (index, value), (height_index, width_index) in zip(rectangular, coordinate_pairs):
            assert index >= 1
            assert value == base_count(height_index) + base_count(width_index) - 2
        comparisons['A209727_bfile_terms'] = len(rectangular)
        for identifier, column in [('A209721', 2), ('A209722', 3), ('A209723', 4),
                                   ('A209724', 5), ('A209725', 6), ('A209726', 7)]:
            entry_path = data_root / (identifier + '.json')
            if entry_path.exists():
                entry = json.loads(entry_path.read_text())[0]
                values = list(map(int, entry['data'].split(',')))
                offset = int(entry['offset'].split(',')[0])
                assert offset == 1
                assert all(value == base_count(index) + base_count(column) - 2
                           for index, value in enumerate(values, start=offset))
                comparisons[identifier + '_entry_terms'] = len(values)
        for identifier in ['A029744', 'A027383']:
            entry_path = data_root / (identifier + '.json')
            if entry_path.exists():
                entry = json.loads(entry_path.read_text())[0]
                values = list(map(int, entry['data'].split(',')))
                offset = int(entry['offset'].split(',')[0])
                for index, value in enumerate(values, start=offset):
                    expected = (1 if index == 1 else base_count(index - 1)) if identifier == 'A029744' else (1 if index == 0 else 2 * base_count(index) - 2)
                    assert value == expected
                comparisons[identifier + '_entry_terms'] = len(values)
    return {'status': 'all_checks_passed', 'tile_cases_examined': 81, 'valid_tiles': tiles,
            'row_graphs': results, 'direct_array_checks': brute_checks,
            'primary_prefix': primary_counts[:12], 'oeis_comparisons': comparisons,
            'corollary_checks': {'beck_first_indices': [1, 210],
                                 'peterson_recurrence_indices': [3, 210],
                                 'diagonal_indices': [1, 210],
                                 'triangle_checks': triangle_checks},
            'proof_scope': 'Finite checks of tiles, graph components, walks, arrays, and corollary identities. The all-dimension results have written proofs in note.tex; the linked Lean declaration covers the five-column specialization.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = check(args.data)
    content = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(content)
    print(content)
