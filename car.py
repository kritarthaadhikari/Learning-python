class car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print(f"You are driving {self.model}!")

    def stop(self):
        print("you stop")

    def change_gears(self):
        print(f"You are changing gears in {self.model}")

    def describe_car(self):
        print(f"You bought a {self.year} {self.color} {self.model} ")