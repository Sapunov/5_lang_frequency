# 5_lang_frequency

Скрипт для нахождения самых частовстречаемых слов в любом тексте

```{r, engine='bash'}
$ python lang_frequency.py --help
usage: lang_frequency.py [-h] -f FILEPATH [-n N] [-m MIN_LENGTH]

Get most frequent words from FILENAME

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        File path
  -n N                  Number of words to print. Default: 10
  -m MIN_LENGTH, --min-length MIN_LENGTH
                        Minimum word length for evaluation. Default: None
```

## Использование

```{r, engine='bash'}
$ python lang_frequency.py -f wiki_love.txt 
#     Word                     Freq
1     и........................91
2     в........................65
3     любовь...................60
4     любви....................38
5     к........................24
6     что......................21
7     не.......................18
8     его......................17
9     с........................16
10    на.......................15
```

В качестве примера используется файл `wiki_love.txt`, содержащий текст статьи из Википедии [про любовь](https://ru.wikipedia.org/wiki/%D0%9B%D1%8E%D0%B1%D0%BE%D0%B2%D1%8C).

> Скрипт использует python 3 версии.


## Параметры

- `-f/--filepath` - путь до входного файла
- `-n` - количество слов, которое нужно вывести. По умолчанию будет выведено 10 самых встречаемых слов.
- `-m/--min-length` - длина слов, которые нужно брать в рассмотрение. По умолчанию скрипт не учитывает длину слов.

Тот же самый пример, но с заданными параметрами

```{r, engine='bash'}
$ python lang_frequency.py -f wiki_love.txt -n 5 -m 7
#     Word                     Freq
1     человека.................11
2     человеку.................6
3     понятие..................5
4     животных.................5
5     единения.................5
```

## Лицензия

[Creative Commons Attribution License](http://creativecommons.org/licenses/by/2.0/)

