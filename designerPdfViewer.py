def designerPdfViewer(h, word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    letters_dict=dict(zip(letters,h))
    height=[letters_dict[i] for i in word]
    max_height=int(max(height))
    lenght=len(word)
    print(max_height*lenght)
h = list(map(int, input().rstrip().split()))
word = input()
result = designerPdfViewer(h, word)

