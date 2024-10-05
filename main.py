from src.load_data import load_all_fastas

def main():
    directory = "data"
    sequences = load_all_fastas(directory)
    print(sequences)

if __name__ == '__main__':
    main()