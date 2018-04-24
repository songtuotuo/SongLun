def run_formula(dv, param=None):
    defult_param = {'t1': 1, 't2': 60}
    if not param:
        param = defult_param

    Variance60 = dv.add_formula('Variance60',
                         "StdDev(Return(close,%s),%s)^2" %(
                         param['t1'], param['t2']),is_quarterly=False)
    return Variance60