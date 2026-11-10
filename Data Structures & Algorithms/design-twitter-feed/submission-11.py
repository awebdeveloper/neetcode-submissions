class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.id = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.id += 1
        self.tweets[userId].append((self.id, tweetId))
        
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

        

    def getNewsFeed(self, userId: int) -> List[int]:

        # get all tweets from user and followers if exists
        tweets = list(self.tweets.get(userId, []))
        for id in self.followers.get(userId, set()):
            tweets.extend(self.tweets.get(id, []))
        

        result = []
        count = 0
        heapq.heapify_max(tweets)


        # get latest 10 tweets
        while tweets and count < 10:
            _,tweet = heapq.heappop_max(tweets)
            result.append(tweet)
            count += 1
        
        return result


    def follow(self,  userId: int, followerId: int) -> None:
        if userId == followerId:
            return
        self.followers[userId].add(followerId)
        

    def unfollow(self, userId: int, followerId: int) -> None:
        if userId in self.followers:
            self.followers[userId].discard(followerId);
        
