class Twitter:

    def __init__(self):
        self.followers = collections.defaultdict(list)
        self.tweets = collections.defaultdict(list)
        self.newsfeed = collections.defaultdict(list)
        self.timer = 0

    def _add_self_follower(self, userId):
        self.followers[userId].append(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # method 1-- 
        # 1. add tweet in tweets and 
        # 2. also add in every followers newsfeed
        self.timer += 1
        self.tweets[userId].append((-self.timer, tweetId))
        
        if userId not in self.followers:
            self._add_self_follower(userId)
        
        for follower in self.followers[userId]:
            heapq.heappush(self.newsfeed[follower], (-self.timer, tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # method 1-- 
        # return the top 10 for that user id. 
        res = []
        temp = []
        while self.newsfeed[userId] and len(res) < 10: 
            temp_elem = heapq.heappop(self.newsfeed[userId])
            res.append(temp_elem[1])
            temp.append(temp_elem)
        
        # put it back in the pq 
        while temp:
            heapq.heappush(self.newsfeed[userId], temp.pop())
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # method 1-- 
        # add to followers map 
        # pick tweets from the followee and 
        # add to the newsfeed of the follower
        if followerId not in self.followers:
            self._add_self_follower(followerId)
        
        if followeeId not in self.followers:
            self._add_self_follower(followeeId)
        
        if followerId == followeeId:
            # disallow doubling self following loop. 
            # We self follow by default. No need to duplicate it. 
            return 

        # disallow same person from sending same request again
        # disallow duplication 
        for follower in self.followers[followeeId]:
            if follower == followerId:
                return 

        self.followers[followeeId].append(followerId)
        
        for tweet in self.tweets[followeeId]:
            heapq.heappush(self.newsfeed[followerId], (tweet[0], tweet[1], followeeId))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # method 1-- 
        # remove from the followers map 
        # remove tweets from the the followeeId from the newsfeed 

        # disallow self following 
        if followerId == followeeId:
            return

        for i, follower in enumerate(self.followers[followeeId]):
            if follower == followerId:
                self.followers[followeeId].pop(i)
                break
        #print(f"unfollowed: follower {followerId}, followee: {followeeId}")
        #print(f"resultant followers: {self.followers}")

        temp = []
        while self.newsfeed[followerId]:
            temp_elem = heapq.heappop(self.newsfeed[followerId])
            if temp_elem[2] != followeeId:
                temp.append(temp_elem)
        
        while temp:
            self.newsfeed[followerId].append(temp.pop())
        
        heapq.heapify(self.newsfeed[followerId])

