import subprocess
import json
import sys

# Main methods
def get_fullscreen_index(index):
    fullscreen_spaces = get_spaces(True)
    return fullscreen_spaces[int(index) - 1]["index"]

def get_nonfullscreen_index(index):
    nonfullscreen_spaces = get_spaces(False)
    return nonfullscreen_spaces[int(index) - 1]["index"]

def get_next_space():
    return get_adjacent_space(False, True) if active_is_fullscreen() else get_adjacent_space(False, False)

def get_previous_space():
    return get_adjacent_space(True, True) if active_is_fullscreen() else get_adjacent_space(True, False)

# Helper methods
def get_adjacent_space(prev, fullscreen):
    spaces = get_spaces(True, get_focused_index_display()) if fullscreen else get_spaces(False, get_focused_index_display())
    focused_index = get_focused_index(spaces)
    # new_index = (focused_index - 1) % len(spaces) if prev else (focused_index + 1) % len(spaces)
    new_index = focused_index - 1 if prev else focused_index + 1
    if new_index < 0:
        new_index = 0
    elif new_index >= len(spaces):
        new_index = len(spaces) - 1
    return spaces[new_index]["index"]

def get_spaces(fullscreen, display=None):
    query = get_yabai_query()
    for item in query[:]:
        if fullscreen and not item["is-native-fullscreen"]:
            query.remove(item)
        if not fullscreen and item["is-native-fullscreen"]:
            query.remove(item)
    if display:
        for item in query[:]:
            if item["display"] != display:
                query.remove(item)
    return query

def active_is_fullscreen():
    query = get_yabai_query()
    for item in query:
        if item["has-focus"]:
            return item["is-native-fullscreen"]

def get_yabai_query():
    return json.loads(subprocess.run(['yabai', '-m', 'query', '--spaces'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

def get_focused_index(spaces):
    for i in range(len(spaces)):
        if spaces[i]["has-focus"]:
            return i

def get_focused_index_display():
    spaces = get_yabai_query()
    for space in spaces:
        if space["has-focus"]:
            return space["display"]

if __name__ == '__main__':
    func_name = sys.argv[1]
    if func_name in ["get_fullscreen_index", "get_nonfullscreen_index"]:
        print(globals()[sys.argv[1]](sys.argv[2]))
    else:
        print(globals()[sys.argv[1]]())

