import sys

def show_args(args: list[str]) -> None:
    print('=== Command Quest ===')
    print(f"Program name: {args[0]}")

    if len(args) == 1:
        print('No arguments provided!')
    else:
        print(f"Arguments received: {len(args) - 1}")
        
        i = 1
        for arg in args[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {len(args)}")
    
def main() -> None:
    show_args(sys.argv)

if __name__ == "__main__":
    main()





#=== Command Quest ===
#Program name: ft_command_quest.py
#No arguments provided!
#Total arguments: 1
#$> python3 ft_command_quest.py hello world 42
#=== Command Quest ===
#Program name: ft_command_quest.py
#Arguments received: 3
#Argument 1: hello
#Argument 2: world
#Argument 3: 42
#Total arguments: 4
#$> python3 ft_command_quest.py "Data Quest"
#=== Command Quest ===
#Program name: ft_command_quest.py
#Arguments received: 1
#Argument 1: Data Quest
#Total arguments: 2