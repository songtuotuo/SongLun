def run_formula(dv, param=None):
    defult_param = {}
    if not param:
        param = defult_param

    NetProfitGrowRate = dv.add_formula('NetProfitGrowRate',
                         "(TTM(net_profit)/Delay(TTM(net_profit),1)) - 1" ,is_quarterly=False)
    return NetProfitGrowRate