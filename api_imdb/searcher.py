import sys
from movies import MovieSearcher


def main(params):
    api = MovieSearcher(params[0])
    exit = False
    while not exit:
        print("{}\n\nEntre uma chave:\n".format(api.info))
        text = input()
        if text == 'exit':
            exit = True
            continue
        print("\n\n{}\n\n".format(api.getInfo(text)))
        
        
def run(params):
    api = MovieSearcher(params[0])
    print(api.data)
        
        

if __name__ == "__main__":
    run(sys.argv[1:])

