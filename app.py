
from nlp_parser import parse_input

def main():
    print("Welcome to the AI Calculator!")


    while True:
        user_input = input("Enter your expression (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break


        print(parse_input(user_input))


if __name__=="__main__":
    main()