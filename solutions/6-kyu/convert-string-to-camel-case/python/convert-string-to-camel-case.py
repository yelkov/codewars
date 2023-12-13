def to_camel_case(text):
    if text[:1] != '-' and text[:1] != '_':
        return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
    else:
        return text[1:2] + text.title()[2:].replace('_', '').replace('-', '')
    
#2nd solution:

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')