from src.load_data import load_all_fastas

def main():
    directory = "data"
    mamalian_sequences, bacterial_sequences = load_all_fastas(directory)
    print(mamalian_sequences)
    print(bacterial_sequences)

if __name__ == '__main__':
    main()