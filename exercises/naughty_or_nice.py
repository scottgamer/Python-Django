bad_actions = ['broke someone\'s window',
               'fought over a toaster', 'killed a bug']

good_actions = ['got someone a new car',
                'saved a man from drowning', 'never got into a fight']


def whatListAmIOn(actions):
    if not len(actions):
        return

    for action in actions:
        if action.startswith('b') or action.startswith('f') or action.startswith('k'):
            return 'naughty'
        elif action.startswith('g') or action.startswith('s') or action.startswith(''):
            return 'nice'
        else:
            return


print(whatListAmIOn(bad_actions))
