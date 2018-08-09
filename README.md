## The code consists of 3 function.
mostPopularArticles(): displays the most popular articles and number of views.
mostPopularAuthors(): displays the most popular authors and number of views.
badDay(): displays the days that has the most errors.

# Setup the environment to run the code:
## Setup the virtual machine and vagrant
1. [install virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_2)
2. [install vagrant](https://www.vagrantup.com/)
3. `vagrant init ubuntu/trusty64`
4. `vagrant up`

## To set up the database:
1. [download news.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. `psql -d news -f newsdata.sql`

## To run the code:
2. [clone the rep](https://github.com/ms10596/Logs-Analysis)
3. cd to the downloaded folder
3. `python Log.py`


