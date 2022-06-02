# DartsLiveHomeAutoMile

使用此功能前，因為尚未實作註冊APP 用戶，\
需要先下載DartsLive Home 註冊APP 會員後，才可以進行使用。\
(使用DartsLive 會員，登入DartsLive Home APP)

使用Gmail 通知功能，需打開二階段認證以及應用程式Token 才可使用，
之後在user.json 的Notify 欄位填上指定的信，\
以及新增一個.env 對照欄位填入你的Gmail Token 以及寄件者信箱。

# About

支援Asynco 非同步機制，支援Docker Container，\
在APP 未更新前，沒擋版本的情況下基本上都能使用。

# Feature

自動登入\
自動拿Bonus Mile\
自動解任務，會依序打301, 501, 701, cricket, count-up. \
(滿分打，會影響到自身紀錄，有需要者可建立另一個PlayerID)\
通知Email 使用者今日的點數成果\
\
當日已拿過點數後則跳過等下一次。

# Coming soon
