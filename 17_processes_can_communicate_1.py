"""
Simple pipe
"""
import os

if __name__ == "__main__":
    file_descriptor_reader, file_descriptor_writer = os.pipe()
    reader = os.fdopen(file_descriptor_reader)
    writer = os.fdopen(file_descriptor_writer, "w")
    writer.write("Into the pipe I go...")
    # パイプへの書き込み後にwriter をclose
    # これはreader のIO#read がEOF（End Of File *2）まで
    # 読み込むことへの対策.EOF にはそれより先にはもう読み込めるデータが無いことを
    # reader に伝える役割がある。
    writer.close()
    print(reader.read())
