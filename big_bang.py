import json


def generate():
    result = []

    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            result.append("BIGBANG")
        elif n % 3 == 0:
            result.append("BIG")
        elif n % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(n))

    return result


def main():
    result = generate()
    with open("output.json", "w") as f:
        json.dump(result, f, indent=2)

    print(f"Wrote {len(result)} entries to output.json")


if __name__ == "__main__":
    main()
