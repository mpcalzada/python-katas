class User:

    def __init__(self) -> None:
        self.rank = -8
        self.progress = 0

    def rank(self):
        return self.rank

    def progress(self):
        pass

    def inc_progress(self, rank):
        pass

    def inc_progress(self, rank, ):
        if rank < -8 or rank > 8 or rank == 0: raise ValueError("The rank is not valid")
        if self.rank == 8:
            self.progress = 0
            return
        diff = rank -self.rank
        value = -1 if diff > 0 else 1
        diff += value if self.rank < 0 and rank > 0 else 0
        diff += value if self.rank > 0 and rank < 0 else 0
        self.progress += self.__get_points(diff)
        self.__inc_rank()

    def __get_points(self, diff):
        if diff < -1: return 0
        if diff == -1: return 1
        if diff == 0: return 3
        if diff > 0: return 10 * diff * diff

    def __inc_rank(self):
        if self.progress < 100: return
        if self.rank == 8: 
            self.progress = 0
            return
        self.rank += 1 if self.rank != -1 else 2
        self.progress = self.progress - 100 if self.rank < 8 else 0
        self.__inc_rank()
            
    


if __name__ == '__main__':
    user = User()
    print(f"Current: {user.rank} Expected: -8")
    print(f"Current: {user.progress} Expected: 0")
    user.inc_progress(-7)
    print(f"Current: {user.progress} Expected: 10")
    user.inc_progress(-5)
    print(f"Current: {user.progress} Expected: 0")
    print(f"Current: {user.rank} Expected: -7")
    user.inc_progress(1)
    print(f"Current: {user.progress} Expected: 0")
    print(f"Current: {user.rank} Expected: -7")

    user.rank = 1
    user.progress = 20
    user.inc_progress(-1)
    print(user.progress)