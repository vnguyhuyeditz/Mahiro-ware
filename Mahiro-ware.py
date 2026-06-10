import os
import sys
import ctypes
import winreg
from datetime import datetime

errors = []


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


if getattr(sys, "frozen", False):
    LOG_FILE = os.path.join(
        os.path.dirname(sys.executable),
        "logs.txt"
    )
else:
    LOG_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "logs.txt"
    )


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"

    print(line)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


CURSORS = {
    "Arrow": "7.ani",
    "Help": "4.ani",

    "AppStarting": "2.ani",
    "Wait": "5.ani",

    "Crosshair": "12.ani",
    "IBeam": "6.ani",
    "No": "1.ani",

    "SizeNS": "3.ani",
    "SizeWE": "8.ani",

    "SizeNWSE": "9.ani",
    "SizeNESW": "10.ani",

    "SizeAll": "11.ani",
    "Hand": "13.ani",
}


log("=" * 60)
log("Mahiro-ware started")
log(f"Working directory: {os.getcwd()}")
log(f"Log file: {LOG_FILE}")


# ==================================================
# CURSORS
# ==================================================

try:
    log("Applying cursor pack...")

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Control Panel\Cursors",
        0,
        winreg.KEY_SET_VALUE
    )

    for cursor_type, filename in CURSORS.items():
        full_path = resource_path(filename)

        if os.path.exists(full_path):

            winreg.SetValueEx(
                key,
                cursor_type,
                0,
                winreg.REG_EXPAND_SZ,
                full_path
            )

            log(f"[OK] {cursor_type} -> {filename}")

        else:
            err = f"Missing cursor file: {filename}"
            log(f"[ERROR] {err}")
            errors.append(err)

    winreg.CloseKey(key)

    SPI_SETCURSORS = 0x0057

    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETCURSORS,
        0,
        None,
        0
    )

    log("Cursor pack applied successfully")

except Exception as e:
    err = f"Cursor Error: {type(e).__name__}: {e}"
    log(f"[ERROR] {err}")
    errors.append(err)


# ==================================================
# WALLPAPER
# ==================================================

try:
    log("Changing wallpaper...")

    wallpaper = resource_path("background.bmp")

    if not os.path.exists(wallpaper):
        raise FileNotFoundError("background.bmp not found")

    result = ctypes.windll.user32.SystemParametersInfoW(
        20,
        0,
        wallpaper,
        3
    )

    if result:
        log("Wallpaper changed successfully")
    else:
        raise RuntimeError(
            "Windows rejected wallpaper change"
        )

except Exception as e:
    err = f"Wallpaper Error: {type(e).__name__}: {e}"
    log(f"[ERROR] {err}")
    errors.append(err)


# ==================================================
# SOUNDS
# ==================================================

try:
    log("Applying sound scheme...")

    wav_path = resource_path("MahiroSfx.wav")

    if not os.path.exists(wav_path):
        raise FileNotFoundError(
            "MahiroSfx.wav not found"
        )

    root = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"AppEvents\Schemes\Apps\.Default",
        0,
        winreg.KEY_READ
    )

    changed = 0
    index = 0

    while True:

        try:
            event_name = winreg.EnumKey(root, index)
            index += 1

        except OSError:
            break

        if event_name == ".Default":
            continue

        try:
            current_key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                fr"AppEvents\Schemes\Apps\.Default\{event_name}\.Current",
                0,
                winreg.KEY_SET_VALUE
            )

            winreg.SetValueEx(
                current_key,
                "",
                0,
                winreg.REG_SZ,
                wav_path
            )

            winreg.CloseKey(current_key)

            changed += 1
            log(f"[OK] Sound changed: {event_name}")

        except OSError:
            pass

    winreg.CloseKey(root)

    log(f"Changed {changed} sound events")

except Exception as e:
    err = f"Sound Error: {type(e).__name__}: {e}"
    log(f"[ERROR] {err}")
    errors.append(err)


# ==================================================
# FINISH
# ==================================================

log("Installation finished")

if errors:

    msg = (
        "Some operations failed.\n\n"
        + "\n".join(errors[:10])
        + "\n\nCheck logs.txt for details."
    )

    ctypes.windll.user32.MessageBoxW(
        0,
        msg,
        "Mahiro-ware - Error",
        0x10
    )

else:

    ctypes.windll.user32.MessageBoxW(
        0,
        "Theme installed successfully!",
        "Mahiro-ware",
        0x40
    )

log("Mahiro-ware finished")
log("=" * 60)