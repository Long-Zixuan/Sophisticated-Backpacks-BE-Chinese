import zipfile
import os

# 压缩指定文件夹
def zipdir(path, ziph):
    # 循环遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(path):
        for file in files:
            # 将每个文件添加到zip文件中
            ziph.write(os.path.join(root, file))

# 将指定文件夹保存为zip文件
def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'a') as zipObj:
        # 添加文件夹及其内容到zip文件中
        zipdir(folder_path, zipObj)

def write_lang_file(path,txt):
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
	   
VERSION = "0.5.2"
CHINESE_VERSION = "3.0"
MOD_NAME = "精妙背包"
FINAL_NAME = MOD_NAME + " v"+VERSION+"."+CHINESE_VERSION+".mcaddon"

CHINESE_R_LANG = 'pack.name=§7[v%s]§r %s-资源包\npack.description=@Angeldfire2 - backpacks    || by 承挨汉化  LoongLy修复  汉化版本：V%s'
CHINESE_B_LANG = 'pack.name=§7[v%s]§r %s-行为包\npack.description=@Angeldfire2 - backpacks    || by 承挨汉化  LoongLy修复  汉化版本：V%s'
CHINESE_R_LANG_PATH = "./RE/texts/zh_CN.lang"
CHINESE_B_LANG_PATH = "./BE/texts/zh_CN.lang"

if __name__ == "__main__":
    chinese_b_lang = CHINESE_B_LANG % (VERSION, MOD_NAME, CHINESE_VERSION)
    chinese_r_lang = CHINESE_R_LANG % (VERSION, MOD_NAME, CHINESE_VERSION)
    write_lang_file(CHINESE_B_LANG_PATH, chinese_b_lang)
    write_lang_file(CHINESE_R_LANG_PATH, chinese_r_lang)

    zip_folder("./BE", FINAL_NAME)
    zip_folder("./RE", FINAL_NAME)

# LZX-2025-11-27-001
