from FileReader import FileReader


class LexicalAnalyzer:
    def __init__(self, file):
        self.file_reader = FileReader(file)
        self.token_remaining = False

    def next_token(self):
        word = self.file_reader.read()
        if not word:
            return None
        print(word)
        return word
