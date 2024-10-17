import argparse
import random

def generate_trace_file(filename, num_commands, max_amount, seed=None):
    """
    Generate a trace file with specified number of random read and write commands, optionally using a seed.

    Args:
    filename (str): Name of the file to write the trace commands.
    num_commands (int): Number of commands to generate.
    max_amount (int): Maximum value for the AMOUNT parameter in commands.
    seed (int, optional): Seed for the random number generator to ensure reproducibility.
    """
    if seed is not None:
        random.seed(seed)  # Set the random seed

    with open(filename, 'w') as file:
        for _ in range(num_commands):
            # Randomly choose between 'randread' and 'randwrite'
            command = random.choice(['randread', 'randwrite'])
            # Generate a random amount between 1 and max_amount
            amount = random.randint(1, max_amount)
            # Write the command to the file
            file.write(f"{command} {amount}\n")

def main():
    parser = argparse.ArgumentParser(description="Generate a trace file for cache simulation.")
    parser.add_argument("--fname", type=str, help="Path to the trace file to be generated.")
    parser.add_argument("--numcmds", type=int, help="Number of commands to generate.", default=1000)
    parser.add_argument("--maxamt", type=int, help="Maximum value for the AMOUNT parameter in commands.", default=1000)
    parser.add_argument("--seed", type=int, help="Seed for the random number generator to ensure reproducibility.", default=None)

    args = parser.parse_args()

    # Generate the trace file with the given arguments
    generate_trace_file(args.fname, args.numcmds, args.maxamt, args.seed)

if __name__ == "__main__":
    main()

