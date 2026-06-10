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

* 13 animated cursor files (`1.ani`,`2.ani`,...)
* Mahiro wallpaper (`background.bmp`)
* Custom sound effect (`MahiroSfx.wav`)

## Requirements

* Windows 10 / Windows 11
* Python 3.10+ (for source version)

## Running from Source

```bash
python Mahiro-ware.py
```

## Building

```bash
pyinstaller --onefile --noconsole --add-data "background.bmp;." --add-data "1.ani;." --add-data "2.ani;." --add-data "3.ani;." --add-data "4.ani;." --add-data "5.ani;." --add-data "6.ani;." --add-data "7.ani;." --add-data "8.ani;." --add-data "9.ani;." --add-data "10.ani;." --add-data "11.ani;." --add-data "12.ani;." --add-data "13.ani;." --add-data "MahiroSfx.wav;." Mahiro-ware.py
```

## Running from available releases

[Click here!](https://github.com/vnguyhuyeditz/Mahiro-ware/releases)

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

This project modifies Windows user settings, including cursors, wallpaper, and sound configuration. Changes affect only the current user profile and can be reverted manually through Windows Settings. Bugs might appear. Run it at your own risk!

## License

This project is provided for educational and personal use.
