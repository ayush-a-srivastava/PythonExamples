# Program to search for the word "test" in "test.txt"
# and write matches with row number into "result.txt"

def search_and_save(keyword, input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for row_number, line in enumerate(infile, start=1):
                if keyword in line:
                    # Write to result.txt: keyword and row number
                    outfile.write(f"Found '{keyword}' in line {row_number}: {line}")
        print(f"Search complete. Results are saved in '{output_file}'.")
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")

# Example usage
search_and_save("test", "test.txt", "result.txt")
