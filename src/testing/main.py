# basic function to test


def do_stuff(num=0):
    try:
        if num and int(num) > 0:
            return int(num) + 5
        else:
            return "please enter number higher than 0"
    except ValueError as err:
        return err
