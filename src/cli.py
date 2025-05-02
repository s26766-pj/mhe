import argparse
from io_utils import read_instance
from model import ThreePartitionProblem
from enumerator import brute_force_search
from hill_climb import hill_climbing_deterministic, hill_climbing_stochastic
# from tabu_search import tabu_search
# from simulated_annealing import simulated_annealing
# from genetic import genetic_algorithm


def main():
    parser = argparse.ArgumentParser(
        description="3-Partition Problem Solver"
    )
    subparsers = parser.add_subparsers(
        title="algorithms",
        dest="algorithm",
        required=True
    )

    brute_parser = subparsers.add_parser(
        "brute", help="Algorytm pełnego przeglądu"
    )
    brute_parser.add_argument(
        "-i", "--input", required=False,
        help="Ścieżka do pliku z instancją (domyślnie stdin)"
    )

    hc_det_parser = subparsers.add_parser(
        "hc_det", help="Hill-climbing deterministyczny"
    )
    hc_det_parser.add_argument(
        "-i", "--input", required=False,
        help="Plik z instancją"
    )
    hc_det_parser.add_argument(
        "--time-limit-seconds", type=int, default=60,
        help="Maksymalny czas działania algorytmu w sekundach"
    )

    hc_rand_parser = subparsers.add_parser(
        "hc_rand", help="Hill-climbing stochastyczny"
    )
    hc_rand_parser.add_argument(
        "-i", "--input", required=False,
        help="Plik z instancją"
    )
    hc_rand_parser.add_argument(
        "--time-limit-seconds", type=int, default=60,
        help="Maksymalny czas działania algorytmu w sekundach"
    )

    tabu_parser = subparsers.add_parser(
        "tabu", help="Algorytm Tabu Search"
    )
    tabu_parser.add_argument("-i", "--input", required=False)
    tabu_parser.add_argument("--tabu-size", type=int, default=50)

    sa_parser = subparsers.add_parser(
        "sa", help="Algorytm symulowanego wyżarzania"
    )
    sa_parser.add_argument("-i", "--input", required=False)
    sa_parser.add_argument("--schedule", choices=["linear", "exp", "log"], default="linear")

    ga_parser = subparsers.add_parser(
        "ga", help="Algorytm genetyczny"
    )
    ga_parser.add_argument("-i", "--input", required=False)
    ga_parser.add_argument("--pop-size", type=int, default=100)
    ga_parser.add_argument("--crossover", choices=["one_point","uniform"], default="one_point")
    ga_parser.add_argument("--mutation", choices=["swap","reassign"], default="swap")

    args = parser.parse_args()
    elements = read_instance(args.input)
    problem = ThreePartitionProblem(elements)

    solution = None

    match args.algorithm:
        case "brute":
            solution = brute_force_search(problem)
        case "hc_det":
            solution = hill_climbing_deterministic(
                problem, time_limit_seconds=args.time_limit_seconds
            )
        case "hc_rand":
            solution = hill_climbing_stochastic(
                problem, time_limit_seconds=args.time_limit_seconds
            )
        # case "tabu":
        #     solution = tabu_search(
        #         problem, tabu_size=args.tabu_size
        #     )
        # case "sa":
        #     solution = simulated_annealing(
        #         problem, schedule=args.schedule
        #     )
        # case "ga":
        #     solution = genetic_algorithm(
        #         problem,
        #         population_size=args.pop_size,
        #         crossover_method=args.crossover,
        #         mutation_method=args.mutation
        #     )
        case _:
            parser.error(f"Nieznany algorytm: {args.algorithm}")

    partitions = solution.as_partitions()
    print("Dane: ", elements)
    print("Rozwiązanie:")
    for idx, part in enumerate(partitions, start=1):
        print(f"   Partycja {idx} -> {part}")


if __name__ == "__main__":
    main()
