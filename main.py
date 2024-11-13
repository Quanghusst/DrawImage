import os
import sys

from PIL import Image

def clear_screen():
    """Clear the screen depending on the operating system"""
    os.system('cls' if os.name == 'nt' else 'clear')

def layTenFile():
    # Yêu cầu người dùng nhập đường dẫn và kiểm tra tính hợp lệ
    while True:
        directory = input("Enter directory path (or press Enter to use the current directory): ").strip()
        if not directory:
            directory = "."  # Mặc định là thư mục hiện tại nếu không nhập gì
        if os.path.isdir(directory):
            break
        else:
            print("Directory path invalue. Try again")

    # Lấy danh sách file .jpg
    filenames = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".jpg")]
    if not filenames:
        print("No file .jpg in this folder")
        return None

    clear_screen()
    print("Choose a file you want to use: ")
    for i, filename in enumerate(filenames):
        print(f"{i + 1}. {os.path.basename(filename)}")
    print("0. EXIT")

    # Get user's file selection
    while True:
        your_choice = input("Enter your choice: ").strip()
        if your_choice == "0":
            clear_screen()
            sys.exit()
        elif your_choice not in map(str, range(1, len(filenames) + 1)):
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")
            continue
        else:
            clear_screen()
            chosen_file = filenames[int(your_choice) - 1]
            print("You are using the file:", os.path.basename(chosen_file))
            return chosen_file

def main():
    while(True):
        clear_screen()
        chosen_file = layTenFile()
        
        if chosen_file is not None:
            try:
                # Mở ảnh
                image = Image.open(chosen_file)
        
                
                # Chuyển ảnh thành ASCII
                img = image.resize((100, 50))  # Resize ảnh
                img = img.convert("L")  # Chuyển ảnh sang thang độ xám

                # Chuyển từng pixel thành ký tự ASCII
                chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
                ascii_str = ""
                for pixel in img.getdata():
                    ascii_str += chars[pixel // 25]  # Đổi pixel thành ký tự ASCII

                # Chia thành hàng và in ra màn hình
                ascii_str = "\n".join([ascii_str[i:i + 100] for i in range(0, len(ascii_str), 100)])
                print(ascii_str)

            except Exception as e:
                print("ERROR", e)
        else:
            print("Author: ledangquangdangquang.")
        input("Press Enter to continue...")

# Thực thi hàm main nếu đây là chương trình chính
if __name__ == "__main__":
    main()
