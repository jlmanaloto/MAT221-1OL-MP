import re


def function_validation(f: str):
    pattern = r'^[0-9a-zA-Z\.\,\+\-\*/\^\(\)=\s]*$'
    return bool(re.fullmatch(pattern, f))