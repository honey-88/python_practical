class Idea:
    def idea_display(self):
        print("welcome to Idea")


class vodafone:
    def vodafone_display(self):
        print("welcome to vodafone")

class VI(Idea,vodafone):
    def display(self):
        self.idea_display()
        self.vodafone_display()
        print("welcome to VI - 2022")

vi = VI()
vi.display()
