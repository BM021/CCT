input_str = '{"ru": 1234, "uz": 123}'

pairs = input_str.split(', ')
result_dict = {key.strip('"'): int(value) if value.isdigit() else value.strip('"') for key, value in (pair.split(': ') for pair in pairs)}

print(pairs)
