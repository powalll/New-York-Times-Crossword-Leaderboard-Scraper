# New York Times Crossword Leaderboard Scraper
A web scraper for the NYT Mini Leaderboard
## Data Format
The CSV returns the following data (at time of scraping): Position, Name, Time, and Time in seconds\
If a player has yet to complete the crossword, the time and time in seconds will be output as "--" and the position will be "�"
[leaderboard.csv](https://github.com/powalll/New-York-Times-Crossword-Leaderboard-Scraper/files/7835980/leaderboard.csv)

| Position      | Name          | Time     | Time in seconds |
| ------------- | ------------- | -------- | -------------   |
| 1             | Name1         | 0:33     |   33            |
| 2             | Name2         | 0:37     |   37            |
| 3             | Name3         | 0:38     |   38            |
| 4             | Name4         | 0:58     |   58            |
| 5             | Name5         | 1:22     |   82            |
| 6             | Name6         | 1:23     |   83            |
| �            | Name7         | --       |   --            |
| �            | Name8         | --       |   --            |
| �            | Name9         | --       |   --            |
| �            | Name10        | --       |   --            |
| �            | Name11        | --       |   --            |
| �            | Name12        | --       |   --            |
## Usage
1. Install requirements.txt
```
pip install -r requirements.txt
```
2. Go to headers in the python script and add your headers values
   - This can be obtained by first going signing into nyt and going to https://www.nytimes.com/puzzles/leaderboards 
   - Then open developer tools (Ctrl+shift+I) and go to the network tab 
   - Refresh the page and scroll up to find the request called leaderboards, right click leaderboards -> Copy -> copy as cURL (bash)
   - Then insert the cURL to https://curlconverter.com/, select language as Python, and add your header values to the script 

```
headers = {
   *Insert values here*
}
```
<img width="344" alt="nyt crossword leaderboard screenshot" src="https://user-images.githubusercontent.com/67936152/148703808-3c758759-712f-4f26-9cca-db25f56908ef.png">

