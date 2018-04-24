def run_formula(dv, param=None):
    defult_param = {'t': 20}
    if not param:
        param = defult_param

    t = param['t']

    Ad2 = dv.add_formula("Ad2", "-1*(Rank(StdDev(Abs((close-open)),%s))+Correlation(close, open, %s))" % (t, t),
                        is_quarterly=False)
    return Ad2

