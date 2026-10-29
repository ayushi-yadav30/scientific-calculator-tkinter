ALLOWED_CHARS = set("0123456789+-*/. ")


def calculate(expression):
    # Sirf allowed characters hi expression me hone chahiye
    if not expression or not set(expression) <= ALLOWED_CHARS:
        return "Error"

    try:
        result = eval(expression)
        return str(result)
    except ZeroDivisionError:
        return "Error"
    except Exception:
        return "Error"