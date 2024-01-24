def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()        
        print(file_contents)
if __name__ == "__main__":
    main()

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))
if __name__ == "__main__":
    main()

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    char_counts= {}
    
    for char in file_contents.lower():
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
        
    print(char_counts)

if __name__ == "__main__":
    main()


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    char_counts= {}    
    for char in file_contents.lower():
        if char.isalpha():
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1
    sorted_counts = sorted(char_counts.items(), key =lambda item: item[1], reverse=True)
    for char, count in sorted_counts:
         print(f"The '{char}' character was found {count} times")

if __name__ == "__main__":
    main()
