import random

def gen_event():
    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim']
    
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield(name, action)

def consume_event(events: list[tuple[str,str]]):
    while(len(events) > 0):
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        name, action = next(event_generator)
        print(f"Event {i}: Player {name} did action {action}")

    stored_events = []
    for x in range(10):
        stored_events.append(next(event_generator))
    
    print(f"Built list of 10 events: {stored_events}")

    for event in consume_event(stored_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {stored_events}")

if __name__ == "__main__":
    main()