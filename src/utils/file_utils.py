def save_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def load_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()