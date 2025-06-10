import inspect
import copy


class BaseConfig:
    def __init__(self) -> None:
        """ Initializes all member classes recursively. Ignores all names starting with '__' (built-in methods)."""
        self.init_member_classes(self)
        self.merge_dicts()

    @staticmethod
    def init_member_classes(obj):
        # iterate over all attributes names
        for key in dir(obj):
            # disregard builtin attributes
            if key == "__class__":
                continue
            # get the corresponding attribute object
            var = getattr(obj, key)
            # check if it the attribute is a class
            if inspect.isclass(var):
                # instantiate the class
                i_var = var()
                # set the attribute to the instance instead of the type
                setattr(obj, key, i_var)
                # recursively init members of the attribute
                BaseConfig.init_member_classes(i_var)

    def merge_dicts(self):
        """Merge dictionaries from parent classes with child class dictionaries."""
        for key in dir(self):
            # Skip special attributes and built-in methods
            if key.startswith('__') or key in ['__weakref__', '__dict__', '__module__', '__doc__']:
                continue
            var = getattr(self, key)
            if isinstance(var, dict):
                # Get the parent class's dictionary if it exists
                parent_dict = None
                for base in self.__class__.__bases__:
                    if hasattr(base, key):
                        parent_var = getattr(base, key)
                        if isinstance(parent_var, dict):
                            parent_dict = parent_var
                            break
                if parent_dict is not None:
                    # Merge dictionaries, with child values taking precedence
                    merged_dict = parent_dict.copy()
                    merged_dict.update(var)
                    setattr(self, key, merged_dict)
            elif hasattr(var, 'merge_dicts'):
                # If the attribute is a class instance that has merge_dicts method, call it
                var.merge_dicts()
            elif isinstance(var, object):
                # Create a new instance of the class to avoid modifying read-only attributes
                new_var = copy.deepcopy(var)
                # Recursively merge dictionaries in the new instance
                for nested_key in dir(var):
                    # Skip special attributes and built-in methods
                    if nested_key.startswith('__') or nested_key in ['__weakref__', '__dict__', '__module__', '__doc__']:
                        continue
                    nested_var = getattr(var, nested_key)
                    if isinstance(nested_var, dict):
                        # Get the parent class's dictionary if it exists
                        parent_dict = None
                        for base in self.__class__.__bases__:
                            if hasattr(base, key):
                                parent_obj = getattr(base, key)
                                if hasattr(parent_obj, nested_key):
                                    parent_var = getattr(parent_obj, nested_key)
                                    if isinstance(parent_var, dict):
                                        parent_dict = parent_var
                                        break
                        if parent_dict is not None:
                            # Merge dictionaries, with child values taking precedence
                            merged_dict = parent_dict.copy()
                            merged_dict.update(nested_var)
                            setattr(new_var, nested_key, merged_dict)
                # Replace the original object with the new one
                setattr(self, key, new_var)
