# DFL-cPanel-Auto-Deployment
This repository houses the the cPanel auto-deployment framework for the [DFL Website](http://foyausa.org/index.html)

## Framework Structure
The auto-deployment structure is defined by the bash script [update.sh](./update.sh), which does the following tasks:
1. Run the python scripts to download and populate JSON objects from the DFL master spreadsheet managed by all captains. Objects are found in [players.json](./players.json) and [schedule.json](./schedule.json).
2. Pretty-print JSON objects using `python -m json.tool`
3. Deploy to cPanel by pushing changes made in (1) by this [update.sh](./update.sh)

When changes are made in this repository, cPanel remotely runs the [.yml file](./.cpanel.yml), using the "push deployment" model, which copies the associated JSON objects to the public domain's home folder.

## Using This Repository
This repository allows the DFL captains to input match report data without having to report to the website host. In order to utilize this auto-deployment structure, it is possible to do either of:
* Manually run `./update.sh` at fixed intervals
* Use crontab to periodically run `./update.sh` by taking the following steps
  1. `crontab -e`
  2. Find the absolute path to update.sh, add a leading period, such as `./Users/user/folder/DFL-cPanel-Auto-Deployment/update.sh`, and paste it into the opened crontab file

## References
* https://man7.org/linux/man-pages/man5/crontab.5.html
* https://en.wikipedia.org/wiki/Cron
* https://lornajane.net/posts/2013/pretty-printing-json-with-pythons-json-tool
* https://cpanel.net/