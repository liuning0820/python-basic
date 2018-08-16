def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # 将分号替换为换行符
                new_line = line.replace(';', '\n')
                # 写入新行到输出文件
                outfile.write(new_line)
        print("文件处理完成！")
    except FileNotFoundError:
        print(f"文件 '{input_file}' 不存在。")

if __name__ == "__main__":
    input_file = input("请输入要处理的文件路径：")
    output_file = input("请输入输出文件路径：")

    process_file(input_file, output_file)
