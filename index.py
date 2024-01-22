def calculate_reward(events: list[tuple[str, int, int]]) -> dict[str, float]:
    RATE_USDT_PER_SEC = 2.778
    MAX_TIME = 3600
    user_rewards = {event[0]: 0 for event in events}  # Initialize rewards for each user
    user_shares = {user: 0 for user, _, _ in events}  # Current shares of each user

    # Include the starting and ending points in the events
    events = sorted(events + [("END", MAX_TIME, 0)], key=lambda x: x[1])

    prev_time = 0
    for user, time, change in events:
        # Calculate the rewards for the interval
        interval = time - prev_time
        total_shares = sum(user_shares.values())
        if total_shares > 0 and interval > 0:
            reward_per_share = (RATE_USDT_PER_SEC * interval) / total_shares
            for u in user_shares:
                user_rewards[u] += reward_per_share * user_shares[u]

        # Update shares
        if user in user_shares:
            user_shares[user] += change

        prev_time = time

    # Round the rewards to 3 decimal places
    return {user: round(reward, 3) for user, reward in user_rewards.items()}

# Test cases
print("Test 1:", calculate_reward([("A", 0, 2), ("B", 2, 1), ("A", 10, -1)]))  # Provided example
print("Test 2:", calculate_reward([("A", 0, 5)]))  # Single user, entire duration
print("Test 3:", calculate_reward([("A", 0, 2), ("B", 10, 2), ("A", 20, -2), ("B", 30, -2)]))  # Multiple changes
print("Test 4:", calculate_reward([]))  # No users
