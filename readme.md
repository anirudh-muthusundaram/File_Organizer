# File Organizer Script

This Python script is designed to organize files in a specified directory into categorized folders based on their file types. It uses the IGDB API to categorize game-related files accurately and supports a wide range of file extensions to ensure thorough organization. The main usage of this organizer is to organize your game files seperate from your installation files using Twitch API. So, Please create and obtain your Client ID and Client Secret from Twitch Developers Website: https://dev.twitch.tv 

## Features

- Categorizes files into folders such as Images, Videos, Installation Packages, Software, Coding, Documents, Archives, and Games.
- Moves directories that contain images or videos into their respective folders.
- Ensures directories are not moved into themselves, avoiding errors.
- Utilizes the IGDB API to fetch game titles for accurate categorization of game-related files.

## Categories and File Types

The script categorizes files into the following folders based on their extensions:

- **Images**: jpg, jpeg, png, gif, bmp, tiff, svg, webp, heic, psd, raw, cr2, nef, orf, sr2, ai, eps, ico, tga, dds
- **Videos**: mp4, mkv, flv, avi, mov, wmv, mpeg, mpg, m4v, 3gp, webm, vob, ogv, mxf, rm, rmvb, asf, mts, m2ts, ts
- **Installation Packages**: exe, msi, dmg, pkg, deb, rpm, sh, run, appimage, tar.gz, tar.bz2, tar.xz
- **Software**: app, bat, bin, sh, dll, sys, drv, jar, apk, ipa, command, ksh, csh, fish, zsh, cmd
- **Coding**: py, java, cpp, c, js, html, css, php, rb, go, rs, swift, kt, ts, jsx, tsx, json, xml, yaml, yml, ini, config, sh, bat, pl, pm, tcl, vbs, lua, r, sas, sql, adb, ads, asm, s, bas, cls, frm, vb, cs, h, hpp, hs, lhs, erl, hrl, fs, fsi, ml, mli, fsx, fsscript, lhs, clj, cljs, cljc, edn, coffee, litcoffee, dart, d, pas, pp, p, m, mm, scm, sld, rkt, ss, sls, el, lisp, lsp, jl, nim, nims, nimble, cr, ecr, ex, exs
- **Documents**: pdf, doc, docx, xls, xlsx, ppt, pptx, txt, md, rtf, odt, ods, odp, epub, mobi, csv, tsv, log, tex, bib, rtfd, wps, wpd, key, numbers, pages, sdc, sdd, sdp
- **Archives**: zip, rar, tar, gz, 7z, bz2, xz, iso, tgz, tbz2, cab, lha, arj, ace, uue, z, war, ear, hqx, sit, sea, taz, lzh, zipx
- **Games**: exe, lnk, url, iso, bin, nrg, cue, ccd, mdf, mds, gcm, rom, sav, nes, smc, sfc, gba, nds, ps1, ps2, psp, xbox, xiso, xex, pak, wad, vpk, apk, ipa

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/anirudh-muthusundaram/File_Organizer.git
    cd file-organizer
    ```

2. **Install the required dependencies:**

    Ensure you have `requests` library installed. You can install it using pip:

    ```sh
    pip install requests
    ```

3. **Set up IGDB API credentials:**

    - Go to [IGDB](https://www.igdb.com/) and sign up for an account.
    - Obtain your Client ID and Client Secret from the Twitch Developer Portal.

4. **Configure the script:**

    Replace the placeholders in the script with your actual IGDB Client ID and Client Secret:

    ```python
    client_id = "YOUR_CLIENT_ID"  # Replace with your IGDB Client ID
    client_secret = "YOUR_CLIENT_SECRET"  # Replace with your IGDB Client Secret
    ```

## Usage

1. **Navigate to the directory containing the script:**

    ```sh
    cd /path/to/script
    ```

2. **Run the script:**

    ```sh
    python3 main.py
    ```

    This will organize all files in the specified path (`/Users/anirudhm/Downloads` by default) into their respective categories.

## Acknowledgements

- [IGDB](https://www.igdb.com/) for providing the game titles database.
- [Python](https://www.python.org/) for being a versatile programming language.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the Creative Commons Zero v1.0 Universal (CC0 1.0) License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [IGDB](https://www.igdb.com/) for providing the game titles database.
- [Python](https://www.python.org/) for being a versatile programming language.

## Contact

For any questions or inquiries, please contact [Anirudh Muthusundaram](mailto:anirudhms247@gmail.com).

---

**Note**: This script is a tool to help organize your files and directories. Please review the categorization logic and adjust the file paths and categories as needed for your specific use case.
