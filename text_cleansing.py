import string
import csv
import re

import os
os.chdir('I:\Project\ITpoliticsBook\Book\code\ch5')

def processing(text):
    #형태소 분석에 불필요한 요소를 제거하는 단계
    text = re.sub(r'(RT)|(@[A-Za-z0-9]+)|(t.co\/[A-Za-z0-9]*)', '', text, flags=re.MULTILINE)
    return text.replace("~", "").replace("\n", "")

def specialchr(text):
    # 특수문자를 제거하는 단계 ex. !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    table = str.maketrans(dict.fromkeys(( i for i in string.punctuation), ''))
    return text.translate(table)

def processed_tweet(read_file, write_file):
    # 파일 읽기와 쓰기를 수행하는 단계
    with open('{}.csv'.format(read_file), 'r', encoding='utf-8') as f:
        with open('{}.csv'.format(write_file), 'w') as fw:

            csv_reader = csv.reader(f, delimiter = '~')
            csv_writer = csv.writer(fw)
            csv_writer.writerow(['date', 'author_id', 'refined_tweet'])

            for row in csv_reader:

                date = row[0]
                author_id = row[1]
                tweet = row[2]
                print(date, author_id, tweet)
                processed_tweet = processing(tweet)
                refined_tweet = specialchr(processed_tweet)

                csv_writer.writerow([date, author_id, refined_tweet.encode('utf-8')])
 
def main():
    processed_tweet("lee_tweet_search", "lee_tweet_search_cleaned")

if __name__ == "__main__":
    main()
