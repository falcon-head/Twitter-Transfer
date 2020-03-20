# Twitter-Transfer
A python automation script that will help you transfer the following users from one account to the another.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Python 3.6](https://img.shields.io/badge/Python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7-blue)](https://www.python.org/download/releases/3.0/) [![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/falcon-head/Twitter-Transfer/graphs/commit-activity) [![contributions welcome](https://img.shields.io/badge/Contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

## Getting Started

1. Clone this repo

```git
git clone https://github.com/falcon-head/Twitter-Transfer.git
```
2. Navigate to the following folder

```windows path
C:\>
C:\> cd C:\[path]\twitter_transfer\twitter_transfer>
```
3. Install all the depending libraries by running `setup.py` 

```windows path
C:\[path]\twitter_transfer\twitter_transfer>python setup.py
```
4. Download [ChromeDriver](https://chromedriver.chromium.org/downloads "Chrome Driver") extract the .exe file and place it inside `C:\[Python path]\Scripts`

## Usage

Run `get_follower_list.py` to get your 'Following' users

```windows path
C:\[path]\twitter_transfer\twitter_transfer>scrapy crawl get_follower_list -a email="twitter_email" -a password="twitter_pass" -o output.csv
```
After getting the ouput in `csv` file run `follow.py` to follow the users in the users list

```windows path
C:\[path]\twitter_transfer\twitter_transfer>scrapy crawl follow -a email="twitter_email" -a password="twitter_pass" -a csv="output.csv"
```
## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/falcon-head/Twitter-Transfer/blob/master/LICENSE)

[MIT](https://github.com/falcon-head/Twitter-Transfer/blob/master/LICENSE)
Copyright (c) 2020 Shrikrishna Joisa
