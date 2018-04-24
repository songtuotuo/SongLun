def run_formula(dv, param=None):
    defult_param = {'t': 5}
    if not param:
        param = defult_param
    t = param['t']
    VOL5 = dv.add_formula('VOL5',
                         "Ts_Mean(turnover_ratio,%s)" %t, is_quarterly=False)
    return VOL5