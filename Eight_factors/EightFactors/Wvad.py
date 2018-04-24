def run_formula(dv, param=None):
    defult_param = {'t': 24}
    if not param:
        param = defult_param
    t = param['t']

    Wvad = dv.add_formula('Wvad',
                         "Ts_Sum(((close-open)/(high-low))*volume,%s)" %t, is_quarterly=False)
    return Wvad