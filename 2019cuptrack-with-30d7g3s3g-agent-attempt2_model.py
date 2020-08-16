def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    speed = params['speed']
    progress = params['progress']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 10
    elif distance_from_center <= marker_2:
        reward = 5
    elif distance_from_center <= marker_3:
        reward = 2
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    
    if all_wheels_on_track:
        reward = reward*2
    
    
    # Steering penality threshold, change the number based on your action space setting
    # Ruchita - based on my action space & the agent, highest steering at 30deg happens at action number 18
    ABS_STEERING_THRESHOLD = 20

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    
    
    # Ruchita - also penalize if the speed is too high while steering
    if steering >= 20 and speed > 1:
        reward *= 0.7
        
    if steering >= 15 and speed > 2:
        reward *= 0.7
        
        
    # reward for finishing track    
    if progress < 25:
        reward *= 0.2
    
    if progress < 50:
        reward *= 0.5
    
    if progress >= 75:
        reward *= 2
    
    if progress == 100:
        reward *= 3
    
    
    return float(reward)