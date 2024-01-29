def sum(a,b):
    try:
        return a/b
    except (TypeError , ZeroDivisionError)as err:
        return err
        #print(f"please enter nums {err}")


print(sum(1,0))
