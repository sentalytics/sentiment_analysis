def handle_error(msg, e=None):
    # do some sort of logging
    print(f'Error: {msg} - {e}')
    raise e
