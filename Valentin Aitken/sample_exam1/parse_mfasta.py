def dic_mfasta(filepath) -> dict:
    with open(filepath, "r") as input_data:
        result = {}
        for line in input_data:
            current = line.strip()
            if current[0] == '>':
                current_key = current[1:]
            else:
                if current_key in result:
                    result[current_key] = result[current_key] + current
                else:
                    result[current_key] = current
        return result
    return None
