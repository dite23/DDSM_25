import os
import re  

def extract_number(file_name):
    return [int(num) for num in re.findall(r'\d+', file_name)]

def generate_index(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Diseño y Desarrollo de un Sistema Mecánico (DDSM_25)\n")
        file.write("="*38 + "\n\n")
        file.write("Aquí se recogerá toda la documentación sobre la asignatura "Diseño y Desarrollo de un Sistema Mecánico" del curso 2024/25.\n\n")
        
        for root, dirs, files in os.walk(root_dir):
            # Only consider immediate subdirectories of the root directory
            if root == root_dir:
                dirs.sort()  # Ensure directories are sorted
                for dir_name in dirs:
                    # Skip directories that start with an underscore
                    if dir_name.startswith('_'):
                        continue
                    # Extract caption by removing leading number and underscore
                    caption = dir_name.split('_', 1)[-1]
                    # Create a toctree for each subdirectory
                    file.write(f".. toctree::\n")
                    file.write(f"   :maxdepth: 2\n")
                    file.write(f"   :caption: {caption}:\n\n")
                    
                    # Add each markdown file in the subdirectory to the toctree
                    sub_dir = os.path.join(root_dir, dir_name)
                    for sub_root, sub_dirs, sub_files in os.walk(sub_dir):
                        #sub_files.sort()  # Ensure directories are sorted
                        sub_files.sort(key=extract_number)
                        for sub_file in sub_files:
                            if sub_file.endswith('.md') or sub_file.endswith('.rst'):
                                file.write(f"   {dir_name}/{sub_file}\n")
                                if sub_file.endswith('.md'):
                                    # Process each markdown file to replace data-align="center">
                                    process_markdown_file(os.path.join(sub_root, sub_file))
                        # We only want to process the top level of each subdirectory
                        break
                    file.write("\n")

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Verificar si el archivo ya contiene las etiquetas de justificación
        has_justify_start = any('<div style="text-align: justify;">' in line for line in lines)
        has_justify_end = any('</div>' in line for line in lines)

        with open(file_path, 'w', encoding='utf-8') as file:
            if not has_justify_start:
                file.write('<div style="text-align: justify;">\n\n')
            
            for line in lines:
                if 'data-align="center"' in line and ' align="center"' not in line:
                    line = line.replace('data-align="center"', 'data-align="center" align="center"')
                file.write(line)
            
            if not has_justify_end:
                file.write('\n</div>\n')

if __name__ == "__main__":
    root_directory = "."  # Change this to your root directory
    output_file_name = "index.rst"
    generate_index(root_directory, output_file_name)
