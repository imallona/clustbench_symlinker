import argparse
import os
import wget
import sys

def main():
    parser = argparse.ArgumentParser(description='clustbench dataset slicer')

    parser.add_argument('--output_dir', type=str,
                        help='output directory to store data files.', default=os.getcwd())
    parser.add_argument('--name', type=str, help='name of this module', default='clustbench')
    parser.add_argument('--dataset_generator', type=str, help='dataset generator name, e.g. graves, mnist etc',
                        required = True)
    parser.add_argument('--dataset_name', type=str,
                        help='dataset name, e.g. for `mnist` either `fashion` or `digits`',
                        required = True)
    parser.add_argument('--preexisting_path', type=str,
                        help='path to the pre-populated clustbench datasets (folder) caution full path'
                        required = True)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)
    
    # clone source
    # rather, download
    # https://github.com/gagolews/clustering-data-v1/raw/refs/heads/master/mnist/digits.data.gz

    generator = args.dataset_generator    
    name = args.dataset_name
    origin_path = args.preexisting_path
    module_name = args.name

    # symlinks (to be created)
    symlink_counts =  os.path.join(args.output_dir, f"{module_name}.data.gz")
    symlink_labels = os.path.join(args.output_dir, f"{module_name}.labels0.gz")
                                  
    # source files (the original, pre-existing data)
    source_counts =  os.path.join(args.origin_path, f"{module_name}.data.gz")
    source_labels = os.path.join(args.origin_path, f"{module_name}.labels0.gz")

    try:
        os.symlink(source_counts, symlink_counts)
        os.symlink(source_labels, symlink_labels)
    except FileExistsError:
        print("Symlink already exists.")
    except OSError as e:
        print(f"Error: {e}"



if __name__ == "__main__":
    main()
