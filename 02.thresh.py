import cv2, os, shutil, argparse

# 基本的なモデルパラメータ
FLAGS = None

def convert_image(sub_path):
    os.mkdir(FLAGS.output_path + sub_path)

    # フォルダ内ファイルを変数に格納(ディレクトリも格納)
    files =  os.listdir(FLAGS.input_path + sub_path)

    for file_name in files:
        # 画像ファイル読込
        img = cv2.imread(FLAGS.input_path + sub_path + file_name)

        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        ret, img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

        cv2.imwrite(FLAGS.output_path + sub_path + file_name, img_thresh)

    print("Folder %s Number of conversion： %d" % ( sub_path, len(files)))

# 直接実行されている場合に通る(importされて実行時は通らない)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_path",
        type=str,
        default="./images/input/",
        help="The path of input directory."
  )
    parser.add_argument(
        "--output_path",
        type=str,
        default="./images/output/02thresh_otsu/",
        help="The path of output directory."
  )

# パラメータ取得と実行
FLAGS, unparsed = parser.parse_known_args() 

# 出力用のディレクトリが存在する場合、削除して再作成
if os.path.exists(FLAGS.output_path):
    shutil.rmtree(FLAGS.output_path)
os.mkdir(FLAGS.output_path)

convert_image("CD/")
convert_image("UD/")




