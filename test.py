from PIL import Image, ImageDraw

# 指定输入的 txt 文件路径和 jpg 图片路径
txt_file_path = "test/scene1/IMG_1.txt"
jpg_file_path = "test/scene1/IMG_1.jpg"

# 读取 txt 文件中的坐标
coordinates = []
with open(txt_file_path, "r") as file:
    for line in file:
        x, y = map(float, line.strip().split())
        coordinates.append((x, y))

# 打开 jpg 图片
image = Image.open(jpg_file_path)

# 创建一个可以在图片上绘制的对象
draw = ImageDraw.Draw(image)

# 在图片上绘制红点
radius = 3  # 红点的半径
fill_color = (255, 0, 0)  # 红色
for x, y in coordinates:
    x_pixel = int(x)  # 将浮点数转换为像素坐标
    y_pixel = int(y)
    draw.ellipse((x_pixel - radius, y_pixel - radius, x_pixel + radius, y_pixel + radius), fill=fill_color)

# 保存绘制后的图片
output_file_path = "./output_image.jpg"
image.save(output_file_path)

# 显示绘制后的图片
image.show()
