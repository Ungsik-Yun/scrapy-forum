# scrapy-forum

python scrapy for https://forums.oneplus.net/

it crawls on entire forum on the site, and gathering user-unique-url, wrote date of thread and messge and thread url

## Run

```sh
scrapy crawl theOne
```
run the shell command at scrapy at `/path/to/scrapy-forum/oneplusone`

## Save crawl result to file

```sh
scrapy crawl theOne -o <save-file-name.csv>
```
run the shell command at scrapy at `/path/to/scrapy-forum/oneplusone`. the command will save crawl result in csv format at scrapy root folder.
