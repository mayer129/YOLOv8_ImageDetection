# Converts YOLOv8 predicted labels back to expected output
# Aggregates individual files to singular output file, removing leading 0's from <image_id>
# Also increments <class> value by 1, as they were decremented in YOLOv8 to conform with expected 0 index
import os
import glob


def aggregate_predictions(input_dir, output_file):
    """
    Aggregates predictions from individual .txt files into a single output file.

    Parameters:
    - input_dir: Directory containing the .txt files.
    - output_file: File to which the aggregated predictions will be written.
    """
    with open(output_file, 'w') as f:
        pass  # Open to clear or create the file

    # Iterate over each .txt file in the input directory using glob
    for txt_file_path in glob.glob(os.path.join(input_dir, '*.txt')):
        # Extract image_id from the file name, remove leading zeros
        image_id = str(int(os.path.basename(txt_file_path).split('.')[0]))

        # Open and read the current .txt file
        with open(txt_file_path, 'r') as file:
            for line in file:
                class_id, cx, cy, w, h, conf = line.strip().split()
                # Adjust class value and prepare the output line
                adjusted_class_id = str(int(class_id) + 1)
                output_line = f"{image_id} {adjusted_class_id} {cx} {cy} {w} {h} {conf}\n"

                # Append the output line to the output file
                with open(output_file, 'a') as out_file:
                    out_file.write(output_line)


# Replace input_dir with current iteration's directory
input_dir = 'runs/detect/train163/labels'
output_file = 'predictions.txt'
aggregate_predictions(input_dir, output_file)

print("Aggregation complete. Check the output file for the combined predictions.")