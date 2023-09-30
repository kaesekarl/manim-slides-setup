from copy import deepcopy


class FallbackDictWrapper:
    """
    A wrapper for a dict that allows to access values by a stack of keys.
    Used for the theme-config and wherever else it might be useful.
    """

    def __init__(self, dict, default_stack=None):
        self.dict = dict
        self.default_stack = default_stack

    def __getitem__(self, route: str):
        temp_dict = deepcopy(self.dict)
        default_stack = self.default_stack
        ret = None
        stack = None
        key = None

        # Preparing strings into lists for easier handling
        if default_stack is None:
            default_stack = []
        if isinstance(default_stack, str):
            default_stack = default_stack.split(" ")
        elif isinstance(default_stack, list):
            pass
        else:
            raise TypeError(f"Expected str or list, got {type(default_stack)}")

        if isinstance(route, str):
            stack = route.split(" ")
        elif isinstance(route, list):
            stack = route
        else:
            raise TypeError(f"Expected str or list, got {type(route)}")

        key, stack = stack[-1], stack[:-1]
        stack = stack + default_stack

        if len(stack) == 0:
            if key in temp_dict:
                ret = temp_dict[key]
            else:
                raise KeyError(f"Key {key} not found in {temp_dict}")
            return ret

        for d in stack:
            if key in temp_dict:
                ret = temp_dict[key]
            if d in temp_dict:
                temp_dict = temp_dict[d]
            else:
                raise KeyError(f"Key {d} not found in {temp_dict}")
            if key in temp_dict:
                ret = temp_dict[key]

        return ret

