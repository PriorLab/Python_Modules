import random


def gen_event():
    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim']
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list[tuple[str, str]]):
    while (len(events) > 0):
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: PLayer {name} did action {action}")

    ten_events: list[tuple[str, str]] = []
    generator2 = gen_event()
    for i in range(10):
        ten_events.append(next(generator2))
    print(f"Built list of 10 events: [{ten_events}]")
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
