def run_formula(dv, param=None):
    defult_param = {}
    if not param:
        param = defult_param

    FixedAssetsTRate = dv.add_formula('FixedAssetsTRate',
                         "TTM(oper_rev)/Ts_Mean((fix_assets+proj_matl+const_in_prog),4)" ,is_quarterly=False)
    return FixedAssetsTRate