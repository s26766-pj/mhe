import argparse
from io_utils import read_instance
from model import ThreePartitionProblem
from enumerator import brute_force_search
from hill_climb import hill_climbing_deterministic, hill_climbing_stochastic
from simulated_annealing import simulated_annealing
from tabu_search import tabu_search


def main():
    parser = argparse.ArgumentParser(
        description="3-Partition Problem Solver"
    )
    subparsers = parser.add_subparsers(
        title="algorithms",
        dest="algorithm",
        required=True
    )

    # Brute-force
    brute_parser = subparsers.add_parser(
        "brute", help="Pełny przegląd wszystkich m^n przydziałów"
    )
    brute_parser.add_argument(
        "-i", "--input", required=False,
        help="Ścieżka do pliku z instancją (domyślnie stdin)"
    )

    # Hill-climbing deterministyczny
    hc_det_parser = subparsers.add_parser(
        "hc_det", help="Hill-climbing deterministyczny"
    )
    hc_det_parser.add_argument(
        "-i", "--input", required=False,
        help="Plik z instancją"
    )
    hc_det_parser.add_argument(
        "--time-limit-seconds", type=int, default=60,
        help="Maksymalny czas działania algorytmu (sekundy)"
    )

    # Hill-climbing stochastyczny
    hc_rand_parser = subparsers.add_parser(
        "hc_rand", help="Hill-climbing stochastyczny"
    )
    hc_rand_parser.add_argument(
        "-i", "--input", required=False,
        help="Plik z instancją"
    )
    hc_rand_parser.add_argument(
        "--time-limit-seconds", type=int, default=60,
        help="Maksymalny czas działania algorytmu (sekundy)"
    )

    # Tabu Search
    tabu_parser = subparsers.add_parser(
        "tabu", help="Algorytm Tabu Search"
    )
    tabu_parser.add_argument(
        "-i", "--input", required=False,
        help="Plik z instancją"
    )
    tabu_parser.add_argument(
        "--tabu-size", type=int, default=50,
        help="Rozmiar listy tabu (0 lub brak limitu = nieograniczone)"
    )
    tabu_parser.add_argument(
        "--time-limit-seconds", type=int, default=60,
        help="Maksymalny czas działania algorytmu (sekundy)"
    )

    # Simulated Annealing
    sa_parser = subparsers.add_parser(
        "sa", help="Algorytm symulowanego wyżarzania"
    )
    sa_parser.add_argument(
        "-i", "--input", required=False,
        help="Plik z instancją"
    )
    sa_parser.add_argument(
        "--schedule", choices=["linear", "exponential", "logarithmic"], default="exponential",
        help="Typ harmonogramu chłodzenia"
    )
    sa_parser.add_argument(
        "--initial-temp", type=float, default=None,
        help="Początkowa temperatura (jeśli nie podano, używana jest total/m)"
    )
    sa_parser.add_argument(
        "--sigma", type=float, default=1.0,
        help="Odchylenie standardowe do wyboru sąsiedztwa (rozkład normalny)"
    )
    sa_parser.add_argument(
        "--time-limit-seconds", type=int, default=60,
        help="Maksymalny czas działania algorytmu (sekundy)"
    )
    sa_parser.add_argument(
        "--alpha", type=float, default=None,
        help="Parametr alpha dla harmonogramu chłodzenia (np. wykładniczy)"
    )
    sa_parser.add_argument(
        "--c", type=float, default=None,
        help="Parametr c dla harmonogramu logarytmicznego"
    )

    args = parser.parse_args()
    elements = read_instance(args.input)
    n = len(elements)
    m = n/3
    o = int(m**n)
    print("Liczba możliwych przydziałów: ", o)
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
        case "tabu":
            solution = tabu_search(
                problem,
                tabu_size=args.tabu_size,
                time_limit_seconds=args.time_limit_seconds
            )
        case "sa":
            schedule_params = {}
            if args.alpha is not None:
                schedule_params['alpha'] = args.alpha
            if args.c is not None:
                schedule_params['c'] = args.c
            solution = simulated_annealing(
                problem,
                schedule=args.schedule,
                schedule_params=schedule_params,
                initial_temp=args.initial_temp,
                sigma=args.sigma,
                time_limit_seconds=args.time_limit_seconds
            )
        case _:
            parser.error(f"Nieznany algorytm: {args.algorithm}")

    partitions = solution.as_partitions()
    print("Multizbiór: ", elements)
    print("Rozwiązanie (trojaczki):")
    for idx, part in enumerate(partitions, start=1):
        print(f"   S{idx} = {part}, Σ(S{idx}) = {sum(part)}")


if __name__ == "__main__":
    main()
