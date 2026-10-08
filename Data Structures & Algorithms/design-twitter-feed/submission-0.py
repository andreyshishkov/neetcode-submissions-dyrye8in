class Twitter:

    def __init__(self):
        self.count = 0
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list) # user_id -> [count, tweet_id]
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        if len(self.tweet_map[userId]) > 10:
            self.tweet_map[userId].pop(0)
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.follow_map[userId].add(userId)
        if len(self.follow_map[userId]) >= 10:
            max_heap = []
            for followeeId in self.follow_map[userId]:
                if followeeId in self.tweet_map:
                    index = len(self.tweet_map[followeeId]) - 1
                    count, tweetId = self.tweet_map[followeeId][index]
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])
                    if len(max_heap) > 10:
                        heapq.heappop(max_heap)
            while max_heap:
                count, tweet_id, followee_id, index = heapq.heappop(max_heap)
                heapq.heappush(min_heap, [-count, tweet_id, followee_id, index])
        else:
            for followeeId in self.follow_map[userId]:
                if followeeId in self.tweet_map:
                    index = len(self.tweet_map[followeeId]) - 1
                    count, tweetId = self.tweet_map[followeeId][index]
                    heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])


        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
