from src.load_data import load_all_viruses

def main():
    directory = "data"
    mamalian_sequences, bacterial_sequences = load_all_viruses(directory)
    print(mamalian_sequences)
    print(bacterial_sequences)

if __name__ == '__main__':
    main()