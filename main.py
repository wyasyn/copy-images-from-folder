import shutil
from pathlib import Path

# Path to the main folder
main_folder = Path("./acne2")
# Create an output folder beside the main folder
output_folder = main_folder.parent / f"{main_folder.name}_collected"
output_folder.mkdir(exist_ok=True)

# Supported image extensions
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

# Global counter to ensure unique names across all images
global_count = 1

# Recursively find all image files in subfolders
for file in main_folder.rglob("*"):
    if file.is_file() and file.suffix.lower() in image_extensions:
        # Determine the top‐level subfolder name for naming
        rel_path = file.relative_to(main_folder)
        top_folder = rel_path.parts[0]

        # Build a new filename and ensure no overwrite
        new_name = f"{top_folder}_{global_count}{file.suffix.lower()}"
        dest = output_folder / new_name
        while dest.exists():
            global_count += 1
            new_name = f"{top_folder}_{global_count}{file.suffix.lower()}"
            dest = output_folder / new_name

        # Copy the image
        shutil.copy(file, dest)
        global_count += 1

print(f"✅ {global_count - 1} images collected into: {output_folder.resolve()}")
