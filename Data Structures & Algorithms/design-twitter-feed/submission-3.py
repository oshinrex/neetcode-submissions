class Twitter:

    def __init__(self):
        # user : who they follow
        self.users = defaultdict(set)

        # user : their posts
        self.posts = defaultdict(list)
        self.tweet = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.tweet, tweetId))
        self.tweet += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.users[userId] | {userId}
        heap = []
        for u in users: 
            p = len(self.posts[u]) - 1

            if p >= 0: 
                num, tweet = self.posts[u][p]
                heapq.heappush(heap, (-num, u, p, tweet))

        res = []

        while len(res) < 10 and heap: 
            _, u, p, tweet = heapq.heappop(heap)
            res.append(tweet)
            
            if p > 0: 
                num, t = self.posts[u][p - 1]
                heapq.heappush(heap, (-num, u, p - 1, t))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
