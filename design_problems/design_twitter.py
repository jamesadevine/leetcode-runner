"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Twitter:
    """
    Design Twitter (LeetCode #355)

    Design a simplified version of Twitter where users can post tweets,
    follow/unfollow another user, and is able to see the 10 most recent
    tweets in the user's news feed.

    Implement the Twitter class:
    - Twitter() Initializes your twitter object.
    - void postTweet(int userId, int tweetId) Composes a new tweet with ID
      tweetId by the user userId. Each call to this function will be made
      with a unique tweetId.
    - List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent
      tweet IDs in the user's news feed. Each item in the news feed must be
      posted by users who the user followed or by the user themself. Tweets
      must be ordered from most recent to least recent.
    - void follow(int followerId, int followeeId) The user with ID followerId
      started following the user with ID followeeId.
    - void unfollow(int followerId, int followeeId) The user with ID followerId
      started unfollowing the user with ID followeeId.

    Example:
    Input: ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
           [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    Output: [null, null, [5], null, null, [6, 5], null, [5]]

    Constraints:
    - 1 <= userId, followerId, followeeId <= 500
    - 0 <= tweetId <= 10^4
    - All the tweets have unique IDs.
    - At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

    Approach: Hash maps + Min Heap
    - Map userId -> set of followees
    - Map userId -> list of (timestamp, tweetId)
    - getNewsFeed: merge k sorted lists using heap (k = followees + self)
    """

    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass


# This problem requires special handling - it's a class design problem
TEST_CASES = []
METHOD_NAME = None

# Manual test:
# twitter = Twitter()
# twitter.postTweet(1, 5)
# twitter.getNewsFeed(1)   # [5]
# twitter.follow(1, 2)
# twitter.postTweet(2, 6)
# twitter.getNewsFeed(1)   # [6, 5]
# twitter.unfollow(1, 2)
# twitter.getNewsFeed(1)   # [5]
