def function(a, b):
    try:
        b = int(b)
        return a + b
    except ValueError:
        return "Error: Cannot add integer and string"