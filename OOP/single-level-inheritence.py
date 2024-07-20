class BIKE:

    def __init__(self, model):
        self.model = model

    def display(self):
        print(f"Hello")


class EBIKE(BIKE):

    def __init__(self,model):

        super().__init__(model)

    def display(self):
        super().display()


ebike1 = EBIKE("kawasaki")

print(ebike1.model)
ebike1.display()