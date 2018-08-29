#!/usr/bin/env python2.7
import psycopg2


def setUpDatabase(query):
    conn = psycopg2.connect("dbname = news")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows


def mostPopularArticles():
    query = '''select quote_ident(articles.title), count(log.path) as num
            from articles, log
            where lower(articles.slug) like substr(lower(log.path),10)
            group by articles.title
            order by num desc;
    '''
    rows = setUpDatabase(query)
    for row in rows:
        print
        row[0] + "-" + str(row[1]) + " views"


def mostPopularAuthors():
    query = '''select quote_ident(authors.name), count(log.path) as num
            from authors, log, articles where
            authors.id = articles.author and
            lower(articles.slug) like substr(lower(log.path),10)
            group by authors.name
            order by num desc;
    '''
    rows = setUpDatabase(query)
    for row in rows:
        print
        row[0] + "-" + str(row[1]) + " views"


def badDay():
    query = '''select to_char(log.time, 'Month DD,YYYY') as x,
    round(
        count(
            case when log.status != '200 OK' then 1 end)*1.0/count(*)*100
                , 1) as y
    from log group by x
    having count(
        case when log.status != '200 OK' then 1 end)*1.0/count(*)*100 > 1;
;
    '''
    rows = setUpDatabase(query)
    for row in rows:
        print
        str(row[0]) + "-" + str(row[1]) + "% errors"


if __name__ == '__main__':
    mostPopularArticles()
    mostPopularAuthors()
    badDay()
