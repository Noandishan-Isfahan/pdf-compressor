#!/bin/bash

# Directory containing the .ui files

DIRECTORY="ui/forms/qt"
# Function to convert .ui to .py and modify the output file
convert_ui_file() {
  ui_file="$1"
  
  OUT_DIRECTORY="ui/forms"
  if [[ -f "$ui_file" ]]; then
    # Get the base name of the file (without extension)
    base_name=$(basename "$ui_file" .ui)
    file_name="$OUT_DIRECTORY/$base_name.py"
    # Convert .ui to .py using pyside6-uic
    pyside6-uic "$ui_file" -o "$file_name"
    
    # Modify the generated Python file
    sed -i '1i from ui.custom.Widget import CustomLabel,CustomPushButton' "$file_name"
    sed -i '1i from pathlib import Path' "$file_name"
    sed -i '1i from setting import ROOT_DIR' "$file_name"
    sed -i -E 's#u"img/(.*\.(png|svg))"#str(Path(ROOT_DIR / "img") / "\1")#g' "$file_name"
    sed -i -E 's/= QPushButton/= CustomPushButton/g' "$file_name"
    sed -i -E 's/= QLabel/= CustomLabel/g' "$file_name"
    
    echo "Converted $ui_file to $file_name"
  else
    echo "No .ui files found in the directory."
  fi
}

export -f convert_ui_file

# Run the conversion in parallel using xargs
find "$DIRECTORY" -name "*.ui" | xargs -P 3 -I {} bash -c 'convert_ui_file "$@"' _ {}

