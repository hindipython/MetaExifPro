import random
import datetime

def get_iphone_14_pro():
    """Returns metadata mimicing an Apple iPhone 14 Pro."""
    timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    return {
        "0th:Make": "Apple",
        "0th:Model": "iPhone 14 Pro",
        "0th:Software": "16.5",
        "0th:DateTime": timestamp,
        "Exif:DateTimeOriginal": timestamp,
        "Exif:DateTimeDigitized": timestamp,
        "Exif:ExifVersion": "0232",
        "Exif:ShutterSpeedValue": "1/60",
        "Exif:ApertureValue": "1.78",
        "Exif:BrightnessValue": "5.45",
        "Exif:ExposureBiasValue": "0",
        "Exif:MeteringMode": "5", # Pattern
        "Exif:Flash": "16", # Off, did not fire
        "Exif:FocalLength": "6.86",
        "Exif:ColorSpace": "65535", # Uncalibrated
        "Exif:SensingMethod": "2", # One-chip color area
        "Exif:SceneType": "1", # Directly photographed
        "Exif:ExposureMode": "0", # Auto
        "Exif:WhiteBalance": "0", # Auto
        "Exif:FocalLengthIn35mmFilm": "24",
        "Exif:LensSpecification": "2.22 9 1.78 2.8",
        "Exif:LensMake": "Apple",
        "Exif:LensModel": "iPhone 14 Pro back triple camera 6.86mm f/1.78",
    }

def get_samsung_s23_ultra():
    """Returns metadata mimicing a Samsung Galaxy S23 Ultra."""
    timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    return {
        "0th:Make": "Samsung",
        "0th:Model": "SM-S918B",
        "0th:Software": "S918BXXU1AWC8",
        "0th:DateTime": timestamp,
        "Exif:DateTimeOriginal": timestamp,
        "Exif:DateTimeDigitized": timestamp,
        "Exif:ExifVersion": "0220",
        "Exif:ExposureProgram": "2", # Normal program
        "Exif:ISOSpeedRatings": str(random.choice([50, 100, 200, 400])),
        "Exif:ShutterSpeedValue": "1/100",
        "Exif:ApertureValue": "1.7",
        "Exif:BrightnessValue": "2.33",
        "Exif:ExposureBiasValue": "0",
        "Exif:MaxApertureValue": "1.16",
        "Exif:MeteringMode": "2", # CenterWeightedAverage
        "Exif:Flash": "0", 
        "Exif:FocalLength": "6.30",
        "Exif:ColorSpace": "1", # sRGB
        "Exif:WhiteBalance": "0", 
        "Exif:FocalLengthIn35mmFilm": "23",
    }

def get_canon_eos_r5():
    """Returns metadata mimicing a Canon EOS R5."""
    timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    return {
        "0th:Make": "Canon",
        "0th:Model": "Canon EOS R5",
        "0th:Artist": "Photographer",
        "0th:DateTime": timestamp,
        "Exif:DateTimeOriginal": timestamp,
        "Exif:DateTimeDigitized": timestamp,
        "Exif:SensitivityType": "2",
        "Exif:RecommendedExposureIndex": "100",
        "Exif:ExifVersion": "0231",
        "Exif:ShutterSpeedValue": "1/200",
        "Exif:ApertureValue": "4.0",
        "Exif:ExposureBiasValue": "0",
        "Exif:MaxApertureValue": "4.0",
        "Exif:MeteringMode": "5",
        "Exif:Flash": "16",
        "Exif:FocalLength": "50.0",
        "Exif:SubSecTime": "00",
        "Exif:SubSecTimeOriginal": "00",
        "Exif:SubSecTimeDigitized": "00",
        "Exif:ColorSpace": "1",
        "Exif:CustomRendered": "0",
        "Exif:ExposureMode": "1", # Manual
        "Exif:WhiteBalance": "0",
        "Exif:SceneCaptureType": "0",
        "Exif:OwnerName": "Unknown",
        "Exif:SerialNumber": "1234567890",
        "Exif:LensSpecification": "24 105 4 4",
        "Exif:LensModel": "RF24-105mm F4 L IS USM",
        "Exif:LensSerialNumber": "0000000000",
    }

def get_huawei_p60_pro():
    """Returns metadata mimicing a Huawei P60 Pro."""
    timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    return {
        "0th:Make": "HUAWEI",
        "0th:Model": "MNA-AL00",
        "0th:Software": "HarmonyOS 4.0.0",
        "0th:DateTime": timestamp,
        "Exif:DateTimeOriginal": timestamp,
        "Exif:DateTimeDigitized": timestamp,
        "Exif:ExifVersion": "0221",
        "Exif:ExposureProgram": "2",
        "Exif:ISOSpeedRatings": str(random.choice([50, 64, 100, 200])),
        "Exif:ShutterSpeedValue": "1/50",
        "Exif:ApertureValue": "1.4",
        "Exif:BrightnessValue": "0",
        "Exif:ExposureBiasValue": "0",
        "Exif:MeteringMode": "5",
        "Exif:Flash": "0",
        "Exif:FocalLength": "24.5",
        "Exif:ColorSpace": "1",
        "Exif:WhiteBalance": "0",
        "Exif:FocalLengthIn35mmFilm": "25",
        "Exif:LensMake": "HUAWEI",
        "Exif:LensModel": "HUAWEI P60 Pro Rear Main Camera",
    }

