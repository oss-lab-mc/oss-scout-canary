def format_count(value):
    label = "record" if value == 1 else "records"
    return f"{value} {label}"
