import pandas
import numpy


def logic_power(row_from_pandas_df, pp_dict, columns):
    min_rival_name = row_from_pandas_df[columns].astype(float).idxmin(skipna=True)
    min_rival_price = row_from_pandas_df[columns].astype(float).min(skipna=True)
    purchase_price = row_from_pandas_df['url']
    min_percent = round(min_rival_price / purchase_price - 1, 3) * 100
    margin = 0
    best_margin = row_from_pandas_df['min_%']
    rule_type = ''

    for key, value in pp_dict.items():
        if type(key) != int:
            break

        margin = value

        if purchase_price > key:
            continue
        if purchase_price <= key:
            break

    if min_rival_name in pp_dict['top_rivals']:
        rule_type = 'у топ дешево, у не топ дешево - автонаценка'
        if min_percent > ((margin - 1) * 100) * (pp_dict['top'] / 100):
            margin = min_percent * 0.9 / 100 + 1
            rule_type = 'упали под топ конкурента'
        else:

            min_rival_name = row_from_pandas_df[[x for x in columns if x not in pp_dict['top_rivals']]].astype(float).idxmin(skipna=True)
            min_rival_price = row_from_pandas_df[[x for x in columns if x not in pp_dict['top_rivals']]].astype(float).min(skipna=True)
            min_percent = round(min_rival_price / purchase_price - 1, 3) * 100

            if min_percent > ((margin - 1) * 100) * (pp_dict['other'] / 100):
                margin = min_percent * 1 / 100 + 1
                rule_type = 'у топ дешево, упали под не топ'

        return (round(purchase_price * margin, -1) - 1, rule_type, min_rival_name)

    if min_rival_name not in pp_dict['top_rivals']:
        rule_type = 'у НЕ топ дешево, у топ дешево - автонаценка'
        if min_percent > ((margin - 1) * 100) * (pp_dict['other'] / 100):
            margin = min_percent * 1 / 100 + 1
            rule_type = 'упали под не топ'
        else:
            min_rival_name = row_from_pandas_df[pp_dict['top_rivals']].astype(float).idxmin(skipna=True)
            min_rival_price = row_from_pandas_df[pp_dict['top_rivals']].astype(float).min(skipna=True)
            min_percent = round(min_rival_price / purchase_price - 1, 3) * 100

            if min_percent > ((margin - 1) * 100) * (pp_dict['top'] / 100):
                margin = min_percent * 1 / 100 + 1
                rule_type = 'у НЕ топ дешево, упали под топ'

        return (round(purchase_price * margin, -1) - 1, rule_type, min_rival_name)
