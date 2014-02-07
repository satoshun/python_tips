def reverse_mapping(mapping):
    reverse_mapping = {}
    for key, value in mapping.items():
        reverse_mapping.setdefault(value, []).append(key)
    return reverse_mapping