def get_xiaomi_13_ultra():
    """Returns metadata mimicing a Xiaomi 13 Ultra."""
    timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    return {
        "0th:Make": "Xiaomi",
        "0th:Model": "2304FPN6DC",
        "0th:Software": "MIUI 14", # or HyperOS depending on version
        "0th:DateTime": timestamp,
        "Exif:DateTimeOriginal": timestamp,
        "Exif:DateTimeDigitized": timestamp,
        "Exif:ExifVersion": "0232",
        "Exif:ExposureProgram": "2",
        "Exif:ISOSpeedRatings": str(random.choice([50, 100, 160])),
        "Exif:ShutterSpeedValue": "1/100",
        "Exif:ApertureValue": "1.9",
        "Exif:ExposureBiasValue": "0",
        "Exif:MaxApertureValue": "1.4",
        "Exif:MeteringMode": "2",
        "Exif:Flash": "16",
        "Exif:FocalLength": "8.7",
        "Exif:ColorSpace": "1",
        "Exif:WhiteBalance": "0",
        "Exif:FocalLengthIn35mmFilm": "23",
        "Exif:LensMake": "Leica",
        "Exif:LensModel": "Leica Vario-Summicron 1:1.8-3.0/12-120 ASPH.",
    }

def get_windows_11_pc():
    """Returns metadata mimicing a Windows 11 PC export."""
    timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    return {
        "0th:Make": "Microsoft",
        "0th:Software": "Windows 11 Pro 22H2",
        "0th:Artist": "User", 
        "0th:DateTime": timestamp,
        "Info:Software": "Paint 3D",
        "Info:System": "Windows 11",
        "comment": "Created on Windows 11",
    }

def get_macos_sonoma():
    """Returns metadata mimicing a macOS Sonoma export."""
    timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    return {
        "0th:Make": "Apple",
        "0th:Software": "macOS 14.0 (23A344)",
        "0th:Artist": "Mac User",
        "0th:DateTime": timestamp,
        "Info:Software": "Mac OS X 10.16 (23A344)",
        "Exif:UserComment": "Screenshot",
        "0th:Model": "MacBook Pro",
    }

def get_ubuntu_linux():
    """Returns metadata mimicing an Ubuntu Linux export."""
    timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    return {
        "0th:Software": "GNOME Screenshot 42.0",
        "0th:DateTime": timestamp,
        "Info:Software": "ImageMagick 6.9.11-60",
        "Info:System": "Ubuntu 22.04 LTS",
        "0th:Artist": "ubuntu",
        "comment": "Screenshot from 2024-01-01",
    }

PRESETS = {
    "iPhone 14 Pro": get_iphone_14_pro,
    "Samsung S23 Ultra": get_samsung_s23_ultra,
    "Huawei P60 Pro": get_huawei_p60_pro,
    "Xiaomi 13 Ultra": get_xiaomi_13_ultra,
    "Canon EOS R5": get_canon_eos_r5,
    "PC - Windows 11": get_windows_11_pc,
    "PC - macOS Sonoma": get_macos_sonoma,
    "PC - Ubuntu 22.04": get_ubuntu_linux
}

def generate_filename(preset: str, original_ext: str) -> str:
    """Generates a realistic filename based on the device preset."""
    now = datetime.datetime.now()
    
    if preset == "iPhone 14 Pro" or preset == "Canon EOS R5":
        # IMG_1234.JPG
        num = random.randint(1000, 9999)
        return f"IMG_{num}{original_ext.upper()}"
    
    elif preset == "Samsung S23 Ultra":
        # 20230521_142201.jpg
        return f"{now.strftime('%Y%m%d_%H%M%S')}{original_ext.lower()}"
    
    elif preset == "Huawei P60 Pro" or preset == "Xiaomi 13 Ultra":
         # IMG_20230521_142201.jpg
        return f"IMG_{now.strftime('%Y%m%d_%H%M%S')}{original_ext.lower()}"
    
    elif preset == "PC - Windows 11":
        # Screenshot 2023-05-21 142201.png
        return f"Screenshot {now.strftime('%Y-%m-%d %H%M%S')}{original_ext.lower()}"
    
    elif preset == "PC - macOS Sonoma":
        # Screenshot 2023-05-21 at 14.22.01.png
        return f"Screenshot {now.strftime('%Y-%m-%d at %H.%M.%S')}{original_ext.lower()}"

    elif preset == "PC - Ubuntu 22.04":
        # Screenshot from 2023-05-21 14-22-01.png
        return f"Screenshot from {now.strftime('%Y-%m-%d %H-%M-%S')}{original_ext.lower()}"
        
    return f"renamed_{original_ext}"
