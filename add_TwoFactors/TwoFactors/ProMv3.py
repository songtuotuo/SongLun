def run_formula(dv, param=None):
    defult_param = {'t': 3}
    if not param:
        param = defult_param

    t = param['t']

    ProMv3 = dv.add_formula("ProMv3", "Ts_Mean(tot_profit/total_mv,%s)" %t,
                        is_quarterly=True)
    return ProMv3