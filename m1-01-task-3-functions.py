def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def cleaned_version(value):
    if not isinstance(value, str):
        return None
    return value.strip().lower()


checking_lst = [33, "  dyvAJSj", "hedgd", "23.56", 45, "igde", "555.76"]
for i in checking_lst:
    print(is_float(i))
    print(cleaned_version(i))