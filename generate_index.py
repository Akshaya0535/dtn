#!/usr/bin/env python3
import os
import datetime

def generate_index_html():
    """Generate an HTML index file for the current directory."""
    # Get the current directory path and name
    current_dir = os.getcwd()
    dir_name = os.path.basename(current_dir)
    
    # Get a list of all files in the current directory
    files = os.listdir(current_dir)
    
    # Sort files alphabetically (case-insensitive)
    files.sort(key=str.lower)
    
    # Files to exclude from the listing
    exclude_files = ['index.html', 'generate_index.py']
    files = [f for f in files if f not in exclude_files]
    
    # HTML content
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing: {dir_name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            border-bottom: 2px solid #ddd;
            padding-bottom: 10px;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin: 10px 0;
            padding: 10px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            transition: background-color 0.2s;
        }}
        li:hover {{
            background-color: #f0f0f0;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
            display: block;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .file-info {{
            color: #666;
            font-size: 0.8em;
            margin-top: 4px;
        }}
        .footer {{
            margin-top: 30px;
            font-size: 0.8em;
            color: #666;
            text-align: center;
        }}
    </style>
</head>
<body>
    <h1>Directory Listing: {dir_name}</h1>
    <ul>
'''
    
    # Add parent directory link
    html_content += f'''        <li>
            <a href="../">../</a>
            <div class="file-info">Parent Directory</div>
        </li>
'''
    
    # Add each file to the HTML
    for file in files:
        # Skip hidden files
        if file.startswith('.'):
            continue
            
        file_path = os.path.join(current_dir, file)
        
        # Get file info
        is_dir = os.path.isdir(file_path)
        try:
            size = os.path.getsize(file_path)
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            modified_str = modified_time.strftime("%Y-%m-%d %H:%M:%S")
        except (FileNotFoundError, PermissionError):
            size = 0
            modified_str = "Unknown"
        
        # Format file size
        if is_dir:
            size_str = "Directory"
        elif size < 1024:
            size_str = f"{size} bytes"
        elif size < 1024 * 1024:
            size_str = f"{size/1024:.1f} KB"
        else:
            size_str = f"{size/(1024*1024):.1f} MB"
        
        # Add directory indicator
        display_name = file
        if is_dir:
            display_name += "/"
            
        html_content += f'''        <li>
            <a href="{file}">{display_name}</a>
            <div class="file-info">{size_str} - Last modified: {modified_str}</div>
        </li>
'''
    
    # Close the HTML tags
    html_content += f'''    </ul>
    <div class="footer">
        Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    </div>
</body>
</html>
'''
    
    # Write the HTML content to index.html
    with open('index.html', 'w') as f:
        f.write(html_content)
    
    print(f"Index file 'index.html' has been generated in {current_dir}")

if __name__ == "__main__":
    generate_index_html()
