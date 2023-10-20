import os
import shutil
from scipy.io import loadmat

# 向train.list写入
for task in ["train","test"]:
    # 获取train/images中所有文件
    images = os.listdir(f"{task}/images")
    with open(f"{task}.list", "w") as f:
        for image in images:
            # 获取文件名的数字部分
            num = image.split(".")[0].split("_")[-1]
            # 创建文件夹 scene_{num}
            os.makedirs(f"{task}/scene{num}")
            # 拷贝文件
            shutil.copy(f"{task}/images/{image}", f"{task}/scene{num}")
            # 处理label
            mat = loadmat(f"{task}/ground-truth/GT_IMG_{num}.mat")
            gt = mat["image_info"][0,0][0,0][0]
            # label写入txt
            with open(f"{task}/scene{num}/IMG_{num}.txt", "w") as gtf:
                # 将gt中每个元素作为一行写入
                for i in gt:
                    gtf.write(f"{i[0]} {i[1]}\n")
            # 写入文件
            f.write(f"{task}/scene{num}/{image} {task}/scene{num}/IMG_{num}.txt\n")

        