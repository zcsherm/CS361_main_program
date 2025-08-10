import random
from time import sleep

FILE_NAME = "shuffler.txt"

# EXAMPLE_INPUT = "size=9999"
# EXAMPLE_INPUT = "size=100,seed=892374,algorithm=biased"


class DeckShuffler:
    def __init__(self, size, seed=None, algorithm="random"):
        self.size = size
        self.deck = [i for i in range(self.size)]
        if seed:
            random.seed(seed)
        self.algorithm = algorithm

    def shuffle(self):
        if self.algorithm == "biased":
            self.biased_shuffle()
        else:
            self.true_random()

    # Each permutation is exactly as likely
    # Fisher Yates Shuffle
    def true_random(self):
        for i in range(len(self.deck) - 1, 0, -1):
            rand = random.randint(0, i)
            self.deck[i], self.deck[rand] = self.deck[rand], self.deck[i]

    # No element appears in its starting position - Feels more random
    # Derangement Shuffle
    def biased_shuffle(self):
        # First true random it
        self.true_random()
        # Get each fixed point
        fixed_points = [i for i in range(len(self.deck)) if self.deck[i] == i]

        # Remove fixed points
        for fixed_point in fixed_points:
            if self.deck[fixed_point] != fixed_point:
                # No longer a fixed point, got swapped earlier
                continue
            # Swap is guaranteed to not cause a new fixed point
            rand = random.choice([i for i in range(len(self.deck)) if i != fixed_point])
            self.deck[fixed_point], self.deck[rand] = self.deck[rand], self.deck[fixed_point]

        fixed_points = [i for i in range(len(self.deck)) if self.deck[i] == i]

    def write_deck(self, file_name):
        response = ",".join([str(x) for x in self.deck])
        print(f"Sending Response: {response}")
        with open(file_name, 'w') as f:
            f.write(response)


def read_request(file_name):
    while True:
        with open(file_name, 'r') as f:
            line = f.readline().strip()
            if line and line[3] and line[0:4] == "size":
                return line
        sleep(.1)


def parse_request(request):
    # This input handling/parsing could be better (like using a dictionary)
    # but it's small enough it's just not worth worrying about (3 inputs)
    size = 10
    seed = None
    algorithm = "random"
    try:
        arr = request.split(",")
        for x in arr:
            x = x.split("=")
            if x[0] == "size":
                size = int(x[1])
            if x[0] == "seed":
                seed = int(x[1])
            if x[0] == "algorithm":
                algorithm = x[1]
    except:
        print("ERROR IN INPUT HANDLING")
        return False, False, False

    return size, seed, algorithm


def write_error(file_name):
    with open(file_name, 'w') as f:
        f.write("ERROR")


def main():
    while True:
        request = read_request(FILE_NAME)
        print(f"Request Received: {request}")
        size, seed, algorithm = parse_request(request)

        if not size:
            write_error(FILE_NAME)
            continue

        shuffler = DeckShuffler(size, seed, algorithm)
        shuffler.shuffle()

        shuffler.write_deck(FILE_NAME)


if __name__ == '__main__':
    main()