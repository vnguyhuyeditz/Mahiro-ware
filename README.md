# Mahiro-ware

Mahiro-ware is a lightweight Windows customization tool that transforms your desktop into a Mahiro-themed experience.

## Features

* Custom animated cursor pack
* Mahiro wallpaper installer
* Custom Windows sound scheme
* Automatic resource handling for PyInstaller builds
* Detailed logging system
* Error reporting with popup dialogs
* One-click installation

## Included Resources

* 13 animated cursor files (`.ani`)
* Mahiro wallpaper (`background.bmp`)
* Custom sound effect (`Windows Background.wav`)

## Requirements

* Windows 10 / Windows 11
* Python 3.10+ (for source version)

## Running the Application

### Option 1: Run from Source

```bash
python Mahiro-ware.py
```

### Option 2: Run the Built Executable

After building with PyInstaller, launch:

```text
dist/Mahiro-ware.exe
```

No Python installation is required when using the executable version.

All required resources are bundled into the executable, allowing the application to run as a standalone Windows program.

## Portable Usage

The built executable can be distributed and run directly on compatible Windows systems without installing Python or additional dependencies.

## Building

```bash
pyinstaller --onefile --noconsole ^
--icon=mahiro.ico ^
--add-data "background.bmp;." ^
--add-data "*.ani;." ^
--add-data "*.wav;." ^
Mahiro-ware.py
```

## Output

After running, Mahiro-ware will:

1. Apply the Mahiro cursor pack
2. Set the desktop wallpaper
3. Configure Windows sound events
4. Create a `logs.txt` file containing installation details
5. Display a completion or error dialog

## Logs

All operations are recorded in:

```text
logs.txt
```

If an installation step fails, check the log file for detailed information.

## Disclaimer

This project modifies Windows user settings, including cursors, wallpaper, and sound configuration. Changes affect only the current user profile and can be reverted manually through Windows Settings.

## License

This project is provided for educational and personal use.
