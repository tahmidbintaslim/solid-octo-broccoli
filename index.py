from typing import List, Tuple, Dict

def calculate_reward(events: List[Tuple[str, int, int]]) -> Dict[str, float]:
    # Initialize variables to keep track of user shares and rewards
    user_shares = {}
    user_rewards = {}
    
    # Initialize the timestamp and total shares
    timestamp = 0
    total_shares = 0
    
    # Iterate through the events
    for event in events:
        user, event_timestamp, share_adjust = event
        
        # Calculate the time duration
        time_duration = event_timestamp - timestamp
        
        # Calculate the tokens to be distributed during this time duration
        tokens_to_distribute = time_duration * 2.778
        
        # Update the total shares based on user's share adjustment
        if user in user_shares:
            user_shares[user] += share_adjust
        else:
            user_shares[user] = max(share_adjust, 0)  # User's shares can never be negative
        
        # Update the total shares in the system
        total_shares += max(share_adjust, 0)  # Only positive share adjustments
        
        # Calculate and distribute rewards to users based on their shares
        for user, shares in user_shares.items():
            user_rewards[user] = user_rewards.get(user, 0) + (shares / total_shares) * tokens_to_distribute
        
        # Update the timestamp
        timestamp = event_timestamp
    
    return user_rewards

# Test cases
events = [("A", 0, 2), ("B", 2, 1), ("A", 10, -1)]
result = calculate_reward(events)
print(result)  # Expected Output: {"A": 5005.556, "B": 4994.444}
