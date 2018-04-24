def run_formula(dv, param=None):
    defult_param = {'t1': 35, 't2': 60, 't3': 60, 't4': 60}
    if not param:
        param = defult_param

    Ad1 = dv.add_formula('Ad1',
                         "-1 * Rank(Ts_Sum(Correlation(volume, (high - low), %s), %s) + Ts_Sum( (1 + (close / Ts_Min(close, %s))), %s))"% (
                         param['t1'], param['t2'], param['t3'], param['t4']),
                         is_quarterly=False)

    return Ad1
