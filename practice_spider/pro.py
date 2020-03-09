#document_1602.txt的地址，直接粘贴即可
# from kkb_tools import open_file
#书写你的代码
connent = input('您输入的是：')
myfile = open(r'document_1602.txt','w')
myfile.write(connent)
# open_file("document_1602.txt")
myfile.close()


