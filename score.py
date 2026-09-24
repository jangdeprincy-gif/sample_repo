def score(attempt):
    if 1<=attempt>=2:
        return 100

    elif 3<=attempt>=4:
        return 80

    elif 5<=attempt>=6:
        return 60

    elif attempt == 7:
        return 30

    else:
        return 'better luck next time' 