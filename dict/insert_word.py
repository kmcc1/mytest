import pymysql
f = open('dict.txt')
db = pymysql.connect('localhost','root','123456','dictionary_query')
cursor = db.cursor()
for line in f:
    tmp = line.split(' ')
    word = tmp[0]  # 获取单词
    mean = ' '.join(tmp[1:]).strip()

    sql = 'insert into words (word,mean) VALUES ("%s","%s")'%(word,mean)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

f.close()