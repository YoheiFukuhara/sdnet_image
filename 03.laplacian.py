import cv2, os, shutil, argparse
import numpy as np

# 基本的なモデルパラメータ
FLAGS = None

# カーネル(ラプラシアンフィルタ)
KERNEL_L = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]])

KERNEL_4 = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]],
                      np.uint8)

def convert_image(sub_path):
    os.mkdir(FLAGS.output_path + sub_path)

    # フォルダ内ファイルを変数に格納(ディレクトリも格納)
    files =  os.listdir(FLAGS.input_path + sub_path)

    for file_name in files:
        # 画像ファイル読込
        img = cv2.imread(FLAGS.input_path + sub_path + file_name)

        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # データ型をcv2.CV_64Fにして負の勾配を考慮したラプラシアンフィルタ適用
        img_edged = cv2.filter2D(img_gray, cv2.CV_64F, KERNEL_L)

        # 膨張
        img_result = cv2.dilate(img_edged, KERNEL_4, iterations=1)
        #img_result = cv2.morphologyEx(img_edged, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)))

        #img_result = cv2.Laplacian(img_gray, cv2.CV_32F, ksize=1)

        #ret, img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

        cv2.imwrite(FLAGS.output_path + sub_path + file_name, img_result)

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
        default="./images/output/03laplacian/",
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




