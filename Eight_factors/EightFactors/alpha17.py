def run_formula(dv, param=None):
    defult_param = {'t1': 15, 't2': 5}
    if not param:
        param = defult_param

    alpha17 = dv.add_formula('alpha17',
                         "Rank((vwap - Max(vwap, %s)))^Delta(close, %s)" %(
                         param['t1'], param['t2']),is_quarterly=False)
    return alpha17