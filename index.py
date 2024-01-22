def calculate_reward(events: list[tuple[str, int, int]]) -> dict[str, float]:
    # Variables to define
    user_shares = {}
    user_rewards = {}
    total_shares = 0
    last_timestamp = 0
    
    # main loop
    for user, timestamp, share_adjust in sorted(events, key=lambda x: x[1]):
        time_elapsed = timestamp - last_timestamp
        reward_per_share = time_elapsed * 2.778

        # Distribute rewards for the elapsed time
        if total_shares > 0 and time_elapsed > 0:
            for u in user_shares:
                user_rewards[u] = user_rewards.get(u, 0) + (user_shares[u] / total_shares) * reward_per_share

        # Update user shares
        user_shares[user] = max(user_shares.get(user, 0) + share_adjust, 0)

        # Update total shares
        total_shares = sum(user_shares.values())

        last_timestamp = timestamp

    # Distribute remaining rewards after the last event
    remaining_time = 3600 - last_timestamp
    reward_per_share = remaining_time * 2.778
    if total_shares > 0 and remaining_time > 0:
        for u in user_shares:
            user_rewards[u] = user_rewards.get(u, 0) + (user_shares[u] / total_shares) * reward_per_share

    # Round the rewards to three decimal places
    for user in user_rewards:
        user_rewards[user] = round(user_rewards[user], 3)

    return user_rewards
