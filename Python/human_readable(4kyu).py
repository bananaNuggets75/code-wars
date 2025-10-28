def format_duration(seconds):
    if seconds == 0:
        return "now"

    # Define units of time
    units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1),
    ]

    parts = []

    # Calculate each unit
    for name, unit_seconds in units:
        value = seconds // unit_seconds
        if value:
            seconds -= value * unit_seconds
            part = f"{value} {name}" + ("s" if value > 1 else "")
            parts.append(part)

    # Combine with commas and "and"
    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return " and ".join(parts)
    else:
        return ", ".join(parts[:-1]) + " and " + parts[-1]
