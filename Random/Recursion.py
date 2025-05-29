def add_one(num):
    print(f"Current number: {num}")

    if num >= 9:
        result = num + 1
        print(f"Reached 9 or greater. Final result: {result}")
        return result

    total = num + 1
    print(f"Adding 1. New total: {total}")

    return add_one(total)


# Test the function
result = add_one(0)
print(f"Final result: {result}")