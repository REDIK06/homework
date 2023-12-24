from hello import Hello


class NewClass(Hello):
    def __init__(self):
        super().__init__()

    def tptint(self):
        print("NewClass")