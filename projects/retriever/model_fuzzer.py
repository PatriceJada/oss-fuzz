import sys
import atheris
import random
import string
from io import StringIO
from contextlib import redirect_stdout
import retriever

def fuzzed_retriever(input_bytes):
    try:
        # Generate random arguments for the retriever CLI
        random_args = generate_random_args(input_bytes)
        
        # Redirect stdout to capture any output
        with StringIO() as buf, redirect_stdout(buf):
            # Replace sys.argv with the random arguments
            sys.argv = random_args
            
            # Call the retriever main function
            retriever.main()
            
            # Optionally, you can check the captured output in buf.getvalue()
            output = buf.getvalue()
            # Process or analyze the output if needed
    except Exception as e:
        # Handle exceptions to continue fuzzing
        pass

def generate_random_args(input_bytes):
    # Example function to generate random arguments
    args = ['retriever']  # Start with the script name
    commands = ['install', 'update', 'citation', 'license', 'new', 'reset', 'autocreate', 'ls', 'commit', 'log']
    flags = ['--quiet', '--debug']
    
    # Generate a random command
    command = random.choice(commands)
    args.append(command)
    
    # Add random flags
    if random.choice([True, False]):
        args.append(random.choice(flags))
    
    # Add random dataset names or file paths if necessary
    if command in ['citation', 'license']:
        args.append('--dataset')
        args.append('sample_dataset')
    
    # Optionally, add some random values for other arguments
    if command in ['autocreate', 'new']:
        args.append('--filename')
        args.append(generate_random_string(10) + '.py')
    
    return args

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main_fuzz():
    atheris.Setup(sys.argv, fuzzed_retriever)
    atheris.Fuzz()

if __name__ == "__main__":
    main_fuzz()
