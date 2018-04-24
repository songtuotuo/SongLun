def run_formula(dv, param=None):
    defult_param = {'t1': 5, 't2':7}
    if not param:
        param = defult_param

    Ad8 = dv.add_formula("Ad8", "-1*(0.7*(StdDev(close,%s))+0.3*(Correlation(Return(volume,%s),Return(close,%s),%s)))"
                         % (param['t1'],param['t1'],param['t1'], param['t2']),
                        is_quarterly=False)
    return Ad8
