import os
import shutil
import requests

# Define the path to the directory to be sorted
path = '/YOUR_PATH'

# Define the categories and their respective extensions
categories = {
    'Images': [
        'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'heic', 'psd', 
        'raw', 'cr2', 'nef', 'orf', 'sr2', 'ai', 'eps', 'ico', 'tga', 'dds'
    ],
    'Videos': [
        'mp4', 'mkv', 'flv', 'avi', 'mov', 'wmv', 'mpeg', 'mpg', 'm4v', '3gp', 
        'webm', 'vob', 'ogv', 'mxf', 'rm', 'rmvb', 'asf', 'mts', 'm2ts', 'ts'
    ],
    'Installation_Packages': [
        'exe', 'msi', 'dmg', 'pkg', 'deb', 'rpm', 'sh', 'run', 'appimage', 
        'tar.gz', 'tar.bz2', 'tar.xz'
    ],
    'Software': [
        'app', 'bat', 'bin', 'sh', 'dll', 'sys', 'drv', 'jar', 'apk', 'ipa', 
        'command', 'ksh', 'csh', 'fish', 'zsh', 'cmd'
    ],
    'Coding': [
        'py', 'java', 'cpp', 'c', 'js', 'html', 'css', 'php', 'rb', 'go', 'rs', 
        'swift', 'kt', 'ts', 'jsx', 'tsx', 'json', 'xml', 'yaml', 'yml', 'ini', 
        'config', 'sh', 'bat', 'pl', 'pm', 'tcl', 'vbs', 'lua', 'r', 'sas', 
        'sql', 'adb', 'ads', 'asm', 's', 'bas', 'cls', 'frm', 'vb', 'cs', 'h', 
        'hpp', 'hs', 'lhs', 'erl', 'hrl', 'fs', 'fsi', 'ml', 'mli', 'fsx', 'fsscript', 
        'lhs', 'clj', 'cljs', 'cljc', 'edn', 'coffee', 'litcoffee', 'dart', 'd', 
        'pas', 'pp', 'p', 'm', 'mm', 'scm', 'sld', 'rkt', 'ss', 'sls', 'el', 
        'lisp', 'lsp', 'jl', 'nim', 'nims', 'nimble', 'cr', 'ecr', 'ex', 'exs'
    ],
    'Documents': [
        'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'md', 'rtf', 
        'odt', 'ods', 'odp', 'epub', 'mobi', 'csv', 'tsv', 'log', 'tex', 'bib', 
        'rtfd', 'wps', 'wpd', 'key', 'numbers', 'pages', 'sdc', 'sdd', 'sdp'
    ],
    'Archives': [
        'zip', 'rar', 'tar', 'gz', '7z', 'bz2', 'xz', 'iso', 'tgz', 'tbz2', 'cab', 
        'lha', 'arj', 'ace', 'uue', 'z', 'war', 'ear', 'hqx', 'sit', 'sea', 
        'taz', 'lzh', 'zipx'
    ],
    'Games': [
        'exe', 'lnk', 'url', 'iso', 'bin', 'nrg', 'cue', 'ccd', 'mdf', 'mds', 
        'gcm', 'rom', 'sav', 'nes', 'smc', 'sfc', 'gba', 'nds', 'ps1', 'ps2', 
        'psp', 'xbox', 'xiso', 'xex', 'pak', 'wad', 'vpk', 'apk', 'ipa'
    ]
}

# Function to fetch the OAuth token
def get_oauth_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print("Failed to obtain OAuth token:", response.status_code, response.text)
        return None

# Function to fetch game titles from IGDB
def fetch_game_titles(client_id, oauth_token):
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {oauth_token}",
    }
    body = "fields name; limit 500;"  # Adjust the query as needed
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        games = response.json()
        return [game['name'].lower() for game in games]
    else:
        print("Error fetching game titles:", response.status_code, response.text)
        return []

# Function to get the category of a file based on its extension and name
def get_category(filename, ext, game_titles):
    if ext == 'exe':
        for game in game_titles:
            if game in filename.lower():
                return 'Games'
        return 'Installation_Packages'
    else:
        for category, extensions in categories.items():
            if ext in extensions:
                return category
    return None

# Function to move files and directories, checking for existing filenames
def move_item(item_path, target_dir, item_name):
    target_path = os.path.join(target_dir, item_name)
    # If the target path exists and is a directory, move the file into it
    if os.path.exists(target_path):
        if os.path.isdir(target_path):
            shutil.move(item_path, os.path.join(target_path, os.path.basename(item_path)))
        else:
            # Handle the case where the existing item is a file and not a directory
            print(f"Error: {target_path} exists and is not a directory.")
    else:
        shutil.move(item_path, target_path)

# Function to categorize and move files and directories
def categorize_and_move(item_path, base_path, game_titles):
    if os.path.isfile(item_path):
        name, ext = os.path.splitext(item_path)
        ext = ext[1:].lower()  # Get the extension and convert to lower case
        category = get_category(name, ext, game_titles)
        if category:
            category_path = os.path.join(base_path, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            move_item(item_path, category_path, os.path.basename(item_path))
    elif os.path.isdir(item_path):
        folder_name = os.path.basename(item_path)
        # Check if the directory should be moved based on its name
        for category in ['Images', 'Videos']:
            if category.lower() in folder_name.lower():
                category_path = os.path.join(base_path, category)
                if os.path.abspath(item_path) != os.path.abspath(category_path):
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    move_item(item_path, category_path, folder_name)
                else:
                    print(f"Cannot move directory '{folder_name}' into itself.")
                return  # Exit after moving the folder

        # If the folder does not match 'Images' or 'Videos', leave it as is
        print(f"Directory '{folder_name}' not moved (only 'Images' and 'Videos' folders are moved).")

# Your IGDB credentials
client_id = "YOUR_CLIENT_ID"  # Replace with your IGDB Client ID
client_secret = "YOUR_CLIENT_SECRET"  # Replace with your IGDB Client Secret

# Obtain OAuth token
oauth_token = get_oauth_token(client_id, client_secret)
if not oauth_token:
    exit("Failed to obtain OAuth token")

# Fetch game titles
game_titles = fetch_game_titles(client_id, oauth_token)

# List all files and directories in the path
list_ = os.listdir(path)

# Go through each item in the directory
for item in list_:
    item_path = os.path.join(path, item)
    categorize_and_move(item_path, path, game_titles)

print("Files and folders have been sorted into respective categories.")
