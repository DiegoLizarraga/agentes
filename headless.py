from model import SimpleModel

def run_headless():
    m = SimpleModel(5, 10, 10)
    print("Initial:")
    m.show_stats()
    for i in range(3):
        m.step()
        print(f"Step {i + 1}:")
        m.show_stats()

if __name__ == "__main__":
    run_headless()