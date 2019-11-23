# Overview

Advice scraper from fucking-great-advice.ru. This is a legacy project that was written several years ago,
the site may have changed since then, so it is possible that you'll have to update the scraper accordingly.

However, the results stored in `out/` are ready for use, and they reflect the state of site at the time
the scraper was written.

## How to use

1. Create and activate virtualenv
2. Install dependencies from `requirements.txt`
3. Run `scrapy crawl advice -o advice-fortune.csv -s JOBDIR=crawls/advice-1`

## Adding fortune to your system

1. `apt install fortune-mod` (this is needed to use `strfile` below; if you already have the fortune file, you only need `fortune` itself)
2. Make sure your CSV file with advices is ready
3. Convert it to the right text format by running `python csv-to-fortune.py` (it takes `advice-fortune.csv` and saves it to `advice-fortune.txt`
4. Run `strfile -c % advice-fortune.txt advice-fortune.dat` to convert it to the fortune format
5. `sudo cp advice-fortune.dat /usr/share/games/fortunes && sudo cp advice-fortune.txt /usr/share/games/fortunes/advice-fortune` (you might have to recreate the directories first)
6. For an extra-dramatic effect: `apt install cowsay`
7. Add `fortune | cowsay` to the end of your `~/.bashrc`
