def say(score0, score1):
    score = score0 if who == 0 else score1
    running_h = running_high
    if score > last_score:
        running = score - last_score
        if running > running_high:
            running_h = running
            print(running_high, 'point(s)! The most yet for Player', who)
    return announce_highest(who, score, running_h)


return say


def say(score0, score1):
    nonlocal running_high, last_score
    if who == 0:
        if running_high < score0 - last_score:
            running_high = score0 - last_score
            print(running_high, 'point(s)! The most yet for Player', who)
        last_score = score0
    else:
        if running_high < score1 - last_score:
            running_high = score1 - last_score
            print(running_high, 'point(s)! The most yet for Player', who)
        last_score = score1

    return announce_highest(who, last_score, running_high)


return say
