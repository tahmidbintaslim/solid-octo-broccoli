def calculate_reward(events: list[tuple[str, int, int]]) -> dict[str, float]:
    # Constants
    reward_rate = 2.778  # USDT per second
    final_time = 3600    # End timestamp

    # Check for empty event list
    if not events:
        return {}

    # Initialize variables
    user_shares = {}
    user_rewards = {}
    total_shares = 0
    last_timestamp = 0

    # Sort events by timestamp
    events.sort(key=lambda x: x[1])

    for user, timestamp, share_adjust in events:
        # Validate timestamp
        if timestamp < last_timestamp:
            raise ValueError("Timestamps must be non-decreasing")
        time_elapsed = timestamp - last_timestamp

        # Distribute rewards for the elapsed time
        if total_shares > 0 and time_elapsed > 0:
            reward_per_share = time_elapsed * reward_rate
            for u, shares in user_shares.items():
                user_rewards[u] = user_rewards.get(u, 0) + (shares / total_shares) * reward_per_share

        # Update user shares
        user_shares[user] = max(user_shares.get(user, 0) + share_adjust, 0)
        total_shares = sum(user_shares.values())  # Update total shares
        last_timestamp = timestamp

    # Distribute remaining rewards
    remaining_time = final_time - last_timestamp
    if total_shares > 0 and remaining_time > 0:
        reward_per_share = remaining_time * reward_rate
        for u, shares in user_shares.items():
            user_rewards[u] = user_rewards.get(u, 0) + (shares / total_shares) * reward_per_share

    # Round the rewards and return
    return {user: round(reward, 3) for user, reward in user_rewards.items()}
