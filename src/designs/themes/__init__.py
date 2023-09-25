from src.designs.themes.Dark_Theme import DarkTheme
from copy import deepcopy

APPLIED_THEME = DarkTheme()


# function to have a recursive fallback for missing attributes using the parent dict

test_dict = {
        "val1": 1,
        "val2": 2,
        "val3": 4,
        "Text": {
                "val1": 1,
                "val2": 3,
                "val4": 5,
                }
        }


class FallbackDictWrapper:
    def __init__(self, dict):
        self.dict = dict

    def __getitem__(self, *args):
        args = list(*args)
        temp_dict = deepcopy(self.dict)
        key, stack = args[-1], args[:-1]
        ret = None
        print(stack)
        print(key)
        print(len(args))
        if len(args) == 1:
            return self.dict[args]
        while True:
            if key in temp_dict:
                ret = temp_dict[key]
            if len(stack) > 0:
                temp_dict = temp_dict[stack.pop(0)]
            else:
                break
        if ret is None:
            raise KeyError(f"Key {key} not found in dict {self.dict}")
        return ret


test = FallbackDictWrapper(test_dict)

print(test["val2"])
