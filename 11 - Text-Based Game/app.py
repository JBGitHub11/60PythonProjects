import json

def load_game_data():
    with open("game_data.json", "r") as f:
        game_data = json.load(f)
    return game_data

def play_game(game_data):
    current_room = game_data["rooms"][game_data["start_room"]]

    while True:
        print(current_room["description"])
        choices = list(current_room["choices"].keys())
        print("Your choices are:", ", ".join(choices))
        choice = input("Enter your choice: ").lower()

        if choice in current_room["choices"]:
            next_room_key = current_room["choices"][choice]
            if next_room_key in game_data["rooms"]:
                current_room = game_data["rooms"][next_room_key]
            else:
                game_state = game_data["game_states"][next_room_key]
                print(game_state["description"])
                break
        else:
            print("Invalid choice. Try again.")

def main():
    game_data = load_game_data()
    play_game(game_data)

if __name__ == "__main__":
    main()