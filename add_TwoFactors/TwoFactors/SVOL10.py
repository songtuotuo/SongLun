def run_formula(dv, param=None):
    defult_param = {'t': 10}
    if not param:
        param = defult_param

    t = param['t']
    VOL10 = dv.add_formula("VOL10_j",
                         "Ts_Mean(turnover_ratio,10)",
                         is_quarterly=False, )
    SVOL10 = dv.add_formula("SVOL10", "-1*StdDev(Ts_Mean(turnover_ratio,%s),%s)"
                            %(t,t),is_quarterly=False,)
    return SVOL10