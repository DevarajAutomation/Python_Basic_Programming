def runner_up(score):


    runner_score=[x for x in score if x != max(score)]

    return max(runner_score)


    # win_score=max(score)
    # score.remove(win_score)

    # runner_up = max(score)

    # return runner_up

sc=[2,3,4,4,5]

print(runner_up(sc))