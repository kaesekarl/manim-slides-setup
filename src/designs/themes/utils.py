from copy import deepcopy


class FallbackDictWrapper:
    """
    A wrapper for a dict that allows to access values by a stack of keys.
    Used for the theme-config and wherever else it might be useful.
    """
    def __init__(self, dict, default_stack=None):
        self.dict = dict
        self.default_stack = default_stack

    def __getitem__(self, *args):
        temp_dict = deepcopy(self.dict)
        default_stack = self.default_stack
        ret = None

        if len(args) == 1:
            key, stack = args[0], default_stack
        else:
            args = list(*args)
            key, stack = args[-1], list(args[:-1])
            stack = default_stack + stack

        if len(stack) == 0:
            return self.dict[key]
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
