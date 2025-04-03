import os
import sys
from autoenv_tool.utils.env import read_env, create_env, create_env_file, create_utils_folder, create_env_py


def autoenv():
    """ Terminaldan `autoenv` deb yozilganda ishga tushadi """
    env_file = ".env"

    # .env faylini tekshirish va yaratish
    if not os.path.exists(env_file):
        ans = input(".env fayli mavjud emas. Yaratilsinmi? (y/n): ").strip().lower()
        if ans == "y":
            create_env(env_file)
        else:
            print("Amal bekor qilindi.")
            sys.exit(0)

    env_data = read_env(env_file)
    
    print("\n🔹 .env dagi o‘zgaruvchilar:")
    for key, value in env_data.items():
        print(f"{key} = {value}")

    confirm = input("\n♻️  Ushbu o‘zgaruvchilarni yuklashni istaysizmi? (y/n): ").strip().lower()
    if confirm == "y" or confirm == "": 
        for key, value in env_data.items():
            os.environ[key] = value
        print("✅ O‘zgaruvchilar yuklandi!")
    else:
        print("❌ Yuklash bekor qilindi.")


def create():
    """ `autoenv` paketini o'rnatish uchun yordamchi funksiya """
    # `.env` fayli yaratish, `utils` papkasini yaratish va `env.py` faylini yaratish
    create_env_file()
    create_utils_folder()
    create_env_py()
    print("Autoenv setup muvaffaqiyatli yakunlandi!")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "create":
        create()
    else:
        autoenv()
