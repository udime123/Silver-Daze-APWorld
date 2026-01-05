import cProfile as P
import Main as M
import Generate as G
import pstats
import os

CUSTOM_OUT = True

pr = P.Profile()
pr.enable()
M.main(G.main()[0], 0)  # force seed 0
pr.disable()

if CUSTOM_OUT:
    def print_stats(stat_list: list, **keys) -> None:
        print_keys = {"ncalls": "ncalls", **keys}  # "filename:lineno(function)"
        f_key = ""
        for display, attr in print_keys.items():
            padding = max(len(display), *[len(str(getattr(data, attr))) for _, _, data in stat_list])
            f_key += "{:>" + str(padding+1) + "}"
        print(f_key.format(*print_keys.keys()) + " filename:lineno(function)")
        for _, name, data in stat_list:
            f_line = f_key.format(*[getattr(data, attr) for attr in print_keys.values()])
            print(f_line + f" {data.file_name.removeprefix(os.getcwd())}:{data.line_number}({name})")

    pp = pstats.Stats(pr).get_stats_profile()

    tottime = sorted(
        [(value.tottime, key, value) for key, value in pp.func_profiles.items()],
        reverse=True
    )[:10]

    cumtime = sorted(
        [(value.cumtime, key, value) for key, value in pp.func_profiles.items()],
        reverse=True
    )[:20]

    print()
    print(f"Profiling done, took {pp.total_tt} time")
    print_stats(tottime, tottime="tottime", percall="percall_tottime")
    print()
    print_stats(cumtime, cumtime="cumtime", percall="percall_cumtime")
else:
    ps = pstats.Stats(pr)
    ps.sort_stats('tottime').print_stats(10)
    ps.sort_stats('cumtime').print_stats(20)
