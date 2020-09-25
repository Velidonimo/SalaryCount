import json
import urllib.request

rate = 0

def getting_rate():
    '''
    Gets a ruble exchange course from openexchangerates.org
    '''
    global rate
    for attempt in range(10):
        try:
            curr_page = urllib.request.urlopen('http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62')
            obj = curr_page.read().decode(encoding='UTF-8')
            content = json.loads(obj)
            rate = round(content['rates']['RUB'], 2)
        except:
            pass
        if rate:
            break


def fill_entries(currency, column, value):
    """
    Fills values
    :param currency: 'rub' or 'dol'
    :param column: int 1-5
    :param value: float
    :return: (entries_dol, entries_rub)
    """
    # calculating the salary per hour
    per_hour = 0
    if column == 0:  # hour
        per_hour = value
    elif column == 1:  # day
        per_hour = value/8
    elif column == 2:  # week
        per_hour = value/40
    elif column == 3:  # month
        per_hour = value/22/8
    elif column == 4:  # year
        per_hour = value/52/40

    # calculating all types of salary
    row = [per_hour, per_hour*8, per_hour*40, per_hour*22*8, per_hour*52*40]
    if currency == 'dol':
        result = (row, [dol * rate for dol in row])
    else:
        result = ([rub/rate for rub in row], row)

    # rounding salary
    rounded_result = (list(map(lambda x: round(x, 2), result[0])), list(map(lambda x: round(x, 2), result[1])))
    return rounded_result


def check_input(entries1, entries2):
    """
    Checks the incoming values
    :param entries1: list of floats (dol entries)
    :param entries2: list of floats (rub entries)
    :return: True if params are OK, else False
    """
    # check the length
    if len(entries1)!=5 or len(entries2)!=5:
        return False
    # check the float
    try:
        entries1 = list(map(lambda x: float(x) if x else None, entries1))
        entries2 = list(map(lambda x: float(x) if x else None, entries2))
    except ValueError:
        return False
    # check for a single positive value
    values_count = 0
    for row in [entries1, entries2]:
        for entry in row:
            if entry:
                values_count += 1
                if entry < 0:
                    return False
    if values_count != 1:
        return False

    return True


def convert_salary(entries_dol, entries_rub):
    """
    Converts salary
    :param entries_dol: list of float. Len = 5
    :param entries_rub: list of float. Len = 5
    :return: (entries_dol, entries_rub)
             or 'ErrorURL' if fail to get ration
             or 'ErrorIncome' if got wrong params
    """

    # trying to get rate
    if not rate:
        getting_rate()
        if not rate:
            return 'ErrorURL'

    # checking for wrong input
    if not check_input(entries_dol, entries_rub):
        return 'ErrorIncome'

    #convert to float
    entries_dol = list(map(lambda x: float(x) if x else 0.0, entries_dol))
    entries_rub = list(map(lambda x: float(x) if x else 0.0, entries_rub))

    # getting converted values
    column = 0
    result = []
    for entry in entries_dol:
        if entry:
            result = fill_entries('dol', column, entry)
        column += 1
    column = 0
    for entry in entries_rub:
        if entry:
            result = fill_entries('rub', column, entry)
        column += 1

    return result


if __name__ == '__main__':
    print(convert_salary(['1','0','','',''],['0','0','','','']))
